#Ryan Ragasa
#Red ID: 817560426
# Assignment #4

import unittest
testLoader = unittest.TestLoader()
testDir = '/Users/RJ/PycharmProjects/AdvancedObjectOrientedProgramming/Assignment_Four/Assignment_Four_Unit_Tests'
suite = testLoader.discover(testDir)
mainRun = unittest.TextTestRunner()
mainRun.run(suite)