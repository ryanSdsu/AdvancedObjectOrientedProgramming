import unittest
from Assignment_Two import NodeClass
from Assignment_Two import PriorityQueueClass
from Assignment_Two import PriorityClass

class TestPriorityClass(unittest.TestCase):

    def setUp(self):
        """
        This is the set up for the 'Priority' class. We are creating the 'PriorityQueue' to be used later.
        :return:
        """
        self.test_priority_queue = PriorityQueueClass.PriorityQueue()

    def test_init_def(self):
        """
        This unit test is testing the __init__ def of a 'Priority' class. It passes when a 'Priority' class
        is successfully created.
        :return:
        """
        test_priority_class = PriorityClass.Priority(PriorityClass.default)
        self.assertIsInstance(test_priority_class, PriorityClass.Priority)

    def test_change_priority(self):
        """
        This unit test is testing the changing of a strategy in the 'PriorityQueue' class. It passes when
        a new strategy is set via the 'Priority' class.
        :return:
        """

        self.test_priority_queue.priority_strategy.input = PriorityClass.student
        self.assertEquals(self.test_priority_queue.priority_strategy.input, PriorityClass.student)
        self.test_priority_queue.priority_strategy.input = PriorityClass.default
        self.assertEquals(self.test_priority_queue.priority_strategy.input, PriorityClass.default)

# # one_argument_node.priority_strategy.input = PriorityClass.student
# one_argument_node.priority_strategy = PriorityClass.Priority(PriorityClass.student)
# one_argument_node.priority_value = one_argument_node.priority_strategy.input(2, 100)
# print(one_argument_node.priority_strategy.input)
# print(one_argument_node.priority_value)
#
#
# one_argument_node.priority_type.priority_strategy = PriorityClass.student
# one_argument_node.priority_type = one_argument_node.priority_type.priority_strategy(one_argument_node.data, 100)

if __name__ == '__main__':
    unittest.main()


