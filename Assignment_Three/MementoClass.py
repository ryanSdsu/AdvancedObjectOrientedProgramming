class Memento:
    """
    This is the base close for the Memento object.
    """
    class TurtleMemento:
        """
        This is the Turtle Memento subclass in which turtle object states will be stored.
        """
        def __init__(self, turtle):
            """
            This is where we store the different states of the turtle.
            :param turtle: The turtle of which we will store it's different states.
            """
            self.location_state = turtle.location_of_turtle
            self.degree_state = turtle.degrees
            self.pen_up_state = turtle.pen_up_state
            self.pen_down_state = turtle.pen_down_state

        def get_turtle_state(self, turtle):
            """
            This is where we return the state of the turtle based on the momento that is given.
            :param turtle: the turtle of which we will set the momento to.
            :return:
            """
            turtle.location_of_turtle = self.location_state
            turtle.degrees = self.degree_state
            turtle.pen_up_state = self.pen_up_state
            turtle.pen_down_state = self.pen_down_state