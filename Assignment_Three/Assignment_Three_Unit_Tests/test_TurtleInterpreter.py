import unittest
import random
from Assignment_Three import TurtleInterpreterClass
from Assignment_Three import TurtleClass


class TestAbstractInterpreterClass(unittest.TestCase):
    """This is the base class for unit tests involving the Turtle Interpreter Class"""

    def setUp(self):
        """
        This is the set up for the 'Turtle Interpreter' class. We are creating the
        Turtle object for which we will be interpreting upon.
        :return:
        """
        self.test_turtle = TurtleClass.Turtle()

    def test_get_variable(self):
        """
        This unit test is testing the 'GetVariable' subclass of the 'Turtle Interpreter'
        class.  It passes when the 'GetVariable' class is successfully instantiated upon
        via a key and the dictionary.  The definition 'interpretation_of_expression'
        also has to be executed successfully by getting the 'value' from the key.
        :return:
        """
        test_dictionary = {'#key':'value'}
        get_variable_class = TurtleInterpreterClass.GetVariable('#key',test_dictionary)
        self.assertIsInstance(get_variable_class, TurtleInterpreterClass.GetVariable)
        set_variable_class = get_variable_class.interpretation_of_expression()
        self.assertEqual(set_variable_class, 'value')

    def test_move_class(self):
        """
        This unit test is testing the 'Move' subclass of the 'Turtle Interpreter' class.
        It passes when the 'Move' class is successfully instantiated upon via the turtle and
        the definition 'interpretation_of_expression' is executed successfully i.e. moving the
        turtle.
        :return:
        """
        move_class = TurtleInterpreterClass.Move(self.test_turtle)
        self.assertIsInstance(move_class, TurtleInterpreterClass.Move)
        move_class.interpretation_of_expression(10)
        self.assertListEqual(self.test_turtle.location(), [10,0])

    def test_numerical(self):
        """
        This unit test is testing the 'Numerical' subclass of the 'Turtle Interpreter'
        class.  It passes when the 'Numerical' class is successfully instantiated upon
        via a number and the definition 'interpretation_of_expression' is executed successfully
        i.e. returning it.
        :return:
        """
        numerical_class = TurtleInterpreterClass.Numerical(10)
        self.assertIsInstance(numerical_class, TurtleInterpreterClass.Numerical)
        numerical_expression = numerical_class.interpretation_of_expression()
        self.assertEqual(numerical_expression, 10)

    def test_pen_down(self):
        """
        This unit test is testing the 'PenDown' subclass of the 'Turtle Interpreter' class.
        It passes when the 'PenDown' class is successfully instantiated upon via the turtle and
        the definition 'interpretation_of_expression' is executed successfully i.e. moving
        the pen down.
        :return:
        """
        pen_down_class = TurtleInterpreterClass.PenDown(self.test_turtle)
        self.assertIsInstance(pen_down_class, TurtleInterpreterClass.PenDown)
        pen_down_class.interpretation_of_expression(None)
        self.assertEqual(self.test_turtle.is_pen_up(), False)
        self.assertEqual(self.test_turtle.pen_up_state, False)
        self.assertEqual(self.test_turtle.pen_down_state, True)

    def test_pen_up(self):
        """
        This unit test is testing the 'PenUp' subclass of the 'Turtle Interpreter' class.
        It passes when the 'PenUp' class is successfully instantiated upon via the turtle and
        the definition 'interpretation_of_expression' is executed successfully i.e. moving the
        pen up.
        :return:
        """
        pen_up_class = TurtleInterpreterClass.PenUp(self.test_turtle)
        self.assertIsInstance(pen_up_class, TurtleInterpreterClass.PenUp)
        pen_up_class.interpretation_of_expression(None)
        self.assertEqual(self.test_turtle.is_pen_up(), True)
        self.assertEqual(self.test_turtle.pen_up_state, True)
        self.assertEqual(self.test_turtle.pen_down_state, False)

    def test_set_variable(self):
        """
        This unit test is testing the 'SetVariable' subclass of the 'Turtle Interpreter'
        class.  It passes when the 'SetVariable' class is successfully instantiated upon
        via a key and the dictionary.  The definition 'interpretation_of_expression'
        also has to be executed successfully by setting the incoming 'value' to the key.
        :return:
        """
        test_dictionary = {}
        set_variable_class = TurtleInterpreterClass.SetVariable('#key',test_dictionary)
        self.assertIsInstance(set_variable_class, TurtleInterpreterClass.SetVariable)
        set_variable_class = set_variable_class.interpretation_of_expression('value')
        self.assertEqual(test_dictionary['#key'], 'value')

    def test_turn(self):
        """
        This unit test is testing the 'Turn' subclass of the 'Turtle Interpreter' class.
        It passes when the 'Turn' class is successfully instantiated upon via the turtle and
        the definition 'interpretation_of_expression' is executed successfully i.e. turning
        the turtle via its degrees.
        :return:
        """
        turn_class = TurtleInterpreterClass.Turn(self.test_turtle)
        self.assertIsInstance(turn_class, TurtleInterpreterClass.Turn)
        turn_class.interpretation_of_expression(90)
        self.assertEqual(self.test_turtle.degrees, 90)


if __name__ == '__main__':
    unittest.main()


