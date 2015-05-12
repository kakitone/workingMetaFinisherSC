1) Run MFixer with options 

python -m srcRefactor.misassemblyFixerLib.mFixer \
-t LR  -par 20  \
-op "toRunAdaptor=True" \
May11TestA/ /usr/bin/


2) Run ASplitter with options

nohup python -m srcRefactor.repeatPhaserLib.aSplitter \
-par 20 -rp mFixed.fasta -ar True -rs 0 -rd True \
-op  "BRThres=2 RThres=5" \
-pk map \
May11TestA/ /usr/bin/ &



3) Run Evaluator to print headers or do evalulation 

python -m srcRefactor.evaluator --option header \
--quastPath /data/kakitone/download2/quast-2.3/quast.py \
--folderName /data/kakitone/May07-2015/workingMetaFinisherSC/May11TestA/ \
--paraFileName option.json \
--outputFilename /data/kakitone/May07-2015/workingMetaFinisherSC/results.csv 


python -m srcRefactor.evaluator --option evaluate \
--quastPath /data/kakitone/download2/quast-2.3/quast.py \
--folderName /data/kakitone/May07-2015/workingMetaFinisherSC/May11TestA/ \
--paraFileName option.json \
--outputFilename /data/kakitone/May07-2015/workingMetaFinisherSC/results.csv 
