#Ryan Ragasa
#Red ID: 817560426
#I am currently enrolled in this class => CS 635 Advanced Object-Oriented Design & Programming.

import unittest
testLoader = unittest.TestLoader()
testDir = '/Users/RJ/PycharmProjects/AdvancedObjectOrientedProgramming/Assignment_Two/Assignment_Two_Unit_Tests'
suite = testLoader.discover(testDir)
mainRun = unittest.TextTestRunner()
mainRun.run(suite)