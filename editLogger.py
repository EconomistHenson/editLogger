import unittest, os



class editLogger():
    """
    A simple logger to summarize the updates
    """
    
    def __init__(self):
        self.nFiles = 0     #number of files underconsideration
        self.LstFils = {}   #files edited key is the inputfile item outputfile
    
    def addFile(self,thefile):
        self.LstFils[thefile] = thefile
        self.nFiles += 1
        
        return self.nFiles
        
    def addFileLst(self,newFileLst,oldExt="",newExt=""):
        """ adds simple list to dictionary
            key and item will be identical unless
            newExt should be added
            oldExt should be removed
            oldExt and newExt should contain periods
            no tupples in File list
        """
        
        # Python does not have case switch type construct
        addFileDic = {}
        newfilename = 'NA'
        
        for oldfilename in newFileLst: 
            if oldExt == "" and newExt != "":
               newfilename = oldfilename + newExt
            elif oldExt != "" and newExt == "":
               newfilename, _oldext = os.path.splitext(oldfilename) 
            elif oldExt != "" and newExt != "":
               newfilename, _oldext = os.path.splitext(oldfilename) 
               newfilename = newfilename + newExt
            else:
               pass
            self.LstFils[oldfilename] = newfilename
            self.nFiles += 1
            
        return self.nFiles
        
    def addFileTuple(self,thefile,theRes): 
        self.LstFils[thefile] = theRes
        self.nFiles += 1
        
        return self.nFiles
        
    def getFileNewLst(self):
        """ return the items in dictionary as a list"""
        return list(self.LstFils.values())
        
    def getFileOldLst(self):
        """ return the keys in a dictionary as a list"""       
        return list(self.LstFils.keys())


        
        
class TestmultReps(unittest.TestCase):

    def test_aStuff(self):
        # primary test
        test1 = editLogger()
        retval = test1.addFile("junk.txt")
        retval = test1.addFileTuple("junkkey.md","junkitem.txt")
        self.assertEqual(retval,2)
        retval = test1.addFileLst(['junk1.txt','junk2.txt'])
        self.assertEqual(retval,4)
        retval = len(test1.getFileOldLst())
        self.assertEqual(retval,4)
    
    def test_addFilelst(self):
        test2 = editLogger()
        retval2 = test2.addFileLst(['F1','F2','F3'])
        self.assertEqual(retval2,3)
        Flst3 = ['F1','F2','F3']
        Ftxt3 = ['F1.txt','F2.txt','F3.txt']
        retval2 = test2.addFileLst(Flst3)
        self.assertEqual(retval2,6)
        retval2 = test2.addFileLst(Ftxt3)
        self.assertEqual(retval2,9)      
        test3 = editLogger()
        retval3 = test3.addFileLst(Ftxt3,oldExt=".txt",newExt=".md")
        self.assertEqual(retval3,3)  
        self.assertEqual(test3.nFiles, 3)
        self.assertEqual(test3.LstFils['F3.txt'],'F3.md') 
        retlst4 = test3.getFileOldLst()
        print(retlst4[2])
        self.assertEqual(len(retlst4),3)
        self.assertEqual((retlst4[2]),'F3.txt')
        retlst5 = test3.getFileNewLst()
        self.assertEqual(len(retlst5),3)
        self.assertEqual(retlst5[2],'F3.md')       
        
if __name__ == '__main__':
    unittest.main()
    # should clean up files
    
