class AbstractInterpreter():
    """
    This is the Abstract Expression class for which all of the turtle objects
    definitions will be run via interpreter.
    """
    def __init__(self, expression):
        """
        This is the constructor for the Abstract Expression class. We pass in an abstract
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