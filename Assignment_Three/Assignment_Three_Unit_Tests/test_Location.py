import unittest
from Assignment_Three import TurtleClass
from Assignment_Three import LocationClass

class TestLocationClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Location Class"""

    def setUp(self):
        """
        This is the set up for the 'Location' class. We are creating the 'Turtle' objects to be
        set, added and tested later.
        :return:
        """
        self.turtle = TurtleClass.Turtle()

    def test_init_def(self):
        """
        This unit test is testing the __init__ def of the 'Location' class.  It passes when a
        'Location' class is successfully created along with it's variable via 'input' containing
        the functionality of the new strategy it was given upon.
        :return:
        """
        test_location_class = LocationClass.Location(self)
        self.assertIsInstance(test_location_class, LocationClass.Location)

    def test_location_custom_turtle_no_graphics(self):
        """
        This unit test is testing the 'custom_turtle_no_graphics' strategy of the 'Location' class.
        It passes when the strategy 'custom_turtle_no_graphics' is set via the 'Location' class
        and when a turtle object is given a set of move instructions, the correct calculations
        for the location should occur.
        :return:
        """
        self.turtle.location_of_turtle = [10,20]
        self.turtle.degrees = 30
        self.turtle.move(15)
        self.assertListEqual(self.turtle.location_of_turtle, [22.99,27.5])

    def test_location_strategy_custom_turtle_no_graphics(self):
        """
        This unit test is testing the 'custom_turtle_no_graphics' strategy of the 'LocationStrategy'
        class. It passes when the strategy 'custom_turtle_no_graphics' is set via the 'LocationStrategy'
        class to the corresponding variable.
        :return:
        """
        test_location_class = LocationClass.LocationStrategy.custom_turtle_no_graphics(self.turtle)
        self.assertEquals(type(test_location_class.input(self.turtle)),
                          type(LocationClass.Location.custom_turtle_no_graphics(self.turtle)))

if __name__ == '__main__':
    unittest.main()


