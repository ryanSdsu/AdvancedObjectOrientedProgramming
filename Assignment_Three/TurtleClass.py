from Assignment_Three import LocationClass

class Turtle:
    """This is the base class for the Turtle object."""

    def __init__(self):
        """
        This is the constructor of 'Turtle' class.  It sets all the default values to 0 and
        the pen_up_state to be true.  Also the current strategy for which to calculate the
        location is set to be 'custom_turtle_no_graphics'.
        """
        self.location_of_turtle = [0, 0]
        self.degrees = 0
        self.distance = 0
        self.pen_up_state = True
        self.pen_down_state = False
        self.__location_strategy = LocationClass.LocationStrategy.custom_turtle_no_graphics(self)

    def move(self, distance):
        """
        This is where the calculations for the distance is measured.  It is performed based on the
        location strategy which was selected in the init def.
        :param distance: how far the turtle object will travel
        :return:
        """
        self.distance = distance
        self.location_of_turtle = self.__location_strategy.input(self)

    def turn(self, degrees):
        """
        This is where the calculations for the degrees are measured.  It has a cap of 360 degrees
        and must be able to take in both positive and negative degrees.  The turning has to resemble
        a circle so an input of 90 as well as -270 should give the same result i.e. 90 degrees.
        :param degrees: the amound of degrees that the turtle will turn
        :return:
        """
        if degrees > 0:
            self.degrees = self.degrees + degrees
        else:
            self.degrees = self.degrees + degrees + 360
        while self.degrees < 0:
            self.degrees = self.degrees + 360
        while self.degrees >= 360:
            self.degrees = self.degrees - 360

    def pen_up(self):
        """
        This is where the pen is moved up from the screen and will no longer continue drawing.
        :return:
        """
        self.pen_up_state = True
        self.pen_down_state = False

    def pen_down(self):
        """
        This is where the pen is moved down from the screen and will continue drawing.
        :return:
        """
        self.pen_up_state = False
        self.pen_down_state = True

    def is_pen_up(self):
        """
        This is where the current state of the pen being up will be shown.
        :return:
        """
        if self.pen_up_state == True and self.pen_down_state == False:
            return True
        elif self.pen_up_state == False and self.pen_down_state == True:
            return False

    def direction(self):
        """
        This is where we return what direction the turtle object is currently facing.
        :return:
        """
        return self.degrees

    def location(self):
        """
        This is where we return the current location of the turtle.
        :return:
        """
        return self.location_of_turtle

