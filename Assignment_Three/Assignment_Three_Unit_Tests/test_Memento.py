import unittest
from Assignment_Three.MementoClass import Momento
from Assignment_Three import TurtleClass

class TestMementoClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Memento Class"""

    def setUp(self):
        """
        This is the set up for the 'Memento' class. We are creating 'turtle' object(s) to be
        set, added and tested upon later.
        :return:
        """
        self.test_turtle = TurtleClass.Turtle()

    def test_constructor(self):
        """
        This unit test is testing the instantiation of the 'Memento/TurtleMemento' class.
        It passes when a 'Memento' object is instantiated as well as its sub object
        'Turtle Memento'.
        :return:
        """
        self.test_turtle_memento = Momento.TurtleMemento(self.test_turtle)
        self.assertIsInstance(self.test_turtle_memento, Momento.TurtleMemento)

    def test_get_turtle_state(self):
        """
        This unit test is testing the 'get_turtle_state' definition of the
        'TurtleMemento' subclass.  It passes when the states of a 'turtle' object
        are set to that of which is into a 'blank' turtle memento.
        :return:
        """
        self.test_blank_turtle = TurtleClass.Turtle()
        self.test_turtle_memento = Momento.TurtleMemento(self.test_blank_turtle)
        self.test_turtle.location_of_turtle = [10,100]
        self.test_turtle.pen_down()
        self.test_turtle.degrees = 40
        self.assertListEqual(self.test_turtle.location(), [10,100])
        self.assertEqual(self.test_turtle.is_pen_up(), False)
        self.assertEqual(self.test_turtle.degrees, 40)
        self.test_turtle_memento.get_turtle_state(self.test_turtle)
        self.assertListEqual(self.test_turtle.location(), [0,0])
        self.assertEqual(self.test_turtle.is_pen_up(), True)
        self.assertEqual(self.test_turtle.degrees, 0)

if __name__ == '__main__':
    unittest.main()