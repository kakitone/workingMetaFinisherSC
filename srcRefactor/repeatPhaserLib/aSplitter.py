import argparse
from ..parLib import mpiHelper

parser = argparse.ArgumentParser(description='aSplitter')
parser.add_argument('folderName')
parser.add_argument('mummerLink')

parser.add_argument('-f', '--fast', help= 'Fast aligns contigs (input is True)', required=False)
parser.add_argument('-par', '--parallel', help= 'Fast aligns contigs (input is maximum number of threads)', required=False)
parser.add_argument('-l', '--large', help= 'Large number of contigs/large size of contigs (input is True)', required=False)

parser.add_argument('-rp', '--replace', help= 'Input files to aSplitter(e.g. noEmbed.fasta, improved.fasta, improved2.fasta or improved3.fasta)', required=False)
parser.add_argument('-ar', '--avoidrefine', help= 'Avoid refined abundance estimation (input is True)', required=False)
parser.add_argument('-rs', '--readsearch', help= 'Number of linking reads across a gap  (input is number of such linking reads/2)', required=False)
parser.add_argument('-rd', '--RRDisable', help= 'Whether one should disable Read to Read overlap check (input is True)', required=False)
parser.add_argument('-pk', '--pickup', help= 'where to run ASplitter, map/count/split/graph', required=False)
parser.add_argument('-bg', '--basicgraph', help= 'whether to run basicGraph only in graphSurgery', required=False)
parser.add_argument('-al', '--abunreplow', help= 'lower bound on repeat inlist/outlist', required=False)


parser.add_argument('-em', '--runemalgo', help= 'whether to run EM for splitting repeats', required=False)
parser.add_argument('-mpi', '--runmpi', help= 'whether to run MPI', required=False)
parser.add_argument('-sc', '--segmentcount', help= 'number of segments to break', required=False)

parser.add_argument('-op', '--option', help='File of parameter list (input is opa=true opb=false)', required=False)

args = vars(parser.parse_args())

mpiHelper.runJob(args, "asplitter")




