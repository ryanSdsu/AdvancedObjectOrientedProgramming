from Assignment_Three.AbstractInterpreterClass import AbstractInterpreter
from Assignment_Three import TurtleClass


# class End(AbstractInterpreterClass.AbstractInterpreter):
#     def __init__(self, repeat_class):
#         self.repeat_class = repeat_class
#
#     def interpretation_of_expression(self, value):
#         for iterator in range(0, self.repeat_class.number_of_repeats):
#             for item in self.repeat_class.repeat_commands:
#                 item.interpretation_of_expression(value)

class GetVariable(AbstractInterpreter):
    """
    This is the subclass for the Turtle Interpreter Class in which the
    'GetVariable' definition is called upon.
    """
    def __init__(self, variable_key, variable_dictionary):
        """
        This is the constructor for the 'Variable' class and is expected to take in
        two variables 'variable_key' and 'variable_dictionary'.  The 'variable_key'
        is the key which will be referenced in the 'variable_dictionary' once it is interpreted
        upon.
        :param variable_key: the key of which the interpretation will be acted upon
        :param variable_dictionary: the dictionary of which the interpretation will be acted upon
        """
        self.variable_key = variable_key
        self.variable_dictionary = variable_dictionary

    def interpretation_of_expression(self):
        """
        This is where we get the 'value' of the 'variable_key' via the 'variable_dictionary'.
        :return:
        """
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
    This is the subclass for the Turtle Interpreter Class in which the turtles
    'NumericalExpression' definition is called upon.
    """
    def __init__(self, number):
        """
        This is the constructor for the 'NumericalExpression' class and is expected to take in
        a number.
        :param number: the number that will be interpreted
        """
        self.number = number

    def interpretation_of_expression(self):
        """
        This is where we return the number that was given by the 'NumericalExpression' class.
        :return:
        """
        return self.number


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

    def interpretation_of_expression(self, value):
        """
        This is where the 'PenDown' def of the turtle object will be activated and interpreted
        once called.
        :param value: None
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

    def interpretation_of_expression(self, value):
        """
        This is where the 'PenUp' def of the turtle object will be activated and interpreted
        once called.
        :param value: None
        :return:
        """
        self.expression.pen_up()

#
# class Repeat(AbstractInterpreterClass.AbstractInterpreter):
#     def __init__(self, number_of_repeats):
#         self.repeat_commands = []
#         self.number_of_repeats = number_of_repeats
#
#     def interpretation_of_expression(self, value):
#         self.repeat_commands.append(value)
#

class SetVariable(AbstractInterpreter):
    """
    This is the subclass for the Turtle Interpreter Class in which the
    'SetVariable' definition is called upon.
    """
    def __init__(self, variable_key, variable_dictionary):
        """
        This is the constructor for the 'Variable' class and is expected to take in
        two variables 'variable_key' and 'variable_dictionary'.  The 'variable_key'
        is the key which will be added to the 'variable_dictionary' once it is interpreted
        upon.
        :param variable_key: the key of which the interpretation will be acted upon
        :param variable_dictionary: the dictionary of which the interpretation will be acted upon
        """
        self.variable_key = variable_key
        self.variable_dictionary = variable_dictionary

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



contextualness = dict()
""" Anything with a # in front is a variable and needs to be added to the context"""
contextualness.update({'#side': 10})
list_of_operations = []
turtle_murtle = TurtleClass.Turtle()
stuff = "hi"
# test_command = Move(turtle_murtle)
# test_interpret = test_command.interpretation_of_expression(10)


# list_of_operations.append(Turn(NumericalExpression(180), turtle_murtle))
# list_of_operations.append(TurnExpression(KeyVariableExpression('#side'), turtle_murtle))
# list_of_operations.append(Move(NumericalExpression(20), turtle_murtle))
# list_of_operations.append(MoveExpression(NumberExpression(20), turtle_murtle))
# list_of_operations.append(TurnExpression(KeyVariableExpression('#side'), turtle_murtle))
# list_of_operations.append(MoveExpression(NumberExpression(15), turtle_murtle))
# for i in list_of_operations:
#     i.interpret(contextualness)
# print(turtle_murtle.location())
#
# repeat_expression = RepeatExpression(4)
# repeat_expression.add_statement(MoveExpression(KeyVariableExpression('#side'), turtle_murtle))
# list_of_operations.append(repeat_expression)
# for i in list_of_operations:
#     i.interpretation_of_expression(contextualness)

"""
#side = 15
move 10
turn 90
move 20
turn -60
move 15
"""

#This is for the unit test
# from pydoc import locate
# klass = locate('Assignment_Three.TurtleClass')

