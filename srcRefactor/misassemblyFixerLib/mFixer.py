import argparse
from ..parLib import mpiHelper


parser = argparse.ArgumentParser(description='mFixer')
parser.add_argument('folderName')
parser.add_argument('mummerLink')
parser.add_argument('-par', '--parallel', help= 'Fast aligns contigs (input is maximum number of threads)', required=False)
parser.add_argument('-t', '--LCReads', help= 'Type of reads aligned to the contigs formed by long reads', required=False)
parser.add_argument('-op', '--option', help= 'Parameters to pass in', required=False)
parser.add_argument('-cl', '--cleanInput', help= 'Parameters to clean inputs', required=False)

parser.add_argument('-l', '--large', help= 'Large number of contigs/large size of contigs (input is True)', required=False)
parser.add_argument('-mpi', '--runmpi', help= 'whether to run MPI', required=False)
parser.add_argument('-sc', '--segmentcount', help= 'number of segments to break', required=False)

args = vars(parser.parse_args())

mpiHelper.runJob(args, "mfixer")




