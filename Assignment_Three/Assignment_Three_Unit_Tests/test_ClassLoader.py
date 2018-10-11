import unittest
from Assignment_Three import ClassLoaderClass
from Assignment_Three import NodeClass
from Assignment_Three import TurtleClass


class TestClassLoaderClass(unittest.TestCase):
    """This is the base class for the Class Loader Class"""

    def test_init_def(self):
        """
        This unit test is testing the __init__ def of the 'ClassLoader' class.
        It passes when a 'ClassLoader' class is successfully created along with its 'class'
        type then being instantiated as well.
        :return:
        """
        self.test_class = ClassLoaderClass.ClassLoader("Assignment_Three", "NodeClass", "Node")
        self.test_class = self.test_class.get_class()
        self.assertEquals(self.test_class, NodeClass.Node)

    def test_class_loader_abstract_interpreter(self):
        """
        This unit test is testing the 'ClassLoader' class in correlation with a turtle object and the
        'AbstractInterpreter' class. It passes when the class loader is successfully able to
        load in the 'Move' class from the 'AbstractInterpreter' and then execute the interpretation
        definition of the class on the turtle.
        :return:
        """
        turtle_new_location = [10.0, 0.0]
        self.test_turtle = TurtleClass.Turtle()
        self.test_class = ClassLoaderClass.ClassLoader("Assignment_Three",
                                                       "TurtleInterpreterClass", "Move")
        self.test_class = self.test_class.get_class()
        self.test_class = self.test_class(self.test_turtle)
        self.test_class.interpretation_of_expression(turtle_new_location[0])
        self.assertEquals(self.test_turtle.location(), turtle_new_location)

if __name__ == '__main__':
    unittest.main()


