import argparse
import json
import os
import time

from ..misassemblyFixerLib import merger 

from ..repeatPhaserLib import abunGraphLib
from ..repeatPhaserLib import abunHouseKeeper
from ..repeatPhaserLib import abunSplitter
from ..repeatPhaserLib.finisherSCCoreLib import alignerRobot
from ..repeatPhaserLib.finisherSCCoreLib import graphLib
from ..repeatPhaserLib.finisherSCCoreLib import houseKeeper
from ..repeatPhaserLib.finisherSCCoreLib import nonRedundantResolver

def runASplitter(args):
    t0 = time.time()

    print "args", args
    pathExists, newFolderName, newMummerLink = houseKeeper.checkingPath(args['folderName'], args['mummerLink'])

    if args['segmentcount'] != None:
        houseKeeper.globalParallelFileNum = int(args['segmentcount'])
    else:
        houseKeeper.globalParallelFileNum = 20

    if args['fast'] == "True":
        houseKeeper.globalFast = True
    else:
        houseKeeper.globalFast = False

    if args['parallel'] != None:
        houseKeeper.globalParallel = int(args['parallel'])
    else:
        houseKeeper.globalParallel = 20

    if args['large'] == "True":
        houseKeeper.globalLarge = True
    else:
        houseKeeper.globalLarge = False

    print "houseKeeper.globalLarge, houseKeeper.globalParallelFileNum , houseKeeper.globalRunMPI ", \
    houseKeeper.globalLarge, houseKeeper.globalParallelFileNum , houseKeeper.globalRunMPI 
    
    if args['avoidrefine'] == "False":
        abunHouseKeeper.abunGlobalAvoidrefine = False
    else:
        abunHouseKeeper.abunGlobalAvoidrefine = True

    if args['readsearch'] != None:
        abunHouseKeeper.abunGlobalReadSearchDepth = int(args['readsearch']) 
    else:
        abunHouseKeeper.abunGlobalReadSearchDepth = 0


    if args['basicgraph'] == "False":
        abunHouseKeeper.abunGlobalBasicGraph = False
    else:
        abunHouseKeeper.abunGlobalBasicGraph = True

    if args['abunreplow'] != None:
        abunHouseKeeper.abunGlobalRepLower = int(args['abunreplow'])
    else:
        abunHouseKeeper.abunGlobalRepLower = 0


    if args['replace'] != None : 
        if  args['replace'] == 'skip':
            print "skip copy"
        else:
            abunHouseKeeper.replaceFiles( newFolderName, args['replace']) 
    else:
        abunHouseKeeper.replaceFiles( newFolderName, "mFixed.fasta")

    if args['RRDisable'] == "False":
        abunHouseKeeper.abunGlobalRRDisable = False
    else:
        abunHouseKeeper.abunGlobalRRDisable = True

    if args['pickup'] in ["find", "map", "count", "split", "graph", "collapse"] :
        abunHouseKeeper.abunGlobalRunPickUp = args['pickup']

    if args['runemalgo'] == "True":
        abunHouseKeeper.abunGlobalRunEM = True
    else:
        abunHouseKeeper.abunGlobalRunEM = False

    if args['option'] != None:
        settingDataCombo = args['option'].split()
        settingDic = {}

        for eachitem in settingDataCombo:
            tmp = eachitem.split('=')
            settingDic[tmp[0]] = tmp[1]

        canLoad = abunHouseKeeper.abunGlobalSplitParameterRobot.loadData(settingDic)
    else:
        canLoad = True    

    if canLoad:
        settingDic = abunHouseKeeper.abunGlobalSplitParameterRobot.__dict__
        with open(newFolderName + "option.json", 'w') as f:
            json.dump(settingDic, f)


    if pathExists and canLoad:
        abunSplitter.mainFlow(newFolderName, newMummerLink)
    else:
        print "Sorry. The above folders or files are missing or options are not correct. If you continue to have problems, please contact me(Ka-Kit Lam) at kklam@eecs.berkeley.edu"

    print  "Time", time.time() - t0

