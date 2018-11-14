from Assignment_Three.VisitorClass import Visitor
from multipledispatch import dispatch
from Assignment_Three import TurtleInterpreterClass


class DistanceCollector(Visitor.TurtleVisitor):
    """
    This is the base class for the Distance Collector. It visits the abstract syntax tree
    and computes the total distance that was traveled by the 'turtle' object.
    """
    def __init__(self):
        """
        This is the constructor for the Distance Collector class. It instantiates a variable
        called "total_distance_collected" in which all of the turtle movement will be
        collected and stored.
        """
        self.total_distance_collected = 0

    @dispatch(TurtleInterpreterClass.End)
    def visit(self, object):
        """
        This is the visit def of the visitor if it classifies the object to be a type 'End'
        from the Turtle Interpreter.
        :param object: the object in which the visitor will be interacting with.
        :return:
        """
        self.total_distance_collected = self.total_distance_collected + object.distance
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
        self.total_distance_collected = self.total_distance_collected + object.distance
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
