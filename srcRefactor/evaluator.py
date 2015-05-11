import time
import datetime
import argparse
import os
import json
import re


from repeatPhaserLib import abunHouseKeeper
from repeatPhaserLib.finisherSCCoreLib import houseKeeper
	
def runEvaluation(quastPath, folderName,paraFileName, outputFilename):
	command = "python "+quastPath+" " + folderName +"abun.fasta -o "  + folderName + "   -R  " + folderName + "reference.fasta"
	os.system(command)
	
	f = open(outputFilename , 'a')
	tmpString  = ""
	st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d~%H:%M:%S')
	
	tmpString = tmpString + str(st) + ","
    
	with open(folderName+paraFileName) as fdic:
		myDic = json.load(fdic)


	for eachitem in myDic:
		tmpString = tmpString + str(myDic[eachitem]) + ","
	
	quastReport = folderName + "report.txt"
	
	regex = re.compile("misassemblies*")

	misassembly = str(1997)
	ncontig = str(1997) 
	
	with open(quastReport) as f2:
	    for line in f2:
	        result = re.match("# misassemblies (.*?) .*", line)
	        if result != None: 
		        ans = result.group(0).split()
		        misassembly = ans[2]
	        
	        result = re.match("# contigs \(>= 0 bp\) (.*?) .*", line)
	        if result != None: 
		        ans = result.group(0).split()
		        ncontig=ans[-1]

	
	tmpString = tmpString  + misassembly + "," + ncontig+ "\n"

	f.write(tmpString)

	f.close()


def loggHeaders(folderName, outputFilename):

	myDic =  abunHouseKeeper.abunGlobalSplitParameterRobot.__dict__
	f = open(outputFilename , 'a')
	tmpString  = ""
	st = "time"
	
	tmpString = tmpString + str(st) + ","

	for eachitem in myDic:
		tmpString = tmpString + eachitem + ","

	tmpString = tmpString  + "misassembly" + "," + "ncontig"+ "\n"

	f.write(tmpString)
	f.close()


parser = argparse.ArgumentParser(description='evaluation')

parser.add_argument('--option', required = True)
parser.add_argument('--quastPath' , required=False)
parser.add_argument('--folderName' , required=False)
parser.add_argument('--paraFileName' , required=False)
parser.add_argument('--outputFilename' , required=False)


args = vars(parser.parse_args())
quastPath, folderName,paraFileName, outputFilename = args['quastPath'], args['folderName'], args['paraFileName'], args['outputFilename']

if args['option'] == 'header' :
	loggHeaders(folderName, outputFilename)
elif args['option'] == 'evaluate':
	runEvaluation(quastPath, folderName,paraFileName, outputFilename)







