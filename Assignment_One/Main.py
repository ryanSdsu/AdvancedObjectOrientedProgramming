#Ryan Ragasa
#Red ID: 817560426
#I am currently enrolled in this class => CS 635 Advanced Object-Oriented Design & Programming.

import unittest
loader = unittest.TestLoader()
start_dir = '/Users/RJ/PycharmProjects/AdvancedObjectOrientedProgramming/Assignment_One/Assignment_One_Unit_Tests'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)