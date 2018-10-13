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

    def test_end(self):
        """
        This unit test is testing the 'End' subclass of the 'Turtle Interpreter'
        class.  It passes when the 'End' class is successfully instantiated upon
        via the 'Repeat' class and the definition 'interpretation_of_expression'
        is executed successfully i.e. iterating through the other interpretations
        in the 'repeat_commands_list'.
        :return:
        """
        repeat_class = TurtleInterpreterClass.Repeat(3)
        pen_up_class = TurtleInterpreterClass.PenUp(self.test_turtle)
        move_class = TurtleInterpreterClass.Move(self.test_turtle)
        numerical_class = TurtleInterpreterClass.Numerical(10)
        pen_down_class = TurtleInterpreterClass.PenDown(self.test_turtle)
        repeat_class.interpretation_of_expression([pen_up_class])
        repeat_class.interpretation_of_expression([move_class, numerical_class])
        repeat_class.interpretation_of_expression([pen_down_class])
        end_class = TurtleInterpreterClass.End(repeat_class)
        self.assertIsInstance(end_class, TurtleInterpreterClass.End)
        end_class.interpretation_of_expression()
        self.assertEqual(self.test_turtle.location(), [30,0])
        self.assertEqual(self.test_turtle.pen_up_state, False)


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

    def test_repeat(self):
        """
        This unit test is testing the 'Repeat' subclass of the 'Turtle Interpreter'
        class.  It passes when the 'Repeat' class is successfully instantiated upon
        and the definition 'interpretation_of_expression' is executed successfully i.e.
        appending other interpretations into the 'repeat_commands_list'.
        :return:
        """
        repeat_class = TurtleInterpreterClass.Repeat(3)
        self.assertIsInstance(repeat_class, TurtleInterpreterClass.Repeat)
        pen_up_class = TurtleInterpreterClass.PenUp(self.test_turtle)
        move_class = TurtleInterpreterClass.Move(self.test_turtle)
        numerical_class = TurtleInterpreterClass.Numerical(10)
        pen_down_class = TurtleInterpreterClass.PenDown(self.test_turtle)
        repeat_class.interpretation_of_expression([pen_up_class])
        repeat_class.interpretation_of_expression([move_class, numerical_class])
        repeat_class.interpretation_of_expression([pen_down_class])
        self.assertIsInstance(repeat_class.repeat_commands[0][0], TurtleInterpreterClass.PenUp)
        self.assertIsInstance(repeat_class.repeat_commands[1][0], TurtleInterpreterClass.Move)
        self.assertIsInstance(repeat_class.repeat_commands[1][1], TurtleInterpreterClass.Numerical)
        self.assertIsInstance(repeat_class.repeat_commands[2][0], TurtleInterpreterClass.PenDown)
        self.assertEqual(repeat_class.number_of_repeats, 3)

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

    def test_string_to_class_turtle_interpreter(self):
        """
        This unit test is testing the 'string_to_class_turtle_interpreter' def of the
        'Turtle Interpreter' class.  It passes when the 'string_to_class_turtle_interpreter'
        def successfully returns the correct 'Turtle Interpreter' subclass based on the
        string that it is passed.
        :return:
        """
        move_class = TurtleInterpreterClass.string_to_class_turtle_interpreter('Move', self.test_turtle)
        self.assertIsInstance(move_class.class_object, TurtleInterpreterClass.Move)
        with self.assertRaises(AttributeError):
            TurtleInterpreterClass.string_to_class_turtle_interpreter('MMove', self.test_turtle)

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


