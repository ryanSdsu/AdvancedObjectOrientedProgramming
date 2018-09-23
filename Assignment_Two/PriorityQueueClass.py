from Assignment_Two import NodeClass
from Assignment_Two import PriorityClass

class PriorityQueue:
    """This is the base class for the PriorityQueue, the main structure is a max heap."""
    def __init__(self):
        """
        This is the constructor for the PriorityQueue class.
        The initial 'None' ensures that students being added to the list start on index 1.
        Also the counter for the iter definition(s) is instantiated.
        """
        self.__priority_queue = []
        self.__counter_priority_queue = 0
        self.priority_strategy = PriorityClass.Priority(PriorityClass.default)
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
        self.priority_value = self.priority_strategy.input(data)
        priority_node = NodeClass.Node(data, self.priority_value)
        self.__priority_queue.append(priority_node)
        self.max_heapify()

    def max_heapify(self):
        """
        This sorts the priority_node(s) in the '__priority_queue' by traversing the nodes in the list
        so that the element with the highest 'priority_value' resides at the top via the max heap.
        In terms of traversal we iterate and check to see if there is a right child of the current node
        and if there is one we see if it's priority is greater than its parents. If this is the case we swap them.
        If not we check the left child (if there is one) and do the same thing.
        :return:
        """
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

    def get_data_from_priority_queue_index(self, priority_queue_index):
        """
        This returns the data from a certain index in the priority queue.
        :return: the data of a certain priority queue index
        :rtype: any
        """
        return self.__priority_queue[priority_queue_index].node_data[0].node_data

    def get_priority_from_priority_queue_index(self, priority_queue_index):
        """
        This returns the priority value from a certain index in the priority queue.
        :return: the priority value of a certain priority queue index
        :rtype: float or int
        """
        return self.__priority_queue[priority_queue_index].node_data[1].node_data

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
        This initializes the iterator to be set to the PriorityQueue class itself.
        :return: self
        :rtype: enumerate
        """
        return self

    def __next__(self):
        if self.__counter_priority_queue < len(self.__priority_queue):
            current_node = self.__priority_queue[self.__counter_priority_queue]
            self.__counter_priority_queue += 1
            return current_node
        else:
            raise StopIteration

    def __str__(self):
        """
        :return:
        """
        return str(list(map(str, self.__priority_queue)))

pq = PriorityQueue()
one_node = NodeClass.Node(1)
pq.add_to_priority_queue(one_node)
two_node = NodeClass.Node(2)
pq.add_to_priority_queue(two_node)
print(pq)