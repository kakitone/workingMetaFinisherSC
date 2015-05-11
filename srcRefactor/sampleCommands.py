1) Run MFixer with options 

python -m srcRefactor.misassemblyFixerLib.mFixer -t LR  -par 20  Apr10Test/ /usr/bin/



adaptorSkipped part 
other parts 




2) Run ASplitter with options 

python -m srcRefactor.repeatPhaserLib.aSplitter \
-par 20 -rp LC_n.fasta -ar True -rs 0 -rd True \
-op  BRThres=2 \
Apr10TestB/ /usr/bin/ 



3) Run Evaluator to print headers or do evalulation 

python -m srcRefactor.evaluator --option header \
--quastPath /data/kakitone/download2/quast-2.3/quast.py \
--folderName /data/kakitone/May07-2015/workingMetaFinisherSC/Apr10TestB/ \
--paraFileName option.json \
--outputFilename /data/kakitone/May07-2015/workingMetaFinisherSC/results.csv 


python -m srcRefactor.evaluator --option evaluate \
--quastPath /data/kakitone/download2/quast-2.3/quast.py \
--folderName /data/kakitone/May07-2015/workingMetaFinisherSC/Apr10TestB/ \
--paraFileName option.json \
--outputFilename /data/kakitone/May07-2015/workingMetaFinisherSC/results.csv 
