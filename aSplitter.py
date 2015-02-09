import abunSplitter

from finisherSCCoreLib import houseKeeper
import time
import argparse

t0 = time.time()

parser = argparse.ArgumentParser(description='aSplitter')
parser.add_argument('folderName')
parser.add_argument('mummerLink')

parser.add_argument('-f', '--fast', help= 'Fast aligns contigs (input is True)', required=False)
parser.add_argument('-par', '--parallel', help= 'Fast aligns contigs (input is maximum number of threads)', required=False)
parser.add_argument('-l', '--large', help= 'Large number of contigs/large size of contigs (input is True)', required=False)




args = vars(parser.parse_args())

print "args", args
pathExists, newFolderName, newMummerLink = houseKeeper.checkingPath(args['folderName'], args['mummerLink'])

if args['fast'] == "True":
    houseKeeper.globalFast = True
else:
    houseKeeper.globalFast = False

if args['parallel'] != None:
    houseKeeper.globalParallel = int(args['parallel'])
else:
    houseKeeper.globalParallel = 1


if args['large'] == "True":
    houseKeeper.globalLarge = True
else:
    houseKeeper.globalLarge = False


if pathExists:
    abunSplitter.mainFlow(newFolderName, newMummerLink)
else:
    print "Sorry. The above folders or files are missing. If you continue to have problems, please contact me(Ka-Kit Lam) at kklam@eecs.berkeley.edu"

print  "Time", time.time() - t0
