from Assignment_Two import PriorityClass

class Node:
    """This is the base class for the Node."""
    def __init__(self, *additional_data):
        """
        This is the constructor for the Node class. If there is no argument being passed the Node class
        variable 'data' will be set to "None". If there is only one argument 'data' will be set to
        what is being passed. For multiple arguments 'data' will become a 'list' containing containing
        what is being passed. If there is a 'list', the counter for the iter definition(s) is instantiated.

        :param additional_data: additional arguments being passed into init and set to 'data'
        """
        self.node_data = None
        if len(additional_data) == 1:
            for data in additional_data:
                self.node_data = data
        elif len(additional_data) > 1:
            self.node_data = []
            self.__counter_data = 0
            for data in additional_data:
                self.node_data.append(data)

        # #Set the priority
        # self.priority_strategy = PriorityClass.Priority(PriorityClass.faculty)
        # self.priority_value = self.priority_strategy.input(self.data - 1)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter_data < len(self.node_data):
            current_data = self.node_data[self.__counter_data]
            self.__counter_data += 1
            return current_data
        else:
            raise StopIteration

    def __str__(self):
        return str(self.node_data)

# one_argument_node = Node(2)
# print(one_argument_node.priority_strategy.input)
# print(one_argument_node.priority_value)
#
# one_argument_node.priority_value = one_argument_node.priority_strategy.input(3)
# print(one_argument_node.priority_strategy.input)
# print(one_argument_node.priority_value)
#
# # one_argument_node.priority_strategy.input = PriorityClass.student
# one_argument_node.priority_strategy = PriorityClass.Priority(PriorityClass.student)
# one_argument_node.priority_value = one_argument_node.priority_strategy.input(2, 100)
# print(one_argument_node.priority_strategy.input)
# print(one_argument_node.priority_value)


# one_argument_node.priority_type.priority_strategy = PriorityClass.student
# one_argument_node.priority_type = one_argument_node.priority_type.priority_strategy(one_argument_node.data, 100)

# one_argument_node.priority_type.priority_strategy = PriorityClass.faculty
# one_argument_node.priority_type.priority_strategy()
#
# one_argument_node.priority_type.priority_strategy = PriorityClass.intern
# one_argument_node.priority_type.priority_strategy()
#
# one_argument_node.priority_type.priority_strategy = PriorityClass.retiree
# one_argument_node.priority_type.priority_strategy()