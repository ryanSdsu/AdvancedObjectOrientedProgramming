class Node:
    """
    This is the base class for the Node. It is used as a wrapper to hold
    each individual expression and then be stored in the Abstract Syntax Tree.
    """
    def __init__(self, *additional_data):
        """
        This is the constructor for the Node class. If there is no argument being passed the Node class
        variable 'data' will be set to "None". If there is only one argument 'data' will be set to
        what is being passed. For multiple arguments 'data' will become a 'list' containing containing
        what is being passed. If there is a 'list', the counter for the iter definition(s) is instantiated.
        :param additional_data: additional arguments being passed into init and set to 'data'
        """
        self.node_data = None
        self.left_child = None
        self.right_child = None

        if len(additional_data) == 1:
            for data in additional_data:
                self.node_data = data
        elif len(additional_data) > 1:
            self.node_data = []
            self.__counter_data = 0
            self.node_data = [data for data in additional_data]

    def __iter__(self):
        """
        This is the iterator for the Node class. It simply is in reference to itself.
        :return:
        """
        return self

    def __next__(self):
        """
        This is the next definition for the Node class. It simply iterates through all of the data
        that is passed into it.
        :return:
        """
        if self.__counter_data < len(self.node_data):
            current_data = self.node_data[self.__counter_data]
            self.__counter_data += 1
            return current_data
        else:
            raise StopIteration

    def __str__(self):
        """
        This is the str definition of Node class in which we simply print the data.
        :return:
        """
        return str(self.node_data)
