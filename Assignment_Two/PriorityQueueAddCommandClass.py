class AddCommand():
    """This is the base class for the PriorityQueueAddCommand class."""
    def __init__(self, data,  priority_queue):
        """
        This sets up the command pattern to include both the data and the
        priority queue for which to be added upon.
        :param data: the entry for which to be added
        :param priority_queue: the queue for which to be added upon
        """
        self.data = data
        self.priority_queue = priority_queue

    def execute(self):
        """
        This executes the PriorityQueue class command 'add_to_priority_queue'.
        :return:
        """
        self.priority_queue.add_to_priority_queue(self.data)

    def undo(self):
        """
        This initiates and 'undo' action on the PriorityQueue class command
        'add_to_priority_queue'.
        :return:
        """
        self.priority_queue.remove_node_from_priority_queue(self.data)