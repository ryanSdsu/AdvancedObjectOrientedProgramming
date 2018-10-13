import unittest
from Assignment_Three import ExpressionLoaderClass
from Assignment_Three import TurtleInterpreterClass
from Assignment_Three import TurtleClass


class TestExpressionLoaderClass(unittest.TestCase):
    """This is the base class for unit test involving the Expression Loader Class"""

    def setUp(self):
        """
        This is the set up for the Expression Loader class. It will contain a turtle object
        from the 'TurtleClass' which will be loaded into the expression loader.
        :return:
        """
        self.test_turtle = TurtleClass.Turtle()

    def test_init_def(self):
        """
        This unit test is testing the '__init__' def of the 'ExpressionLoader' class.
        It passes when a 'ExpressionLoader' class is successfully created along with its 'class'
        type then being instantiated as well.
        :return:
        """
        self.test_class = ExpressionLoaderClass.ExpressionLoader("Assignment_Three",
                                                                 "TurtleInterpreterClass",
                                                                 "Move", self.test_turtle)
        self.test_class = self.test_class.get_class()
        self.assertIsInstance(self.test_class, TurtleInterpreterClass.Move)

    def test_interpret_expression(self):
        """
        This unit test is testing the 'interpret_expression' definition of the 'ExpressionLoader' class.
        It passes when the correct ouput is produced via the corresponding expression that
        was initialized and then executed upon.
        :return:
        """
        self.test_class = ExpressionLoaderClass.ExpressionLoader("Assignment_Three",
                                                                 "TurtleInterpreterClass",
                                                                 "Move", self.test_turtle)
        self.test_class.interpret_expression(33)
        self.assertListEqual(self.test_turtle.location(), [33,0])


if __name__ == '__main__':
    unittest.main()