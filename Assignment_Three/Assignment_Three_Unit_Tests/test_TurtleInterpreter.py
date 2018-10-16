import unittest
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
        self.test_ti = TurtleInterpreterClass.TurtleInterpreter()
        self.test_ti.string_to_class_interpreter(['repeat', '4'])
        self.assertIsInstance(self.test_ti.repeat_class.class_object, TurtleInterpreterClass.Repeat)
        self.assertEqual(self.test_ti.repeat_class.class_object.number_of_repeats, 4)
        self.test_ti.string_to_class_interpreter(['Move', '10'], self.test_turtle)
        self.test_ti.string_to_class_interpreter(['move', '10'], self.test_turtle)
        self.test_ti.string_to_class_interpreter(['PenDown'], self.test_turtle)
        end_class = self.test_ti.string_to_class_interpreter(['end'], self.test_turtle)
        self.assertIsInstance(end_class[0].class_object, TurtleInterpreterClass.End)
        end_class[0].interpret_expression()
        self.assertEqual(self.test_turtle.location(), [80,0])
        self.assertEqual(self.test_turtle.is_pen_up(), False)

    def test_get_variable(self):
        """
        This unit test is testing the 'GetVariable' subclass of the 'Turtle Interpreter'
        class.  It passes when the 'GetVariable' class is successfully instantiated upon
        via a key and the dictionary.  The definition 'interpretation_of_expression'
        also has to be executed successfully by getting the 'value' from the key.
        :return:
        """
        test_dictionary = {'#key':'value'}
        get_variable_class = TurtleInterpreterClass.GetVariable(['#key',test_dictionary])
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
        pen_down_class.interpretation_of_expression()
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
        pen_up_class.interpretation_of_expression()
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

    def test_repeat_command_identifier(self):
        """
        This unit test is testing the 'repeat_command_identifier' definition of the
        'Turtle Interpreter' class.  It passes when the 'Repeat' class is successfully
        instantiated into the 'repeat_command' variable of the 'Turtle Interpreter' class
        after reading in the string list command with 'repeat' in it as well as a certain
        number of 'iterations'.
        :return:
        """
        self.test_ti = TurtleInterpreterClass.TurtleInterpreter()
        self.test_ti.end_and_repeat_command_identifier(['repeat', '10'])
        self.assertIsInstance(self.test_ti.repeat_class.class_object, TurtleInterpreterClass.Repeat)
        self.assertEqual(self.test_ti.repeat_class.class_object.number_of_repeats, 10)

    def test_set_variable(self):
        """
        This unit test is testing the 'SetVariable' subclass of the 'Turtle Interpreter'
        class.  It passes when the 'SetVariable' class is successfully instantiated upon
        via a key and the dictionary.  The definition 'interpretation_of_expression'
        also has to be executed successfully by setting the incoming 'value' to the key.
        :return:
        """
        test_dictionary = {}
        set_variable_class = TurtleInterpreterClass.SetVariable(['#key', test_dictionary])
        self.assertIsInstance(set_variable_class, TurtleInterpreterClass.SetVariable)
        set_variable_class.interpretation_of_expression('value')
        self.assertEqual(test_dictionary['#key'], 'value')

    def test_string_to_class_interpreter(self):
        """
        This unit test is testing the 'string_to_class_interpreter' def of the
        'Turtle Interpreter' class.  It passes when the 'string_to_class_interpreter'
        def successfully returns the correct 'Turtle Interpreter' subclass based on the
        string that it is passed and the grammar of which it was created upon i.e. handling
        cases that involve 'repeat', 'end' and variable commands.
        :return:
        """
        self.test_ti = TurtleInterpreterClass.TurtleInterpreter()

        set_variable_class = self.test_ti.string_to_class_loader(['#key', '10'])
        set_variable_class[0].interpret_expression(set_variable_class[1].interpret_expression())
        move_class = self.test_ti.string_to_class_interpreter(['move', '#key'], self.test_turtle)
        move_class[0].interpret_expression(move_class[1].interpret_expression())
        turn_class = self.test_ti.string_to_class_interpreter(['turn', '90'], self.test_turtle)
        turn_class[0].interpret_expression(turn_class[1].interpret_expression())
        move_class = self.test_ti.string_to_class_interpreter(['move', '20'], self.test_turtle)
        move_class[0].interpret_expression(move_class[1].interpret_expression())
        turn_class = self.test_ti.string_to_class_interpreter(['turn', '-60'], self.test_turtle)
        turn_class[0].interpret_expression(turn_class[1].interpret_expression())
        move_class = self.test_ti.string_to_class_interpreter(['move', '15'], self.test_turtle)
        move_class[0].interpret_expression(move_class[1].interpret_expression())
        self.assertEqual(self.test_turtle.location(), [22.99,27.5])
        turn_class = self.test_ti.string_to_class_interpreter(['turn', '-30'], self.test_turtle)
        turn_class[0].interpret_expression(turn_class[1].interpret_expression())
        self.test_ti.string_to_class_interpreter(['repeat', '4'])
        self.assertIsInstance(self.test_ti.repeat_class.class_object, TurtleInterpreterClass.Repeat)
        self.assertEqual(self.test_ti.repeat_class.class_object.number_of_repeats, 4)
        self.test_ti.string_to_class_interpreter(['Move', '#key'], self.test_turtle)
        self.test_ti.string_to_class_interpreter(['move', '10'], self.test_turtle)
        self.test_ti.string_to_class_interpreter(['PenDown'], self.test_turtle)
        end_class = self.test_ti.string_to_class_interpreter(['end'], self.test_turtle)
        self.assertIsInstance(end_class[0].class_object, TurtleInterpreterClass.End)
        end_class[0].interpret_expression()
        self.assertEqual(self.test_turtle.location(), [102.99,27.5])
        move_class = self.test_ti.string_to_class_interpreter(['move', '10'], self.test_turtle)
        move_class[0].interpret_expression(move_class[1].interpret_expression())
        move_class = self.test_ti.string_to_class_interpreter(['move', '#key'], self.test_turtle)
        move_class[0].interpret_expression(move_class[1].interpret_expression())
        self.assertEqual(self.test_turtle.location(), [122.99,27.5])
        self.assertEqual(self.test_turtle.is_pen_up(), False)


    def test_string_to_class_loader(self):
        """
        This unit test is testing the 'string_to_class_loader' def of the
        'Turtle Interpreter' class.  It passes when the 'string_to_class_loader'
        def successfully returns the correct 'Turtle Interpreter' subclass based on the
        string that it is passed.
        :return:
        """
        self.test_ti = TurtleInterpreterClass.TurtleInterpreter()
        move_class = self.test_ti.string_to_class_loader(['Move', '10'], self.test_turtle)
        self.assertIsInstance(move_class[0].class_object, TurtleInterpreterClass.Move)
        self.assertIsInstance(move_class[1].class_object, TurtleInterpreterClass.Numerical)
        move_class[0].interpret_expression(move_class[1].interpret_expression())

        self.assertEqual(self.test_turtle.location(), [10, 0])
        pen_down_class = self.test_ti.string_to_class_loader(['PenDown'], self.test_turtle)
        self.assertIsInstance(pen_down_class[0].class_object, TurtleInterpreterClass.PenDown)
        pen_down_class[0].interpret_expression()
        self.assertEqual(self.test_turtle.is_pen_up(), False)
        self.assertEqual(self.test_turtle.pen_up_state, False)
        self.assertEqual(self.test_turtle.pen_down_state, True)

        set_variable_class = self.test_ti.string_to_class_loader(['#key', '10'])
        self.assertIsInstance(set_variable_class[0].class_object, TurtleInterpreterClass.SetVariable)
        self.assertIsInstance(set_variable_class[1].class_object, TurtleInterpreterClass.Numerical)
        set_variable_class[0].interpret_expression(set_variable_class[1].interpret_expression())
        self.assertEqual(self.test_ti.variable_dictionary['#key'], '10')

        set_variable_class = self.test_ti.string_to_class_loader(['#kei', '100'])
        self.assertIsInstance(set_variable_class[0].class_object, TurtleInterpreterClass.SetVariable)
        self.assertIsInstance(set_variable_class[1].class_object, TurtleInterpreterClass.Numerical)
        set_variable_class[0].interpret_expression(set_variable_class[1].interpret_expression())
        self.assertEqual(self.test_ti.variable_dictionary['#kei'], '100')

        move_class = self.test_ti.string_to_class_loader(['Move', '#key'], self.test_turtle)
        self.assertIsInstance(move_class[0].class_object, TurtleInterpreterClass.Move)
        self.assertIsInstance(move_class[1].class_object, TurtleInterpreterClass.GetVariable)
        move_class[0].interpret_expression(move_class[1].interpret_expression())
        self.assertEqual(self.test_turtle.location(), [20, 0])

        move_class = self.test_ti.string_to_class_loader(['Turn', '#kei'], self.test_turtle)
        self.assertIsInstance(move_class[0].class_object, TurtleInterpreterClass.Turn)
        self.assertIsInstance(move_class[1].class_object, TurtleInterpreterClass.GetVariable)
        move_class[0].interpret_expression(move_class[1].interpret_expression())
        self.assertEqual(self.test_turtle.degrees, 100)

        with self.assertRaises(AttributeError):
            TurtleInterpreterClass.string_to_class_turtle_interpreter(self.test_turtle, 'MMove')

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


