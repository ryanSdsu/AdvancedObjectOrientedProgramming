from Assignment_Three.AbstractClassLoaderClass import AbstractClassLoader

class ExpressionLoader(AbstractClassLoader):
    """
    This is the base class for the expression loader. It allows one to load expressions
    from different interpreters, specifically in this case the subclasses of the Turtle
    Interpreter class. The translation from string to Turtle Interpreter also happens
    here in the 'string_to_class_turtle_interpreter' definition.
    """
    def __init__(self, module_name, file_name, class_name, expression):
        """
        This builds off of the class loader class and allows one to further load expressions
        from the interpreter.
        :param module_name: the name of the module to be loaded
        :param file_name: the file to be loaded
        :param class_name: the class name to be loaded
        :param expression: the expression for which to be loaded
        """
        super().__init__(module_name, file_name, class_name)
        self.class_object = self.class_object(expression)

    def interpret_expression(self, *value):
        """
        This executes the interpretation of the expression that was was loaded.
        :param value: the value of that which will be passed into the interpretation
        :return:
        """
        if len(value) == 1:
            return self.class_object.interpretation_of_expression(value[0])
        else:
            return self.class_object.interpretation_of_expression()