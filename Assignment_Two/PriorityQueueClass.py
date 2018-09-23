from Assignment_Two import NodeClass
from Assignment_Two import PriorityClass
import copy

class PriorityQueue:
    """This is the base class for the PriorityQueue, the main structure is a max heap."""
    def __init__(self):
        """
        This is the constructor for the PriorityQueue class.
        The default Priority strategy is set to default.
        """
        self.__priority_queue = []
        self.__priority_strategy = PriorityClass.Priority(PriorityClass.default)
        self.__priority_value = None

    def add_to_priority_queue(self, data):
        """
        This is where we add a new object into the 'priority_queue'.  The main structure is a max heap therefore
        all of the objects being added must traverse to the top of the list based on the highest 'priority'. As a
        reminder the parents of each newly added object in a max heap is the "floor" of the index / 2.
        :param Node
        :return: priority_queue
        :rtype: []
        """
        self.priority_value = self.__priority_strategy.input(data)
        priority_node = [data, self.priority_value]
        self.__priority_queue.append(priority_node)
        self.max_heapify()

    def get_all_data_from_priority_queue(self):
        """
        This returns all of the data from the priority queue in a list.
        :return: data_queue
        :rtype: []
        """
        data_queue = []
        for data in self.__priority_queue:
            data_queue.append(data[0])

        return data_queue

    def get_data_from_priority_queue_index(self, priority_queue_index):
        """
        This returns the data from a certain index in the priority queue.
        :return: the data of a certain priority queue index
        :rtype: any
        """
        return self.__priority_queue[priority_queue_index][0]

    def get_priority_from_priority_queue_index(self, priority_queue_index):
        """
        This returns the priority value from a certain index in the priority queue.
        :return: the priority value of a certain priority queue index
        :rtype: float or int
        """
        return self.__priority_queue[priority_queue_index][1]

    def get_priority_queue(self):
        """
        This returns the priority queue.
        :return: priority queue
        :rtype: []
        """
        return self.__priority_queue

    def get_priority_strategy(self):
        """
        This returns the current priority strategy of the priority queue.
        :return: the current priority strategy
        :rtype: PriorityClass
        """
        return self.__priority_strategy.input

    def max_heapify(self):
        """
        This sorts the priority_node(s) in the '__priority_queue' by traversing the nodes in the list
        so that the element with the highest 'priority_value' resides at the top via the max heap.
        In terms of traversal we iterate and check to see if there is a right child of the current node
        and if there is one we see if it's priority is greater than its parents. If this is the case we swap them.
        If not we check the left child (if there is one) and do the same thing.
        :return:
        """
        try:
            number_of_nodes_in_priority_queue = len(self.__priority_queue)
            if number_of_nodes_in_priority_queue < 1:
                return
            for priority_queue_index in range(number_of_nodes_in_priority_queue, 1, -2):
                node_parent_index = (priority_queue_index - 2) // 2
                node_left_child_index = node_parent_index * 2 + 1
                node_right_child_index = node_parent_index * 2 + 2

                if(node_right_child_index <= (number_of_nodes_in_priority_queue - 1)):
                    if(self.get_priority_from_priority_queue_index(node_right_child_index) >
                           self.get_priority_from_priority_queue_index(node_parent_index)):
                        self.swap_priority_queue_index(node_right_child_index, node_parent_index)

                if(node_left_child_index <= (number_of_nodes_in_priority_queue - 1)):
                    if(self.get_priority_from_priority_queue_index(node_left_child_index) >
                           self.get_priority_from_priority_queue_index(node_parent_index)):
                        self.swap_priority_queue_index(node_left_child_index, node_parent_index)
        except TypeError:
            raise TypeError("The data being passed into the priority queue "
                            "is not aligned with a compatible priority strategy.")

    def remove_top_priority_from_priority_queue(self):
        """
        This is where we remove the object with the highest priority in the priority queue.
        After removing this object we then re-heapify the entire queue in order to ensure that the next
        object with the highest 'studentPriority' is at the top.
        :return: priorityQueue
        :rtype: []
        """

        if len(self.__priority_queue) <= 0:
            raise ValueError ("There are no elements in this queue to remove")
        else:
            self.__priority_queue[0] = self.__priority_queue[-1]
            self.__priority_queue.pop(-1)
            self.max_heapify()

    def set_priority_strategy(self, name_of_strategy):
        """
        This modifies the priority strategy to the desired choice.
        :param name_of_strategy: strategy to be chosen
        :return:
        """
        self.__priority_strategy.input = name_of_strategy

    def swap_priority_queue_index(self, node_index_one, node_index_two):
        """
        This swaps the position of two different nodes in the priority queue.
        :param node_index_one: the position of one node in the priority queue
        :param node_index_two: the position of another node in the priority queue
        :return: None
        """
        node_temp = self.__priority_queue[node_index_one]
        self.__priority_queue[node_index_one] = self.__priority_queue[node_index_two]
        self.__priority_queue[node_index_two] = node_temp

    def __iter__(self):
        """
        This initializes the iterator to be set to the PriorityQueue_iter class.
        :return: self
        :rtype: enumerate
        """
        return PriorityQueue_iter(self)

    def __str__(self):
        """
        :return:
        """
        return str(list(map(str, self.__priority_queue)))

class PriorityQueue_iter:

    def __init__(self, priority_queue):
        self.__temporary_queue = copy.deepcopy(priority_queue)
        self.size_of_priority_queue = len(self.__temporary_queue.get_all_data_from_priority_queue())
        self.__counter_temp_queue = 0

    def __iter__(self):
        """
        This initializes the iterator to be set to the PriorityQueue class itself.
        :return: self
        :rtype: enumerate
        """
        return self

    def __next__(self):
        if self.__counter_temp_queue < self.size_of_priority_queue:
            current_node = self.__temporary_queue.get_priority_queue()[0]
            self.__temporary_queue.remove_top_priority_from_priority_queue()
            self.__counter_temp_queue += 1
            return current_node
        else:
            raise StopIteration
