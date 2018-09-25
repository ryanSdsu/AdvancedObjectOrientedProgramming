import unittest
from Assignment_Two import PriorityQueueClass
from Assignment_Two import PriorityQueueAddCommandClass

class TestPriorityQueueAddCommandClass(unittest.TestCase):

    def setUp(self):
        """
        This is the set up for the 'PriorityQueueAddCommand' class. We are creating the 'PriorityQueue' class to
        be invoked later.
        :return:
        """
        self.test_priority_queue = PriorityQueueClass.PriorityQueue()

    def test_init_def(self):
        """
        This unit test is testing the __init__ def of a 'PriorityQueueAddCommand' class. It passes when a
        'PriorityQueueAddCommand' is successfully created along with data and priority queue both being
        instantiated.
        :return:
        """
        priority_queue_add_command = PriorityQueueAddCommandClass.PriorityQueueAddCommand(1, self.test_priority_queue)
        self.assertIsInstance(priority_queue_add_command, PriorityQueueAddCommandClass.PriorityQueueAddCommand)
        self.assertEquals(priority_queue_add_command.data, 1)
        self.assertEqual(priority_queue_add_command.priority_queue, self.test_priority_queue)

    def test_execute_def(self):
        """
        This unit test is testing the execute def of the 'PriorityQueueAddCommand' class. It passes when a
        successful command is invoked i.e. add_to_priority_queue.
        :return:
        """
        add_command = PriorityQueueAddCommandClass.PriorityQueueAddCommand(1, self.test_priority_queue)
        add_command.execute()
        self.assertListEqual(self.test_priority_queue.get_all_data_from_priority_queue(), [1])

    def test_undo_def(self):
        """
        This unit test is testing the undo def of the 'PriorityQueueAddCommand' class. It passes when a
        successful command is invoked i.e. remove_node_from_priority_queue.
        :return:
        """
        add_command = PriorityQueueAddCommandClass.PriorityQueueAddCommand(1, self.test_priority_queue)
        add_command.execute()
        self.assertListEqual(self.test_priority_queue.get_all_data_from_priority_queue(), [1])
        add_command.undo()
        self.assertListEqual(self.test_priority_queue.get_all_data_from_priority_queue(), [])

if __name__ == '__main__':
    unittest.main()


