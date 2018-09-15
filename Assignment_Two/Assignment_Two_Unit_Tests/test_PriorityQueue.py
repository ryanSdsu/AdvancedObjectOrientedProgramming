import unittest
from Assignment_Two import NodeClass
from Assignment_Two import PriorityQueueClass

class TestPriorityQueueClass(unittest.TestCase):

    def setUp(self):
        self.test_priority_queue = PriorityQueueClass.PriorityQueue()

    def test_init_def(self):
        """
        This unit test is testing the __init__ def of a 'PriorityQueue' class. It passes when a 'PriorityQueue'
        is successfully created.
        :return:
        """
        cs635_priority_queue = PriorityQueueClass.PriorityQueue()
        self.assertIsInstance(cs635_priority_queue, PriorityQueueClass.PriorityQueue)

    def test_add_to_priority_queue(self):
        """
        This unit test is testing the 'PriorityQueue' class definition 'add_to_priority_queue'.  This test passes
        if a Node of any type is successfully added into the '__priority_queue'.
        :return:
        """
        int_node = NodeClass.Node(1)
        self.test_priority_queue.add_to_priority_queue(int_node)
        self.assertEquals(self.test_priority_queue.__next__(), None)
        self.assertEquals(self.test_priority_queue.__next__().data, 1)

    def test_iter_next_def(self):
        """
        This unit test is testing the __iter__ of a 'PriorityQueue' object. It passes when the '__priority_queue' list
        and all of its elements are iterated upon via the __next__ definition.
        :return:
        """
        int_one_node = NodeClass.Node(1)
        int_two_node = NodeClass.Node(2)
        int_three_node = NodeClass.Node(3)
        int_four_node = NodeClass.Node(4)
        self.test_priority_queue.add_to_priority_queue(int_one_node)
        self.test_priority_queue.add_to_priority_queue(int_two_node)
        self.test_priority_queue.add_to_priority_queue(int_three_node)
        self.test_priority_queue.add_to_priority_queue(int_four_node)
        self.assertEquals(self.test_priority_queue.__next__(), None)
        self.assertEquals(self.test_priority_queue.__next__().data, 1)
        self.assertEquals(self.test_priority_queue.__next__().data, 2)
        self.assertEquals(self.test_priority_queue.__next__().data, 3)
        self.assertEquals(self.test_priority_queue.__next__().data, 4)

    def test_str_def(self):
        """
        This unit test is testing the 'str' def of the 'PriorityQueue' class. It passes when upon proceeding with the
        __str__() def that the '__priority_queue' list is being passed to it.
        :return:
        """
        int_one_node = NodeClass.Node(1)
        self.test_priority_queue.add_to_priority_queue(int_one_node)
        self.assertEquals(self.test_priority_queue.__str__(), '[\'None\', \'1\']')

        int_two_node = NodeClass.Node(2)
        self.test_priority_queue.add_to_priority_queue(int_two_node)
        self.assertEquals(self.test_priority_queue.__str__(), '[\'None\', \'1\', \'2\']')

        int_three_node = NodeClass.Node(3)
        self.test_priority_queue.add_to_priority_queue(int_three_node)
        self.assertEquals(self.test_priority_queue.__str__(), '[\'None\', \'1\', \'2\', \'3\']')


if __name__ == '__main__':
    unittest.main()


