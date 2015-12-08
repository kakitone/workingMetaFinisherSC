#!/bin/sh
module load python
module load mpi4py
python-mpi -m srcRefactor.repeatPhaserLib.aSplitter  -mpi True  -sc 90 -l True -pk split   /global/project/projectdirs/m2426/folderForKaKit/aliciamock2/ /global/homes/k/kakitone/MUMmer3.23/
