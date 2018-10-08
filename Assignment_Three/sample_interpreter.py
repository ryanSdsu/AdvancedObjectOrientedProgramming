import abc
from Assignment_Three import TurtleClass


class AbstractExpression(metaclass=abc.ABCMeta):
    """
    Declare an abstract Interpret operation that is common to all nodes
    in the abstract syntax tree.
    """
    def __init__(self, turtle_class):
        self.turtle = turtle_class

    @abc.abstractmethod
    def interpret(self, context):
        pass


class NumberExpression(AbstractExpression):
    def __init__(self, number):
        self.num = number

    def interpret(self, context):
        return self.num


class VariableExpression(AbstractExpression):
    def __init__(self, name):
        self.name = name

    def interpret(self, context):
        return context.get(self.name)


class MoveExpression(AbstractExpression):
    def __init__(self, expression, turtle_class):
        self.expression = expression
        self.turtle = turtle_class

    def interpret(self, context):
        self.turtle.move(self.expression.interpret(context))


class TurnExpression(AbstractExpression):
    def __init__(self, expression, turtle_class):
        self.expression = expression
        self.turtle = turtle_class

    def interpret(self, context):
        self.turtle.turn(self.expression.interpret(context))


class PenUpExpression(AbstractExpression):
    def __init__(self, turtle_class):
        self.turtle = turtle_class

    def interpret(self, context):
        self.turtle.pen_up()


class PenDownExpression(AbstractExpression):
    def __init__(self, turtle_class):
        self.turtle = turtle_class

    def interpret(self, context):
        self.turtle.pen_down()


class RepeatExpression(AbstractExpression):
    def __init__(self, k):
        self.repeat_me = []
        self.number_of_repeats = k

    def add_statement(self, statement):
        self.repeat_me.append(statement)

    def interpret(self, context):
        for iterator in range(0, self.number_of_repeats):
            for item in self.repeat_me:
                item.interpret(context)


contextualness = dict()
""" Anything with a # in front is a variable and needs to be added to the context"""
contextualness.update({'#side': 90})
list_of_operations = []
turtle_murtle = TurtleClass.Turtle()
# list_of_operations.append(MoveExpression(NumberExpression(10), turtle_murtle))
# list_of_operations.append(TurnExpression(NumberExpression(90), turtle_murtle))
# list_of_operations.append(MoveExpression(NumberExpression(20), turtle_murtle))
# list_of_operations.append(TurnExpression(VariableExpression('#side'), turtle_murtle))
# list_of_operations.append(MoveExpression(NumberExpression(15), turtle_murtle))
repeat_expression = RepeatExpression(5)
repeat_expression.add_statement(MoveExpression(NumberExpression(10), turtle_murtle))
repeat_expression.add_statement(TurnExpression(VariableExpression('#side'), turtle_murtle))
list_of_operations.append(repeat_expression)
for i in list_of_operations:
    i.interpret(contextualness)
print(turtle_murtle.location_of_turtle())

"""
#side = 15
move 10
turn 90
move 20
turn -60
move 15
"""