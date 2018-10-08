from Assignment_Three import TurtleClass
import numpy as np

class Location:
    """This is the base class for the Location Strategy."""
    def __init__(self, input):
        """
        This is the constructor of 'Location' class in which the class strategy can be set.
        :param input: the strategy of which the 'Location' class can be set to.
        """
        self.input = input


    def custom_turtle_no_graphics(turtle):
        """
        This is the location strategy used to determine the turtle coordinates with no graphics.
        It is set by converting degrees to radians, and by using delta_x and delta_y we determine
        the new x and y whereabouts.
        :param location: the location of the turtle via [x, y]
        :param degrees: the number of degrees the turtle will be heading towards
        :param distance: how far the turtle will be traveling
        :return: the new turtle location
        :rtype [x, y]
        """
        radians = turtle.degrees * np.pi / 180
        delta_x = np.cos(radians) * turtle.distance
        delta_y = np.sin(radians) * turtle.distance
        new_x = turtle.location_of_turtle[0] + delta_x
        new_y = turtle.location_of_turtle[1] + delta_y
        return [float("{0:.2f}".format(new_x)), float("{0:.2f}".format(new_y))]