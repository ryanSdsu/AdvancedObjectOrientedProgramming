import unittest
from Assignment_Two import NodeClass
from Assignment_Two import PriorityQueueClass

class TestPriorityQueueClass(unittest.TestCase):

    def setUp(self):
        self.test_priority_queue = PriorityQueueClass.PriorityQueue()

    def test_add_to_priority_queue(self):
        """
        This unit test is testing the 'PriorityQueue' class definition 'add_to_priority_queue'.  This test passes
        if a Node of any type is successfully added into the '__priority_queue' along with it's priority.
        It also passes if the Node with the highest priority remains at the top of the queue via the max heap.
        :return:
        """
        import random
        for new_node_value in range(100):
            self.test_priority_queue.add_to_priority_queue(NodeClass.Node(new_node_value))
            self.assertEquals(self.test_priority_queue.get_data_from_priority_queue_index(0), new_node_value)
            self.assertEquals(self.test_priority_queue.get_priority_from_priority_queue_index(0), new_node_value)

        samples = random.sample(list(range(101, 200)),20)
        max_sample = max(samples)
        for new_node_value in samples:
            self.test_priority_queue.add_to_priority_queue(NodeClass.Node(new_node_value))

        self.assertEquals(self.test_priority_queue.get_data_from_priority_queue_index(0), max_sample)

    def test_get_data_from_priority_queue_index(self):
        """
        This unit test is testing the 'PriorityQueue' class definition 'get_data_from_priority_queue_index'.
        This test passes if a Node of any type is successfully added into the '__priority_queue' along with it's data
        still intact.
        :return:
        """
        for new_node_value in range(100):
            self.test_priority_queue.add_to_priority_queue(NodeClass.Node(new_node_value))
            self.assertEquals(self.test_priority_queue.get_data_from_priority_queue_index(0), new_node_value)

    def test_get_priority_from_priority_queue_index(self):
        """
        This unit test is testing the 'PriorityQueue' class definition 'get_priority_from_priority_queue_index'.
        This test passes if a Node of any type is successfully added into the '__priority_queue' along with it's data
        still intact.
        :return:
        """
        for new_node_value in range(100):
            self.test_priority_queue.add_to_priority_queue(NodeClass.Node(new_node_value))
            self.assertEquals(self.test_priority_queue.get_priority_from_priority_queue_index(0), new_node_value)

    def test_init_def(self):
        """
        This unit test is testing the __init__ def of a 'PriorityQueue' class. It passes when a 'PriorityQueue'
        is successfully created.
        :return:
        """
        cs635_priority_queue = PriorityQueueClass.PriorityQueue()
        self.assertIsInstance(cs635_priority_queue, PriorityQueueClass.PriorityQueue)



        # def test_iter_next_def(self):
    #     """
    #     This unit test is testing the __iter__ of a 'PriorityQueue' object. It passes when the '__priority_queue' list
    #     and all of its elements are iterated upon via the __next__ definition.
    #     :return:
    #     """
    #     int_one_node = NodeClass.Node(1)
    #     int_two_node = NodeClass.Node(2)
    #     int_three_node = NodeClass.Node(3)
    #     int_four_node = NodeClass.Node(4)
    #     self.test_priority_queue.add_to_priority_queue(int_one_node)
    #     self.test_priority_queue.add_to_priority_queue(int_two_node)
    #     self.test_priority_queue.add_to_priority_queue(int_three_node)
    #     self.test_priority_queue.add_to_priority_queue(int_four_node)
    #     self.assertEquals(self.test_priority_queue.__next__().data, 1)
    #     self.assertEquals(self.test_priority_queue.__next__().data, 2)
    #     self.assertEquals(self.test_priority_queue.__next__().data, 3)
    #     self.assertEquals(self.test_priority_queue.__next__().data, 4)

    # def test_str_def(self):
    #     """
    #     This unit test is testing the 'str' def of the 'PriorityQueue' class. It passes when upon proceeding with the
    #     __str__() def that the '__priority_queue' list is being passed to it.
    #     :return:
    #     """
    #     int_one_node = NodeClass.Node(1)
    #     self.test_priority_queue.add_to_priority_queue(int_one_node)
    #     self.assertEquals(self.test_priority_queue.__str__(), '[\'1\']')
    #
    #     int_two_node = NodeClass.Node(2)
    #     self.test_priority_queue.add_to_priority_queue(int_two_node)
    #     self.assertEquals(self.test_priority_queue.__str__(), '[\'1\', \'2\']')
    #
    #     int_three_node = NodeClass.Node(3)
    #     self.test_priority_queue.add_to_priority_queue(int_three_node)
    #     self.assertEquals(self.test_priority_queue.__str__(), '[\'1\', \'2\', \'3\']')


if __name__ == '__main__':
    unittest.main()


