
import unittest
import os
import merger
from ..repeatPhaserLib.finisherSCCoreLib import houseKeeper



class IsOddTests(unittest.TestCase):
    
    def setUp(self):
        print "Init : Copying files : "
        self.testingFolder = "unitTestFolder"
        self.mummerPath = "/Users/kakitlam/Desktop/experimentBench/MUMmer3.23/"
        self.listOfFiles = ["raw_reads.fasta", "contigs.fasta"]
        #os.system("rm -rf "+ self.testingFolder)
        
        
    def testLC_SR(self):
        print "Testing LC_SR "
        #self.runningLCSRTestSet("/Users/kakitlam/Desktop/metaFinisherSC/LC_SR/", 4)
    
    def testSC_LR(self):
        print "Testing SC_LR "
        self.runningSCLRTestSet("/Users/kakitlam/Desktop/metaFinisherSC/SC_LR/", 4)
        
    def testMerger(self):
        print "Testing SC_LR "
        #self.runningMergerTestSet()
    
    def runningMergerTestSet(self):
        self.listOfFiles = ["/Users/kakitlam/Desktop/metaFinisherSC/LC_SR/LC.fasta", \
                            "/Users/kakitlam/Desktop/metaFinisherSC/LC_SR/SR.fasta", \
                            "/Users/kakitlam/Desktop/metaFinisherSC/SC_LR/SC.fasta", \
                            "/Users/kakitlam/Desktop/metaFinisherSC/SC_LR/LR.fasta"]
        
        os.system("mkdir " + self.testingFolder)
        
        for eachitem in self.listOfFiles:
            os.system("cp " + eachitem + " " +self.testingFolder)
        
        os.system("python -m srcRefactor.misassemblyFixerLib.mFixer -par 4 "+ self.testingFolder + "/ "+ self.mummerPath )
        
        os.system("rm -rf "+ self.testingFolder)
    
        
    def runningLCSRTestSet(self ,myFolderName, ctexpected):
        print "Integration test on Merger:  " + myFolderName
        self.listOfFiles = ["LC.fasta", "SR.fasta"]
        self.sourceFolder = myFolderName
        
        os.system("mkdir " + self.testingFolder)
        
        for eachitem in self.listOfFiles:
            os.system("cp "+ self.sourceFolder + eachitem + " " +self.testingFolder)
        
        houseKeeper.globalParallel = 4
        merger.fixLCMisassembly(self.testingFolder+"/", self.mummerPath)
        
        os.system("rm -rf "+ self.testingFolder)
    
    def runningSCLRTestSet(self, myFolderName, ctexpected):
        print "Integration test on Merger:  " + myFolderName
        self.listOfFiles = ["SC.fasta", "LR.fasta", "LC_n.fasta"]
        self.sourceFolder = myFolderName
        
        os.system("mkdir " + self.testingFolder)
        
        for eachitem in self.listOfFiles:
            os.system("cp "+ self.sourceFolder + eachitem + " " +self.testingFolder)
        
        houseKeeper.globalParallel = 4
        merger.fixSCMisassembly(self.testingFolder+"/", self.mummerPath)
        
        #os.system("rm -rf "+ self.testingFolder)

    def tearDown(self):
        print "Teardown : Removing used files "
        
        

def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
