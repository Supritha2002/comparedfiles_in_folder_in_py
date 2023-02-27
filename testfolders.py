from main import *
import unittest
class TestFolder(unittest.TestCase):

    def test_for_missing_additional_files(self):
        missingfiles,additionalfiles=comparefolder(".","standardfile.json")
        self.assertEqual(len(missingfiles),0)
        self.assertTrue(len(additionalfiles)>=0)
           

if __name__ == '__main__':
    unittest.main()
