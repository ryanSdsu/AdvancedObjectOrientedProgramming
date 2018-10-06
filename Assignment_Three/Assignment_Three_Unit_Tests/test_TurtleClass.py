import unittest
from Assignment_Three import TurtleClass

class TestStudentClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Turtle Class"""

    def setUp(self):
        self.turtle = TurtleClass.Turtle()

    def test_constructor(self):
        """
        This unit test is testing the instantiation of the 'Turtle' object based on the 'TurtleClass' via the
        default constructor.  It passes when a Turtle object is instantiated as well as the default location of
        coordinates [0,0] being set.
        :return:
        """
        self.assertIsInstance(self.turtle, TurtleClass.Turtle)
        self.assertListEqual(self.turtle.location(), [0,0])


    def test_is_pen_up(self):
        """
        This unit test is testing the is_pen_up def of the 'Turtle' class.  It passes when after
        executing the definition, if the 'pen_up_state' is set to True and the 'pen_down_state'
        is set to False, the value being returned is True.  If the 'pen_up_state' is set to False
        and the 'pen_down_state' is set to True, the value being returned is False.
        :return:
        """
        self.turtle.pen_up()
        self.assertEquals(self.turtle.is_pen_up(), True)
        self.turtle.pen_down()
        self.assertEquals(self.turtle.is_pen_up(), False)
        self.turtle.pen_up()
        self.assertEquals(self.turtle.is_pen_up(), True)
        self.turtle.pen_down()
        self.assertEquals(self.turtle.is_pen_up(), False)

    def test_pen_up(self):
        """
        This unit test is testing the pen_up def of the 'Turtle' class.  It passes when after
        executing the definition, the 'pen_up_state' is set to True while the 'pen_down_state'
        is set to False.
        :return:
        """
        self.turtle.pen_up()
        self.assertEquals(self.turtle.pen_up_state, True)
        self.assertEquals(self.turtle.pen_down_state, False)

    def test_pen_down(self):
        """
        This unit test is testing the pen_down def of the 'Turtle' class.  It passes when after
        executing the definition, the 'pen_down_state' is set to True while the 'pen_up_state'
        is set to False.
        :return:
        """
        self.turtle.pen_down()
        self.assertEquals(self.turtle.pen_down_state, True)
        self.assertEquals(self.turtle.pen_up_state, False)

if __name__ == '__main__':
    unittest.main()