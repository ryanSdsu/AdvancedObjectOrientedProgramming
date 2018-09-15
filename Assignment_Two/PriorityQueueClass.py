class PriorityQueue:
    """This is the base class for the PriorityQueue, the main structure is a max heap."""
    def __init__(self):
        """
        This is the constructor for the PriorityQueue class.
        The initial 'None' ensures that students being added to the list start on index 1.
        Also the counter for the iter definition(s) is instantiated.
        """
        self.__priority_queue = [None]
        self.__counter_priority_queue = 0

    def add_to_priority_queue(self, Node):
        """
        This is where we add a new object into the 'priority_queue'.  The main structure is a max heap therefore
        all of the objects being added must traverse to the top of the list based on the highest 'priority'. As a
        reminder the parents of each newly added object in a max heap is the "floor" of the index / 2.
        :param Node
        :return: priority_queue
        :rtype: []
        """
        # To begin we will confirm if the newly added object has any "parents".
        # Since the parents location of the newly added object is the "floor" of the newly added objects index / 2,
        # we can simply compute this by doing a bit shift to the right.
        self.__priority_queue.append(Node)
        # self.current_index_root_node = len(self.__priority_queue) - 1
        # new_node_parent_location = self.current_index_root_node >> 1
        #
        # # If the newly added object has parents we can now check the ''.
        # # If the newly added objects 'studentPriority' is lower than that of it's parents, we will traverse it upwards
        # # on the 'priorityQueue' by swapping their locations.
        # while (new_node_parent_location > 0):
        #     if Node.studentPriority > self.__priority_queue[new_node_parent_location].studentPriority:
        #         self.traverseObjectIndexInPriorityQueue(new_node_parent_location, self.current_index_root_node, new_node_parent_location)
        #         new_node_parent_location = new_node_parent_location >> 1
        #     else:
        #         new_node_parent_location = new_node_parent_location >> 1
        # return self.__priority_queue

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter_priority_queue < len(self.__priority_queue):
            current_node = self.__priority_queue[self.__counter_priority_queue]
            self.__counter_priority_queue += 1
            return current_node
        else:
            raise StopIteration

    def __str__(self):
        return str(list(map(str, self.__priority_queue)))