import argparse

'''
Sample run example
python srcRefactor/createJob.py \
	-ma mem \
	-to mfixer \
	-wd myworkdir \
	-dd mydatadir 

qsub myJob

'''

def createShellScript():
	f = open( args['workdir'] + "bashScript.sh" , 'w')	

	if args['machine'] == "simple":
		pythonheader = "python -m "
		isMPI = "-mpi False "
	else:
		pythonheader = "python-mpi -m"
		isMPI = "-mpi True "

	
	if args['tool'] == "mfixer":
		toolName  = "srcRefactor.misassemblyFixerLib.mFixer "
	elif args['tool'] == "asplitter":
		toolName = "srcRefactor.repeatPhaserLib.aSplitter "
	else:
		print "No tool for this"
		assert(False)

	if args['machine'] == "simple":
		optionToRun = "-par 20 "
	elif args['machine'] == "highpar":
		optionToRun = "-sc 90 -l True "
	elif args['machine'] == "highmem":
		optionToRun = "-sc 20 "


	pythonCommand = pythonheader + " " + toolName + " " +  isMPI + " " +  optionToRun + " " + args['datadir'] + " " + args['mumdir'] 

	commandString = ("#!/bin/sh\n"
				 	 "module load python\n"
					 "module load mpi4py\n"
					 "" + pythonCommand + "\n"
					)

	f.write(commandString)
	f.close()


def createJobSpec():
	f = open("myJob", 'w')
	numMPI = -1
	aprunCommand  = "" 
	
	if args['machine'] == "simple":	
		aprunCommand = "aprun -n 1 -d 24 " + args['workdir'] + "bashScript.sh" +"\n"
		numMPI = 24 

	elif args['machine'] == "highpar":
		aprunCommand = "aprun -n 90 -N 8 " + args['workdir'] + "bashScript.sh" +"\n"
		numMPI = 288 

	elif args['machine'] == "highmem":
		aprunCommand = "aprun -n 20 -N 1 " + args['workdir'] + "bashScript.sh" +"\n"
		numMPI = 504 
	else:
		print "Invalid machine type"
		assert(False)

	jobString = ("#PBS -q debug\n"
				 "#PBS -l mppwidth=" + str(numMPI) + "\n"
				 "#PBS -l walltime=00:29:00\n" 
				 "#PBS -N metajob\n" 
				 "#PBS -j oe\n"
				 "\n"
				 "cd " + args['workdir'] + "\n"
				 "" + aprunCommand + "\n"
				)
	

	f.write(jobString)			
	f.close()


parser = argparse.ArgumentParser(description='qsubJobGenerator')
parser.add_argument('-ma', '--machine', required=True)
parser.add_argument('-to', '--tool', required=True)
parser.add_argument('-wd', '--workdir', required=True)
parser.add_argument('-dd', '--datadir', required=True)
parser.add_argument('-md', '--mumdir', required=True)


args = vars(parser.parse_args())
if args['workdir'][-1] != '/':
	args['workdir'] = args['workdir'] + "/"

if args['datadir'][-1] != '/':
	args['datadir'] = args['datadir'] + "/"

if args['mumdir'][-1] != '/':
	args['mumdir'] = args['mumdir'] + "/"

createJobSpec()
createShellScript()


