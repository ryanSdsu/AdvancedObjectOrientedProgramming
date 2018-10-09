# Ryan Ragasa
# Red ID: 817560426
# Assignment #3

import unittest
testLoader = unittest.TestLoader()
testDir = '/Users/RJ/PycharmProjects/AdvancedObjectOrientedProgramming/Assignment_Three/Assignment_Three_Unit_Tests'
suite = testLoader.discover(testDir)
mainRun = unittest.TextTestRunner()
mainRun.run(suite)