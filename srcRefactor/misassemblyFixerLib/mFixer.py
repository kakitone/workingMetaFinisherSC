import merger 
from ..repeatPhaserLib.finisherSCCoreLib import houseKeeper

import time
import argparse

t0 = time.time()

parser = argparse.ArgumentParser(description='mFixer')
parser.add_argument('folderName')
parser.add_argument('mummerLink')
parser.add_argument('-par', '--parallel', help= 'Fast aligns contigs (input is maximum number of threads)', required=False)
parser.add_argument('-t', '--LCReads', help= 'Type of reads aligned to the contigs formed by long reads', required=False)



args = vars(parser.parse_args())


if args['parallel'] != None:
    houseKeeper.globalParallel = int(args['parallel'])
else:
    houseKeeper.globalParallel = 1


if args['LCReads'] == None:
    merger.mergerGlobalLCReads = "SR"
elif args['LCReads'] == "LR":
    merger.mergerGlobalLCReads = "LR"
elif args['LCReads'] == "SR":
    merger.mergerGlobalLCReads = "SR"


merger.mergeContigs(args['folderName'] , args['mummerLink'])
print  "Time", time.time() - t0

