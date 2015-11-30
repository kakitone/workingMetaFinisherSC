#!/bin/sh
module load python
module load mpi4py
python -m  srcRefactor.misassemblyFixerLib.mFixer  -mpi False  -par 20  ./ ./