def runMFixer(args):
    t0 = time.time()
    if args['segmentcount'] != None:
        houseKeeper.globalParallelFileNum = int(args['segmentcount'])
    else:
        houseKeeper.globalParallelFileNum = 20

    if args['large'] == "True":
        houseKeeper.globalLarge = True
    else:
        houseKeeper.globalLarge = False

    print "houseKeeper.globalLarge, houseKeeper.globalParallelFileNum , houseKeeper.globalRunMPI ", \
        houseKeeper.globalLarge, houseKeeper.globalParallelFileNum , houseKeeper.globalRunMPI 
    
    #assert(False)

    if args['parallel'] != None:
        houseKeeper.globalParallel = int(args['parallel'])
    else:
        houseKeeper.globalParallel = 20

    if args['LCReads'] == None:
        merger.mergerGlobalLCReads = "LR"
    elif args['LCReads'] == "LR":
        merger.mergerGlobalLCReads = "LR"
    elif args['LCReads'] == "SR":
        merger.mergerGlobalLCReads = "SR"

    pathExists, newFolderName, newMummerLink = houseKeeper.checkingPath(args['folderName'] , args['mummerLink'], False)

    if args['cleanInput'] == "True":
        fileList = ["SC.fasta", "LC.fasta", "SR.fasta", "LR.fasta"]

        for eachitem in fileList:
                os.system("sed -e 's/|//g' " + newFolderName + eachitem+"  > " + newFolderName + "tmp.fasta")
                os.system("cp " + newFolderName + "tmp.fasta " + newFolderName + eachitem )


    if args['option'] != None:
        settingDataCombo = args['option'].split()
        settingDic = {}

        for eachitem in settingDataCombo:
            tmp = eachitem.split('=')
            settingDic[tmp[0]] = tmp[1]

        canLoad = merger.mergerGlobalFixerRobot.loadData(settingDic)
    else:
        canLoad = True    


    if canLoad:
        settingDic = merger.mergerGlobalFixerRobot.__dict__
        with open(newFolderName + "optionMFixer.json", 'w') as f:
            json.dump(settingDic, f)


    if canLoad == True:
        merger.mainFlow(newFolderName, newMummerLink)
    else: 
        print "Sorry. The above folders or files are missing or options are not correct. If you continue to have problems, please contact me(Ka-Kit Lam) at kklam@eecs.berkeley.edu"

    print  "Time", time.time() - t0

def runMPIWorker(comm):
    while True:
        data = comm.recv(source=0)

        if data == "endall":
            break

        elif len(data) > 0 and data[0] == "nucmerjob":
            mummerLink, folderName, outputName, referenceName, queryName, specialForRaw , specialName , refinedVersion= data[1:]
            alignerRobot.useMummerAlign(mummerLink, folderName, outputName, referenceName, queryName, specialForRaw , specialName , refinedVersion)
            comm.send(data, dest=0)
        elif len(data) > 0 and data[0] == "gapjob":
            eachmatchpair,folderName, N1,  mummerLink,  contigReadGraph, contigFilename,readsetFilename = data[1:]
            newdata = abunGraphLib.singleGapLookUp(eachmatchpair,folderName, N1,  mummerLink,  contigReadGraph, contigFilename,readsetFilename)
            comm.send(newdata, dest=0)
        elif len(data) > 0 and data[0] == "onlynucmer":
            specialForRaw, mummerLink, folderName, outputName, referenceName, queryName,refinedVersion = data[1:]
            alignerRobot.nucmerMummer(specialForRaw, mummerLink, folderName, outputName, referenceName, queryName,refinedVersion)
            comm.send(data, dest=0)
        elif len(data) > 0 and data[0] == "parallelpath":
            #data = "nothing"
            ### need to fix what to process here... 
            # Input here : startindex, endindex, N1, folderName, contigReadGraph
            # Output here : adjList = [  [1, [2,3,4]] , [ 2, [3, 4, 5] ], ..., ]
            startindex, endindex, N1, folderName, contigReadGraph= data[1] ,data[2], data[3] , data[4] , data[5]

            G = graphLib.seqGraph(0)
            G.loadFromFile(folderName, contigReadGraph)

            adjList = []

            for i in range(startindex, endindex):
                tmpList = abunGraphLib.findAllReachable(i, N1, G)
                adjList.append([i, tmpList])

            print "0: send", adjList, startindex, endindex
            comm.send(adjList, dest=0)

def runJob(args, jobname):
    if args['runmpi'] == "True":
        houseKeeper.globalRunMPI = True
    else:
        houseKeeper.globalRunMPI = False

    me = 0 

    if houseKeeper.globalRunMPI == True:
        from mpi4py import MPI
        from mpi4py.MPI import ANY_SOURCE
        comm = MPI.COMM_WORLD
        me = comm.Get_rank()
        nproc = comm.Get_size()

    if me ==0 :
        if jobname == "asplitter":
            runASplitter(args)
        elif jobname == "mfixer":
            runMFixer(args)

        if houseKeeper.globalRunMPI == True:
            for i in range(1, nproc):
                data = "endall"
                comm.send(data, dest=i)
    else:
        runMPIWorker(comm)


