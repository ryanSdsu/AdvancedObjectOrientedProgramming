from Assignment_Three import AbstractInterpreterClass
from Assignment_Three import TurtleClass


# class End(AbstractInterpreterClass.AbstractInterpreter):
#     def __init__(self, repeat_class):
#         self.repeat_class = repeat_class
#
#     def interpretation_of_expression(self, value):
#         for iterator in range(0, self.repeat_class.number_of_repeats):
#             for item in self.repeat_class.repeat_commands:
#                 item.interpretation_of_expression(value)
#
#
# class KeyVariableExpression(AbstractInterpreterClass.AbstractInterpreter):
#     def __init__(self, variable_name):
#         self.variable_name = variable_name
#
#     def interpretation_of_expression(self, value):
#         return value.get(self.variable_name)


class Move(AbstractInterpreterClass.AbstractInterpreter):
    def __init__(self, turtle_class):
        self.expression = turtle_class

    def interpretation_of_expression(self, value):
        self.expression.move(value)


# class NumericalExpression(AbstractInterpreterClass.AbstractInterpreter):
#     def __init__(self, number):
#         self.num = number
#
#     def interpretation_of_expression(self, value):
#         return self.num
#
#
class PenDown(AbstractInterpreterClass.AbstractInterpreter):
    def __init__(self, turtle_class):
        self.expression = turtle_class

    def interpretation_of_expression(self, value):
        self.expression.pen_down()
#
#
# class PenUp(AbstractInterpreterClass.AbstractInterpreter):
#     def __init__(self, turtle_class):
#         self.expression = turtle_class
#
#     def interpretation_of_expression(self, value):
#         self.expression.pen_up()
#
#
# class Repeat(AbstractInterpreterClass.AbstractInterpreter):
#     def __init__(self, number_of_repeats):
#         self.repeat_commands = []
#         self.number_of_repeats = number_of_repeats
#
#     def interpretation_of_expression(self, value):
#         self.repeat_commands.append(value)
#
#
# class Turn(AbstractInterpreterClass.AbstractInterpreter):
#     def __init__(self, expression, turtle_class):
#         self.expression = expression
#         self.turtle = turtle_class
#
#     def interpretation_of_expression(self, value):
#         self.turtle.turn(self.expression.interpretation_of_expression(value))



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

