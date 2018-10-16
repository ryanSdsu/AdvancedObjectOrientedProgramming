import unittest
from Assignment_Three.MementoClass import Momento
from Assignment_Three.CaretakerClass import Caretaker
from Assignment_Three import TurtleClass

class TestCaretakerClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Caretaker Class"""

    def setUp(self):
        """
        This is the set up for the 'Caretaker' class. We are creating 'turtle' object(s) to be
        set, added and tested upon later. This includes also creating and instantiating a
        'test_caretaker' i.e. a 'Caretaker' object.
        :return:
        """
        self.test_caretaker = Caretaker()
        self.test_turtle = TurtleClass.Turtle()

    def test_constructor(self):
        """
        This unit test is testing the instantiation of the 'Caretaker' class.
        It passes when a 'Caretaker' object is instantiated.
        :return:
        """
        self.assertIsInstance(self.test_caretaker, Caretaker)

    def test_add_memento(self):
        """
        This unit test is testing the 'add_memento' definition of the
        'Caretaker' class.  It passes when a 'memento' object
        is successfully added to that of the Caretaker's 'saved_mementos' list.
        :return:
        """
        self.test_turtle_memento = Momento.TurtleMemento(self.test_turtle)
        self.test_caretaker.add_memento(self.test_turtle_memento)
        self.assertEqual(len(self.test_caretaker.saved_mementos), 1)

    def test_get_memento(self):
        """
        This unit test is testing the 'get_memento' definition of the
        'Caretaker' class.  It passes when a 'memento' object
        is successfully returned from the Caretaker's 'saved_mementos' list.
        :return:
        """
        self.test_turtle.location_of_turtle = [10,100]
        self.test_turtle.pen_down()
        self.test_turtle.degrees = 40
        self.test_turtle_memento = Momento.TurtleMemento(self.test_turtle)
        self.test_caretaker.add_memento(self.test_turtle_memento)
        self.test_new_turtle = TurtleClass.Turtle()
        self.test_new_momento = self.test_caretaker.get_memento(0)
        self.test_new_momento.get_turtle_state(self.test_new_turtle)
        self.assertListEqual(self.test_new_turtle.location(), [10,100])
        self.assertEqual(self.test_new_turtle.is_pen_up(), False)
        self.assertEqual(self.test_new_turtle.degrees, 40)

if __name__ == '__main__':
    unittest.main()