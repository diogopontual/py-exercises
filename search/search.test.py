import unittest
import binarysearch as binarysearch

class TestSearch(unittest.TestCase):
    def runTest(self):
        names = ['augusto', 'barbara', 'carla', 'carlos', 'cristiano', 'daniel', 'danilo', 'davi', 'diogo', 'douglas', 'eduardo', 'fabricio', 'gustavo', 'paula', 'rafael', 'ronaldo', 'ziraldo']
        self.assertEquals(binarysearch.search(names,'diogo'),8)
        self.assertEquals(binarysearch.search(names,'dioga'),None)

unittest.main()
