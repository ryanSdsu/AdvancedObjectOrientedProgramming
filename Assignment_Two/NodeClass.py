class Node:
    """This is the base class for the Node."""
    def __init__(self, *additional_data):
        """
        This is the constructor for the Node class. If there is no argument being passed the Node class
        variable 'data' will be set to "None". If there is only one argument 'data' will be set to
        what is being passed. For multiple arguments 'data' will become a list containing containing
        what is being passed.
        :param additional_data: additional arguments being passed into init and set to 'data'
        """
        self.data = None
        if len(additional_data) == 1:
            for data in additional_data:
                self.data = data
        elif len(additional_data) > 1:
            self.data = []
            for data in additional_data:
                self.data.append(data)

    def __str__(self):
        return str(self.data)