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
        coordinates [0,0] being set and the pen is up.
        :return:
        """
        self.assertIsInstance(self.turtle, TurtleClass.Turtle)
        self.assertListEqual(self.turtle.location(), [0, 0])
        self.assertEquals(self.turtle.is_pen_up(), True)
        self.assertEquals(self.turtle.pen_down_state, False)

    def test_move(self):
        """
        This unit test is testing the move definition of the 'Turtle' object. It passes when after
        receiving a certain amount of units to move, it's location gets updated based on where its
        X/Y coordinates were previously as well as what the current 'degrees' was set to.
        The actual mathematical calculations are contained within the 'custom_turtle_no_graphics'
        strategy in the '__location_strategy' variable.
        :return:
        """
        self.turtle.location_of_turtle = [10,20]
        self.turtle.degrees = 30
        self.turtle.move(15)
        self.assertListEqual(self.turtle.location_of_turtle, [22.99,27.5])

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

    def test_turn(self):
        """
        This unit test is testing the turn def of the 'Turtle' class. It passes when the
        definition receives a certain amount of degrees and turns based on its given input.
        The turning has to resemble a circle so an input of 90 as well as -270 should
        give the same result i.e. 90 degrees.
        :return:
        """
        self.turtle.turn(90)
        self.assertEquals(self.turtle.degrees, 90)
        self.turtle.turn(-90)
        self.assertEquals(self.turtle.degrees, 0)
        self.turtle.turn(-270)
        self.assertEquals(self.turtle.degrees, 90)
        self.turtle.turn(-45)
        self.assertEquals(self.turtle.degrees, 45)
        self.turtle.turn(315)
        self.assertEquals(self.turtle.degrees, 0)

if __name__ == '__main__':
    unittest.main()