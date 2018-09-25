# Ryan Ragasa
# Red ID: 817560426
# Assignment #2

# Q1)
# My unit tests that I did for assignment #1 I personally felt were “Ok” however they were
# lacking in terms of their handling for 'generic' types. Because of this I had to re-write a bunch of
# new unit tests in order to make sure that different data types and classes were being taken care of.
# This had caused me to go back to the very beginning and start with a new simple “Node” class.
# It was with this very rudimentary class that I had built my new priority queue and had begun doing
# initial testing. From there I then transitioned into focusing on the "Student" class where surprisingly
# in the end I had only reused a few of the old unit tests from AS#1. In fact, after refactoring,
# most of the tests that I had written were 'new' as my new priority queue had to be able to handle a more
# wider range of data types along with different class operations and requirements.

import unittest
testLoader = unittest.TestLoader()
testDir = '/Users/RJ/PycharmProjects/AdvancedObjectOrientedProgramming/Assignment_Two/Assignment_Two_Unit_Tests'
suite = testLoader.discover(testDir)
mainRun = unittest.TextTestRunner()
mainRun.run(suite)