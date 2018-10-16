import unittest
from Assignment_Three.VisitorClass import Visitor

class TestVisitorClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Visitor Class"""

    def test_constructor(self):
        """
        This unit test is testing the instantiation of the 'Visitor' class.
        It passes when a 'Visitor' object is instantiated as well as its sub object
        'Turtle Visitor'.
        :return:
        """
        self.test_visitor = Visitor.TurtleVisitor()
        self.assertIsInstance(self.test_visitor, Visitor.TurtleVisitor)

if __name__ == '__main__':
    unittest.main()