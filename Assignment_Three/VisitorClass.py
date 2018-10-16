from Assignment_Three import TurtleInterpreterClass
from multipledispatch import dispatch

class Visitor:
    """
    This is the base class for the Visitor pattern.
    """

    class TurtleVisitor:
        """
        This is the Turtle Visitor subclass in which the visitor object will perform certain
        actions upon visiting certain classes.
        """
        @dispatch(TurtleInterpreterClass.End)
        def visit(self, object):
            """
            This is the visit def of the visitor if it classifies the object to be a type 'End'
            from the Turtle Interpreter.
            :param object: the object in which the visitor will be interacting with.
            :return:
            """
            pass

        @dispatch(TurtleInterpreterClass.Repeat)
        def visit(self, object):
            """
            This is the visit def of the visitor if it classifies the object to be a type 'End'
            from the Turtle Interpreter.
            :param object: the object in which the visitor will be interacting with.
            :return:
            """
            pass


        @dispatch(TurtleInterpreterClass.GetVariable)
        def visit(self, object):
            """
            This is the visit def of the visitor if it classifies the object to be a type 'GetVariable'
            from the Turtle Interpreter.
            :param object: the object in which the visitor will be interacting with.
            :return:
            """
            pass

        @dispatch(TurtleInterpreterClass.Move)
        def visit(self, object):
            """
            This is the visit def of the visitor if it classifies the object to be a type 'Move'
            from the Turtle Interpreter.
            :param object: the object in which the visitor will be interacting with.
            :return:
            """
            pass

        @dispatch(TurtleInterpreterClass.PenDown)
        def visit(self, object):
            """
            This is the visit def of the visitor if it classifies the object to be a type 'PenDown'
            from the Turtle Interpreter.
            :param object: the object in which the visitor will be interacting with.
            :return:
            """
            pass

        @dispatch(TurtleInterpreterClass.PenUp)
        def visit(self, object):
            """
            This is the visit def of the visitor if it classifies the object to be a type 'PenUp'
            from the Turtle Interpreter.
            :param object: the object in which the visitor will be interacting with.
            :return:
            """
            pass

        @dispatch(TurtleInterpreterClass.Repeat)
        def visit(self, object):
            """
            This is the visit def of the visitor if it classifies the object to be a type 'Repeat'
            from the Turtle Interpreter.
            :param object: the object in which the visitor will be interacting with.
            :return:
            """
            pass


        @dispatch(TurtleInterpreterClass.SetVariable)
        def visit(self, object):
            """
            This is the visit def of the visitor if it classifies the object to be a type 'SetVariable'
            from the Turtle Interpreter.
            :param object: the object in which the visitor will be interacting with.
            :return:
            """
            pass

        @dispatch(TurtleInterpreterClass.Turn)
        def visit(self, object):
            """
            This is the visit def of the visitor if it classifies the object to be a type 'Turn'
            from the Turtle Interpreter.
            :param object: the object in which the visitor will be interacting with.
            :return:
            """
            pass

