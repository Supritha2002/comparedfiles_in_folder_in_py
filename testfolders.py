from compare_folder import *
import unittest
import sys
class TestFolder(unittest.TestCase):

    def test_for_missing_additional_files(self):
        missingfiles,additionalfiles=compare_folder_contents(cmdline_param1,cmdline_param2)
        self.assertEqual(len(missingfiles),0)
        self.assertTrue(len(additionalfiles)>=0)
           

if __name__ == '__main__':
    if len(sys.argv)!=3:
        sys.exit("Require 3 command line arguments")
    cmdline_param1,cmdline_param2=sys.argv[1],sys.argv[2]
    del sys.argv[1:]
    unittest.main()
