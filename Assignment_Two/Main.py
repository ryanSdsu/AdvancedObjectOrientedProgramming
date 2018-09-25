# Ryan Ragasa
# Red ID: 817560426
# Assignment #2

# Q1)
# My unit tests that I did for assignment #1 I personally felt were “Ok” however they were
# lacking in terms of their handling for generic types. Because of this I had to write a bunch of
# new unit tests in order to make sure that some of the hypothetical cases were taken care of.
# This had caused me to go back to the very beginning and start with a simple “Node” class.
# It was with this simple class that I had built my new priority queue upon and had used for
# initial testing. From there I began to focus on the student class where in the end I ended
# up reusing quite a bit of the old unit tests but not as many as I thought I would do.
# In fact, after refactoring, most of the tests that I had to write/create were new as my
# priority queue had to be able to handle a more wider array of data types.

import unittest
testLoader = unittest.TestLoader()
testDir = '/Users/RJ/PycharmProjects/AdvancedObjectOrientedProgramming/Assignment_Two/Assignment_Two_Unit_Tests'
suite = testLoader.discover(testDir)
mainRun = unittest.TextTestRunner()
mainRun.run(suite)