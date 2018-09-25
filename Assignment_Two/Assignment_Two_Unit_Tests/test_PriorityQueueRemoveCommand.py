import unittest
from Assignment_Two import PriorityQueueClass
from Assignment_Two import PriorityQueueRemoveCommandClass

class TestPriorityQueueRemoveCommandClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Priority Queue Remove Command Class"""
    def setUp(self):
        """
        This is the set up for the 'PriorityQueueRemoveCommandClass' class. We are creating the
        'PriorityQueue' class to be invoked later.
        :return:
        """
        self.test_priority_queue = PriorityQueueClass.PriorityQueue()

    def test_init_def(self):
        """
        This unit test is testing the __init__ def of a 'PriorityQueueRemoveCommandClass' class. It passes when a
        'PriorityQueueRemoveCommandClass' is successfully created along with data and priority queue both being
        instantiated.
        :return:
        """
        priority_queue_remove_command = PriorityQueueRemoveCommandClass.PriorityQueueRemoveCommand(self.test_priority_queue)
        self.assertIsInstance(priority_queue_remove_command, PriorityQueueRemoveCommandClass.PriorityQueueRemoveCommand)
        self.assertEquals(priority_queue_remove_command.data, None)
        self.assertEqual(priority_queue_remove_command.priority_queue, self.test_priority_queue)

    def test_execute_def(self):
        """
        This unit test is testing the execute def of the 'PriorityQueueRemoveCommandClass' class. It passes when a
        successful command is invoked i.e. remove_node_from_priority_queue.
        :return:
        """
        self.test_priority_queue.add_to_priority_queue(1)
        self.assertListEqual(self.test_priority_queue.get_all_data_from_priority_queue(), [1])
        priority_queue_remove_command = PriorityQueueRemoveCommandClass.PriorityQueueRemoveCommand(self.test_priority_queue)
        priority_queue_remove_command.execute()
        self.assertListEqual(self.test_priority_queue.get_all_data_from_priority_queue(), [])

    def test_undo_def(self):
        """
        This unit test is testing the undo def of the 'PriorityQueueRemoveCommandClass' class. It passes when a
        successful command is invoked i.e. add_to_priority_queue.
        :return:
        """
        self.test_priority_queue.add_to_priority_queue(1)
        self.assertListEqual(self.test_priority_queue.get_all_data_from_priority_queue(), [1])
        priority_queue_remove_command = PriorityQueueRemoveCommandClass.PriorityQueueRemoveCommand(self.test_priority_queue)
        priority_queue_remove_command.execute()
        self.assertListEqual(self.test_priority_queue.get_all_data_from_priority_queue(), [])
        priority_queue_remove_command.undo()
        self.assertListEqual(self.test_priority_queue.get_all_data_from_priority_queue(), [1])

if __name__ == '__main__':
    unittest.main()


