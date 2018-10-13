from Assignment_Three.AbstractInterpreterClass import AbstractInterpreter
from Assignment_Three.ExpressionLoaderClass import ExpressionLoader

class TurtleInterpreter:
    """
    This is the base class for the 'Turtle Interpreter'. It translates string commands
    into the desired subclasses via the Turtle Language.
    """
    def __init__(self):
        """
        This is the constructor for the Turtle Interpreter. It creates a 'variable_dictionary'
        that will be referenced whenever a string being passed has a '#' in the beginning
        so that the values can be stored, referenced and changed if necessary.
        """
        self.variable_dictionary = {}

    def string_to_class_turtle_interpreter(self, expression_list, *turtle):
        """
        This reads in a list of string expressions and then selects the proper subclass from the
        'Turtle Interpreter Class' to be loaded based on that string.
        :return:
        """

        module_name = "Assignment_Three"
        turtle_interpreter = "TurtleInterpreterClass"

        if len(expression_list) == 1:
            if expression_list[0][0] == '#':
                set_variable_list = [expression_list[0], self.variable_dictionary]
                class_object = ExpressionLoader(module_name, turtle_interpreter,
                                            "GetVariable", set_variable_list)
                return [class_object]

            try:
                class_object = ExpressionLoader(module_name, turtle_interpreter,
                                                expression_list[0], turtle[0])
                return [class_object]
            except AttributeError:
                raise AttributeError("An invalid class has been selected: {}.".format(
                    expression_list[0]))

        else:
            if expression_list[0][0] == '#':
                set_variable_list = [expression_list[0], self.variable_dictionary]
                class_object_one = ExpressionLoader(module_name, turtle_interpreter,
                                                "SetVariable", set_variable_list)

                if type(expression_list[1]) is str:
                    if expression_list[1][0] == '#':
                        if expression_list[1] in self.variable_dictionary:
                            set_variable_list = [expression_list[1], self.variable_dictionary]
                            class_object_two = ExpressionLoader(module_name, turtle_interpreter,
                                                            "GetVariable", set_variable_list)
                            return [class_object_one, class_object_two]

                if type(expression_list[1]) is int or type(expression_list[1]) is float:
                    class_object_two = ExpressionLoader(module_name, turtle_interpreter,
                                                        "Numerical", expression_list[1])
                    return [class_object_one, class_object_two]

                try:
                    class_object_two = ExpressionLoader(module_name, turtle_interpreter,
                                                        expression_list[1], turtle[0])
                    return [class_object_one, class_object_two]
                except AttributeError:
                    raise AttributeError("An invalid class has been selected: {}.".format(
                        expression_list[1]))

            try:
                class_object_one = ExpressionLoader(module_name, turtle_interpreter,
                                                    expression_list[0], turtle[0])
            except AttributeError:
                raise AttributeError("An invalid class has been selected: {}.".format(
                    expression_list[0]))

            if type(expression_list[1]) is int or type(expression_list[1]) is float:
                class_object_two = ExpressionLoader(module_name, turtle_interpreter,
                                                "Numerical", expression_list[1])
                return [class_object_one, class_object_two]

            try:
                if type(expression_list[1]) is str:
                    if expression_list[1][0] == '#':
                        if expression_list[1] in self.variable_dictionary:
                            set_variable_list = [expression_list[1], self.variable_dictionary]
                            class_object_two = ExpressionLoader(module_name, turtle_interpreter,
                                                                "GetVariable", set_variable_list)
                            return [class_object_one, class_object_two]
            except AttributeError:
                raise AttributeError("The variable '{}' is not in the variable_dictionary.".format(
                    expression_list[1]))


class End(AbstractInterpreter):
    """
    This is the subclass for the Turtle Interpreter Class in which the
    'End' class is called upon.
    """
    def __init__(self, repeat_class):
        """
        This is the constructor for the 'End' class and is expected to take in
        the variable 'repeat_class' which is the the 'Repeat' subclass of the
        Turtle Interpreter.
        :param repeat_class: the Repeat subclass to be interpreted upon
        """
        self.repeat_class = repeat_class

    def interpretation_of_expression(self):
        """
        This is where we iterate through the 'Repeat' class and execute the interpretations
        of those expressions
        :return:
        """
        for iterations in range(0, self.repeat_class.number_of_repeats):
            for value, expression in enumerate(self.repeat_class.repeat_commands):
                if len(expression) == 1:
                    expression[0].interpretation_of_expression()
                else:
                    expression[0].interpretation_of_expression(
                        expression[1].interpretation_of_expression())


class GetVariable(AbstractInterpreter):
    """
    This is the subclass for the Turtle Interpreter Class in which the
    'GetVariable' class is called upon.
    """
    def __init__(self, variable_key_and_dictionary):
        """
        This is the constructor for the 'Variable' class and is expected to take in
        two variables 'variable_key' and 'variable_dictionary'.  The 'variable_key'
        is the key which will be referenced in the 'variable_dictionary' once it is interpreted
        upon.
        :param variable_key: the key of which the interpretation will be acted upon
        :param variable_dictionary: the dictionary of which the interpretation will be acted upon
        """
        self.variable_key = variable_key_and_dictionary[0]
        self.variable_dictionary = variable_key_and_dictionary[1]

    def interpretation_of_expression(self):
        """
        This is where we get the 'value' of the 'variable_key' via the 'variable_dictionary'.
        :return:
        """
        if type(self.variable_dictionary[self.variable_key]) is str:
            if self.variable_dictionary[self.variable_key][0] == '#':
                if self.variable_dictionary[self.variable_key] in self.variable_dictionary:
                    return self.interpretation_of_expression(self.variable_dictionary[self.variable_key])
        return self.variable_dictionary[self.variable_key]



