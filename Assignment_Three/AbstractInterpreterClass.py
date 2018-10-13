class AbstractInterpreter():
    """
    This is the Abstract Interpreter class for which the Turtle Interpreter
    class will be inheriting from to create interpreter classes.
    """
    def __init__(self, expression):
        """
        This is the constructor for the Abstract Interpreter class. We pass in an abstract
        expression for which we will interpret in the interpret definition.
        :param expression: the expression for which to be interpreted
        """
        self.expression = expression

    def interpretation_of_expression(self, value):
        """
        This is is where we will execute an interpretation of the expression that was given
        in the init definition.
        :param value: the value of which will be passed into the interpretation
        :return:
        """
        return value