class Caretaker:
    """
    This is the base class for the Caretaker object.
    """
    def __init__(self):
        """
        This is the constructor for the Caretaker class in which we instantiate a list for
        which to store all of the mementos.
        """
        self.saved_mementos =[]

    def add_memento(self, memento):
        """
        This is where we add a memento object to the 'saved_momentos' list
        :param momento: the current memento that needs to be saved
        :return:
        """
        self.saved_mementos.append(memento)

    def get_memento(self, index):
        """
        This is where we return a memento object based on an index that is given.
        :param index: the index for which to retrieve a certain memento
        :return:
        """
        return self.saved_mementos[index]