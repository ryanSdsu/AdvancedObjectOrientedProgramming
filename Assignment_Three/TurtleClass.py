class Turtle():

    def __init__(self):
        self._location = [0,0]
        self._degrees = 0

    def move(self, distance):
        self._distance = distance
        self._location[0] = self._location[0] + distance
        print("The distance the turtle has moved is: {}".format(distance))
        print("The location for the turtle is: {}".format(self._location))

    def turn(self, degrees):
        self._degrees = self._degrees + degrees
        if self._degrees > 360:
            self._degrees =  self._degrees - 360
        print("The turtle has turned {} degrees and is now at: {}".format(degrees, self._degrees))

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
        return self._distance

    def location(self):
        return self._location