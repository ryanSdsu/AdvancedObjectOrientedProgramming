from Assignment_Three import LocationClass

class Turtle:

    def __init__(self):
        self.location_of_turtle = [0, 0]
        self.degrees = 0
        self.pen_up_state = True
        self.pen_down_state = False
        self.__location_strategy = LocationClass.Location(LocationClass.Location.custom_turtle_no_graphics)

    def move(self, distance):
        self.distance = distance
        self.location_of_turtle = self.__location_strategy.input(self)

    def turn(self, degrees):
        if degrees > 0:
            self.degrees = self.degrees + degrees
        else:
            self.degrees = self.degrees + degrees + 360
        if self.degrees >= 360:
            self.degrees = self.degrees - 360

    def pen_up(self):
        self.pen_up_state = True
        self.pen_down_state = False

    def pen_down(self):
        self.pen_up_state = False
        self.pen_down_state = True

    def is_pen_up(self):
        if self.pen_up_state == True and self.pen_down_state == False:
            return True
        elif self.pen_up_state == False and self.pen_down_state == True:
            return False

    @property
    def direction(self):
        return self.distance

    def location(self):
        return self.location_of_turtle