class Move(AbstractInterpreter):
    """
    This is the subclass for the Turtle Interpreter Class in which the turtles
    'Move' definition is called upon.
    """
    def __init__(self, turtle_class):
        """
        This is the constructor for the 'Move' class and is expected to take in
        a turtle object.
        :param turtle_class: the turtle of which the interpretation will be acted upon
        """
        self.expression = turtle_class

    def interpretation_of_expression(self, value):
        """
        This is where the 'Move' def of the turtle object will be activated and interpreted
        once called.
        :param value: the value in which the turtle will move by.
        :return:
        """
        self.expression.move(value)


class Numerical(AbstractInterpreter):
    """
    This is the subclass for the Turtle Interpreter Class in which the
    'NumericalExpression' class is called upon.
    """
    def __init__(self, number):
        """
        This is the constructor for the 'NumericalExpression' class and is expected to take in
        a number.
        :param number: the number that will be interpreted
        """
        self.expression = number

    def interpretation_of_expression(self):
        """
        This is where we return the number that was given by the 'NumericalExpression' class.
        :return:
        """
        return self.expression


class PenDown(AbstractInterpreter):
    """
    This is the subclass for the Turtle Interpreter Class in which the turtles
    'PenDown' definition is called upon.
    """
    def __init__(self, turtle_class):
        """
        This is the constructor for the 'PenDown' class and is expected to take in
        a turtle object.
        :param turtle_class: the turtle of which the interpretation will be acted upon
        """
        self.expression = turtle_class

    def interpretation_of_expression(self):
        """
        This is where the 'PenDown' def of the turtle object will be activated and interpreted
        once called.
        :return:
        """
        self.expression.pen_down()


class PenUp(AbstractInterpreter):
    """
    This is the subclass for the Turtle Interpreter Class in which the turtles
    'PenUp' definition is called upon.
    """
    def __init__(self, turtle_class):
        """
        This is the constructor for the 'PenUp' class and is expected to take in
        a turtle object.
        :param turtle_class: the turtle of which the interpretation will be acted upon
        """
        self.expression = turtle_class

    def interpretation_of_expression(self):
        """
        This is where the 'PenUp' def of the turtle object will be activated and interpreted
        once called.
        :return:
        """
        self.expression.pen_up()


class Repeat(AbstractInterpreter):
    """
    This is the subclass for the Turtle Interpreter Class in which the
    'Repeat' class is called upon.
    """
    def __init__(self, number_of_repeats):
        """
        This is the constructor for the 'Repeat' class, it instantiates the 'repeat_commands'
        list and is expected to take in the variable 'number_of_repeats'.  The 'number_of_repeats'
        is the number of times that 'repeat_commands' list will be iterated upon.
        upon.
        :param number_of_repeats: the number of enumerations
        """
        self.repeat_commands = []
        self.number_of_repeats = number_of_repeats

    def interpretation_of_expression(self, value):
        """
        This is where we add the interpreter commands for which to be executed.
        :param value:
        :return:
        """
        self.repeat_commands.append(value)


class SetVariable(AbstractInterpreter):
    """
    This is the subclass for the Turtle Interpreter Class in which the
    'SetVariable' class is called upon.
    """
    def __init__(self, variable_key_and_dictionary):
        """
        This is the constructor for the 'Variable' class and is expected to take in
        two variables 'variable_key' and 'variable_dictionary'.  The 'variable_key'
        is the key which will be added to the 'variable_dictionary' once it is interpreted
        upon.
        :param variable_key: the key of which the interpretation will be acted upon
        :param variable_dictionary: the dictionary of which the interpretation will be acted upon
        """
        self.variable_key = variable_key_and_dictionary[0]
        self.variable_dictionary = variable_key_and_dictionary[1]

    def interpretation_of_expression(self, value):
        """
        This is where we set the 'value' to the 'variable_key' via the 'variable_dictionary'.
        :return:
        """
        new_entry = {self.variable_key:value}
        return self.variable_dictionary.update(new_entry)


class Turn(AbstractInterpreter):
    """
    This is the subclass for the Turtle Interpreter Class in which the turtles
    'Turn' definition is called upon.
    """
    def __init__(self, turtle_class):
        """
        This is the constructor for the 'Turn' class and is expected to take in
        a turtle object.
        :param turtle_class: the turtle of which the interpretation will be acted upon
        """
        self.expression = turtle_class

    def interpretation_of_expression(self, value):
        """
        This is where the 'Turn' def of the turtle object will be activated and interpreted
        once called.
        :param value: the value in which the turtle will turn by.
        :return:
        """
        self.expression.turn(value)