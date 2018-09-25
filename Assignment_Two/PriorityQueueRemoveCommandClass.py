class PriorityQueueRemoveCommand():
    """This is the base class for the PriorityQueueRemoveCommand class."""
    def __init__(self, priority_queue):
        """
        This sets up the command pattern to include both the data and the
        priority queue for which to be removed upon.
        :param data: the entry for which to be removed
        :param priority_queue: the queue for which to be removed upon
        """
        self.data = None
        self.priority_queue = priority_queue

    def execute(self):
        """
        This executes the PriorityQueue class command 'remove_node_from_priority_queue'.
        :return:
        """
        self.data = self.priority_queue.get_data_from_priority_queue_index(0)
        self.priority_queue.remove_top_priority_node_from_priority_queue()

    def undo(self):
        """
        This initiates and 'undo' action on the PriorityQueue class command
        'remove_node_from_priority_queue'.
        :return:
        """
        self.priority_queue.add_to_priority_queue(self.data)