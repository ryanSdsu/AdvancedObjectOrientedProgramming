from Assignment_Three.VisitorClass import Visitor
from multipledispatch import dispatch
from Assignment_Three import TurtleInterpreterClass
from Assignment_Three.CaretakerClass import Caretaker
from Assignment_Three.MementoClass import Memento


class MementoVisitor(Visitor.TurtleVisitor):
    """
    This is the base class for the Memento Visitor. It saves the state of the turtle
    after each time that it changes.
    """
    def __init__(self):
        """
        This is the constructor for the 'Memento Visitor' class. It instantiates a variable
        called "turtle_memento_caretaker" in which all of the turtles states will be
        collected and stored.
        """
        self.turtle_memento_caretaker = Caretaker()

    @dispatch(TurtleInterpreterClass.End)
    def visit(self, object):
        """
        This is the visit def of the visitor if it classifies the object to be a type 'End'
        from the Turtle Interpreter.
        :param object: the object in which the visitor will be interacting with.
        :return:
        """
        self.turtle_memento = Memento.TurtleMemento(object.expression)
        self.turtle_memento_caretaker.add_memento(self.turtle_memento)
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
        self.turtle_memento = Memento.TurtleMemento(object.expression)
        self.turtle_memento_caretaker.add_memento(self.turtle_memento)
        pass

    @dispatch(TurtleInterpreterClass.PenDown)
    def visit(self, object):
        """
        This is the visit def of the visitor if it classifies the object to be a type 'PenDown'
        from the Turtle Interpreter.
        :param object: the object in which the visitor will be interacting with.
        :return:
        """
        self.turtle_memento = Memento.TurtleMemento(object.expression)
        self.turtle_memento_caretaker.add_memento(self.turtle_memento)
        pass

    @dispatch(TurtleInterpreterClass.PenUp)
    def visit(self, object):
        """
        This is the visit def of the visitor if it classifies the object to be a type 'PenUp'
        from the Turtle Interpreter.
        :param object: the object in which the visitor will be interacting with.
        :return:
        """
        self.turtle_memento = Memento.TurtleMemento(object.expression)
        self.turtle_memento_caretaker.add_memento(self.turtle_memento)
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
        self.turtle_memento = Memento.TurtleMemento(object.expression)
        self.turtle_memento_caretaker.add_memento(self.turtle_memento)
        pass
