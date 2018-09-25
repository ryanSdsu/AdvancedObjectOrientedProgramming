import unittest
import random
from Assignment_Two import NodeClass
from Assignment_Two import PriorityQueueClass
from Assignment_Two import PriorityClass
from Assignment_Two import StudentClass

class TestPriorityQueueClass(unittest.TestCase):
    """This is the base class for the unit tests involving the PriorityQueue Class"""
    def setUp(self):
        """
        This is the set up for the 'PriorityQueue' class. We are creating the 'PriorityQueue' to be used later.
        We are also creating instances of the 'StudentClass' via student objects which are set to be added
        and tested.
        :return:
        """
        self.test_priority_queue = PriorityQueueClass.PriorityQueue()
        self.student_david = StudentClass.Student("David", 111111111, "David@aol.com", "134 Red St", 2.0, 75)
        self.student_eric = StudentClass.Student("Eric", 222222222, "Eric@aol.com", "135 Yolo St", 3.0, 100)
        self.student_nathan = StudentClass.Student("Nathan", 333333333, "Nathan@aol.com", "136 Welp St", 3.5, 120)
        self.student_paul = StudentClass.Student("Paul", 444444444, "Paul@aol.com", "137 Uinx St", 3.8, 148)
        self.student_chris = StudentClass.Student("Chris", 555555555, "Chris@aol.com", "138 Down St", 3.6, 121)
        self.student_bob = StudentClass.Student("Bob", 666666666, "Bob@aol.com", "139 Up St", 2.5, 7.6)
        self.student_larissa = StudentClass.Student("Larissa", 777777777, "Larissa@aol.com", "140 Cool St", 3.25, 110)
        self.student_mark = StudentClass.Student("Mark", 888888888, "Mark@aol.com", "141 Pole St", 3.65, 122)
        self.student_heath = StudentClass.Student("Heath", 999999999, "Heath@aol.com", "142 Red St", 0, 0)
        self.student_sarah = StudentClass.Student("Sarah", 100000000, "Sarah@aol.com", "143 Oil St", 3.7, 123)
        self.student_ashley = StudentClass.Student("Ashley", 110000000, "Ashley@aol.com", "144 Far St", 3.9, 149)
        self.student_ryan = StudentClass.Student("Ryan", 120000000, "Ryan@aol.com", "145 Guard St", 4, 150)
        self.student_jake = StudentClass.Student("Jake", 130000000, "Jake@aol.com", "146 Palace St", 1, 1)
        self.student_drake = StudentClass.Student("Drake", 140000000, "Drake@aol.com", "147 Nom St", 1, 1)
        self.student_blake = StudentClass.Student("Blake", 150000000, "Blake@aol.com", "148 Lol St", 1, 1)

    def _get(self):
        """
        This unit test is testing the _get definition in the PriorityQueue class. It passes when the queue
        variable returns the top node of the queue i.e. the one with the highest priority.
        :return:
        """
        for index in range(5):
            self.test_priority_queue._put(index)
        for index in range(5, -1, -1):
            self.assertEquals(self.test_priority_queue._get(), index)

    def test_get_all_data_from_priority_queue(self):
        """
        This unit test is testing the get_all_data_from_priority_queue definition in the PriorityQueue class.
        It passes when the priority queue's nodes are returned in a list once the the definition is called.
        :return:
        """
        for data in range(1,10):
            self.test_priority_queue.add_to_priority_queue(data)

        self.assertListEqual(self.test_priority_queue.get_all_data_from_priority_queue(),
                             [9, 8, 6, 7, 3, 2, 5, 1, 4])

    def test_get_priority_queue(self):
        """
        This unit test is testing the get_priority_queue definition in the PriorityQueue class.
        It passes when the priority queue is returned successfully.
        :return:
        """
        for data in range(1,10):
            self.test_priority_queue.add_to_priority_queue(data)

        self.assertListEqual(self.test_priority_queue.get_priority_queue(),
                             [[9, 9], [8, 8], [6, 6], [7, 7], [3, 3], [2, 2], [5, 5], [1, 1], [4, 4]])

    def test_get_data_from_priority_queue_index(self):
        """
        This unit test is testing the get_data_from_priority_queue_index definition in the PriorityQueue class.
        It passes when a specific priority queue node's data is returned based on the index that was passed.
        :return:
        """
        test_range = 20

        for index in range(test_range):
            self.test_priority_queue.get_priority_queue().append([index,0])

        for index in range(test_range):
            self.assertEquals(self.test_priority_queue.get_data_from_priority_queue_index(index), index)


    def test_get_priority_from_priority_queue_index(self):
        """
        This unit test is testing the get_priority_from_priority_queue_index definition in the PriorityQueue class.
        It passes when a specific priority queue node's priority is returned based on the index that was passed.
        :return:
        """
        test_range = 20

        for index in range(test_range):
            self.test_priority_queue.get_priority_queue().append([0,index])

        for index in range(test_range):
            self.assertEquals(self.test_priority_queue.get_priority_from_priority_queue_index(index), index)

    def test_get_and_set_priority_strategy(self):
        """
        This unit test is testing the get_priority_strategy definition in the PriorityQueue class.
        It passes when the priority queue strategy is returned successfully.
        :return:
        """

        self.test_priority_queue.set_priority_strategy(PriorityClass.student)

        self.assertEquals(self.test_priority_queue.get_priority_strategy(), PriorityClass.student)

    def test_init_def(self):
        """
        This unit test is testing the __init__ def of a 'PriorityQueue' class. It passes when a 'PriorityQueue'
        is successfully created.
        :return:
        """
        cs635_priority_queue = PriorityQueueClass.PriorityQueue()
        self.assertIsInstance(cs635_priority_queue, PriorityQueueClass.PriorityQueue)


    def test_iter_def_and_priority_queue_iter(self):
        """
        This unit test is testing the __iter__ of a 'PriorityQueue' object as well as it's subclass
        'PriorityQueueIter. It passes when the '__priority_queue' list and all of its nodes are iterated
        upon via the __next__ definition. Each of the iterations must be with the highest priority. It also
        passes upon the checking of the has_next, is_done and current_item definitions.
        :return:
        """
        self.test_priority_queue.set_priority_strategy(PriorityClass.node())
        int_one_node = NodeClass.Node(1)
        int_two_node = NodeClass.Node(2)
        int_three_node = NodeClass.Node(3)
        int_four_node = NodeClass.Node(4)

        self.test_priority_queue.add_to_priority_queue(int_one_node)
        self.test_priority_queue.add_to_priority_queue(int_two_node)
        self.test_priority_queue.add_to_priority_queue(int_three_node)
        self.test_priority_queue.add_to_priority_queue(int_four_node)

        iter_priority = self.test_priority_queue.__iter__()

        self.assertEquals(iter_priority.has_next(), True)
        self.assertEquals(iter_priority.is_done(), False)
        self.assertEquals(iter_priority.__next__()[1], int_four_node.node_data)
        self.assertEquals(iter_priority.is_done(), False)
        self.assertEquals(iter_priority.has_next(), True)
        self.assertEquals(iter_priority.current_item()[1], int_four_node.node_data)
        self.assertEquals(iter_priority.__next__()[1], int_three_node.node_data)
        self.assertEquals(iter_priority.is_done(), False)
        self.assertEquals(iter_priority.has_next(), True)
        self.assertEquals(iter_priority.current_item()[1], int_three_node.node_data)
        self.assertEquals(iter_priority.__next__()[1], int_two_node.node_data)
        self.assertEquals(iter_priority.is_done(), False)
        self.assertEquals(iter_priority.has_next(), True)
        self.assertEquals(iter_priority.current_item()[1], int_two_node.node_data)
        self.assertEquals(iter_priority.__next__()[1], int_one_node.node_data)
        self.assertEquals(iter_priority.has_next(), False)
        self.assertEquals(iter_priority.is_done(), True)
        self.assertEquals(iter_priority.current_item()[1], int_one_node.node_data)

    def test_max_heapify(self):
        """
        This unit test is testing the max_heapify def of a 'PriorityQueue' class. It passes whenever an
        node is added into the priority queue and after being added it automatically bubbles
        the node with the highest priority to the top of the queue.
        :return:
        """
        samples = random.sample(list(range(101, 200)),20)
        for node in samples:
            self.test_priority_queue.get_priority_queue().append([node,node])
            max_sample = max(self.test_priority_queue.get_all_data_from_priority_queue())
            self.test_priority_queue.max_heapify()
            self.assertEquals(self.test_priority_queue.get_data_from_priority_queue_index(0),max_sample)

    def test_node_add_to_priority_queue(self):
        """
        This unit test is testing the 'PriorityQueue' class definition 'add_to_priority_queue'.  This test passes
        if a Node of any type is successfully added into the '__priority_queue' along with it's priority.
        It also passes if the Node with the highest priority remains at the top of the queue via the 'max_heapify'.
        :return:
        """
        self.test_priority_queue.set_priority_strategy(PriorityClass.node())
        for new_node_value in range(100):
            self.test_priority_queue.add_to_priority_queue(NodeClass.Node(new_node_value))
            self.assertEquals(self.test_priority_queue.get_data_from_priority_queue_index(0).node_data, new_node_value)
            self.assertEquals(self.test_priority_queue.get_priority_from_priority_queue_index(0), new_node_value)

        samples = random.sample(list(range(101, 200)),20)
        max_sample = max(samples)
        for new_node_value in samples:
            self.test_priority_queue.add_to_priority_queue(NodeClass.Node(new_node_value))

        self.assertEquals(self.test_priority_queue.get_data_from_priority_queue_index(0).node_data, max_sample)

    def test_node_get_data_from_priority_queue_index(self):
        """
        This unit test is testing the 'PriorityQueue' class definition 'get_data_from_priority_queue_index'.
        This test passes if a Node of any type is successfully added into the '__priority_queue' along with it's data
        still intact.
        :return:
        """
        self.test_priority_queue.set_priority_strategy(PriorityClass.node())
        for new_node_value in range(100):
            self.test_priority_queue.add_to_priority_queue(NodeClass.Node(new_node_value))
            self.assertEquals(self.test_priority_queue.get_data_from_priority_queue_index(0).node_data, new_node_value)

    def test_node_get_priority_from_priority_queue_index(self):
        """
        This unit test is testing the 'PriorityQueue' class definition 'get_priority_from_priority_queue_index'.
        This test passes if a Node of any type is successfully added into the '__priority_queue' along with it's data
        still intact.
        :return:
        """
        self.test_priority_queue.set_priority_strategy(PriorityClass.node())
        for new_node_value in range(100):
            self.test_priority_queue.add_to_priority_queue(NodeClass.Node(new_node_value))
            self.assertEquals(self.test_priority_queue.get_priority_from_priority_queue_index(0), new_node_value)

    def test_node_remove_def(self):
        """
        This unit test is testing the __iter__ of a 'PriorityQueue' object. It passes when the '__priority_queue' list
        and all of its nodes are iterated upon via the __next__ definition. Each of the iterations must be with the
        highest priority.
        :return:
        """

        self.test_priority_queue.add_to_priority_queue(1)
        self.test_priority_queue.add_to_priority_queue(2)
        self.test_priority_queue.add_to_priority_queue(3)
        self.test_priority_queue.add_to_priority_queue(4)
        self.test_priority_queue.add_to_priority_queue(5)

        self.test_priority_queue.remove_node_from_priority_queue(1)
        self.assertListEqual(self.test_priority_queue.get_all_data_from_priority_queue(),
                             [5, 4, 2, 3])

        self.test_priority_queue.remove_node_from_priority_queue(5)
        self.assertListEqual(self.test_priority_queue.get_all_data_from_priority_queue(),
                             [4, 2, 3])

        self.test_priority_queue.remove_node_from_priority_queue(3)
        self.assertListEqual(self.test_priority_queue.get_all_data_from_priority_queue(),
                             [4, 2])

        self.test_priority_queue.remove_node_from_priority_queue(4)
        self.assertListEqual(self.test_priority_queue.get_all_data_from_priority_queue(),
                             [2])

    def test_put(self):
        """
        This unit test is testing the 'PriorityQueue' class definition '_put'.  This test passes
        if a Node of any type is successfully added into the overwritten 'queue' variable and
        the highest value bubbles up to the top after being sorted.
        :return:
        """
        for index in range(5):
            self.test_priority_queue._put(index)
        self.assertListEqual(self.test_priority_queue.queue, [4,3,1,0,2])

    def test_qsize(self):
        """
        This unit test is testing the _qsize def of a 'PriorityQueue' class. It passes when the correct
        length of the queue at any given time is returned.
        :return:
        """
        queue_size = 10
        for index in range(queue_size):
            self.test_priority_queue.queue.append(index)

        self.assertEquals(self.test_priority_queue._qsize(), queue_size)

    def test_student_add_to_priority_queue(self):
        """
        This unit test is testing the PriorityQueue class definition 'add_to_priority_queue' with student objects.
        This test passes if all 15 'student' objects which were instantiated in the 'setUp' definition are
        successfully added to the priority queue and are in priority order.
        :return:
        """
        self.test_priority_queue.set_priority_strategy(PriorityClass.student())
        self.test_priority_queue.add_to_priority_queue(self.student_david)
        self.test_priority_queue.add_to_priority_queue(self.student_eric)
        self.test_priority_queue.add_to_priority_queue(self.student_nathan)
        self.test_priority_queue.add_to_priority_queue(self.student_paul)
        self.test_priority_queue.add_to_priority_queue(self.student_chris)
        self.test_priority_queue.add_to_priority_queue(self.student_bob)
        self.test_priority_queue.add_to_priority_queue(self.student_larissa)
        self.test_priority_queue.add_to_priority_queue(self.student_mark)
        self.test_priority_queue.add_to_priority_queue(self.student_heath)
        self.test_priority_queue.add_to_priority_queue(self.student_sarah)
        self.test_priority_queue.add_to_priority_queue(self.student_ashley)
        self.test_priority_queue.add_to_priority_queue(self.student_ryan)
        self.test_priority_queue.add_to_priority_queue(self.student_jake)
        self.test_priority_queue.add_to_priority_queue(self.student_drake)
        self.test_priority_queue.add_to_priority_queue(self.student_blake)
        self.assertListEqual(self.test_priority_queue.get_all_data_from_priority_queue(),
                             [self.student_ryan, self.student_paul, self.student_ashley,
                              self.student_chris, self.student_sarah, self.student_larissa,
                              self.student_eric, self.student_david, self.student_heath,
                              self.student_nathan, self.student_mark, self.student_bob,
                              self.student_jake, self.student_drake, self.student_blake])

    def test_student_add_to_priority_queue_size_check(self):
        """
        This unit test is testing the PriorityQueue class definition 'add_to_priority_queue'.
        This test goes and increments the size and ensures that whenever an object is added to the priority queue
        that the length is growing by an index of 1. The number of iterations can be determined by
        adjusting the 'number_of_students_to_add'variable.
        :return:
        """
        number_of_students_to_add = 5
        self.test_priority_queue.set_priority_strategy(PriorityClass.student())
        for index in range(number_of_students_to_add):
            self.test_priority_queue.add_to_priority_queue(self.student_david)

        length_of_priotity_queue = len(self.test_priority_queue.get_all_data_from_priority_queue())

        self.assertEquals(number_of_students_to_add, length_of_priotity_queue)

    def test_student_remove_highest_priority_Node(self):
        """
        This unit test is testing the PriorityQueue class definition 'remove_from_priority_queue'.  This test passes
        if all 15 'student' objects which were instantiated in the 'setUp' definition are successfully added to the
        priority queue and then the 'student' object Ryan is removed once the definition 'remove_from_priority_queue'
        is called. The priority queue must maintain priority order at all times with the 'student' object having the
        highest priority be on the top of the list since the structure is based on a max heap.
        :return:
        """
        self.test_priority_queue.set_priority_strategy(PriorityClass.student())
        self.test_priority_queue.add_to_priority_queue(self.student_david)
        self.test_priority_queue.add_to_priority_queue(self.student_eric)
        self.test_priority_queue.add_to_priority_queue(self.student_nathan)
        self.test_priority_queue.add_to_priority_queue(self.student_paul)
        self.test_priority_queue.add_to_priority_queue(self.student_chris)
        self.test_priority_queue.add_to_priority_queue(self.student_bob)
        self.test_priority_queue.add_to_priority_queue(self.student_larissa)
        self.test_priority_queue.add_to_priority_queue(self.student_mark)
        self.test_priority_queue.add_to_priority_queue(self.student_heath)
        self.test_priority_queue.add_to_priority_queue(self.student_sarah)
        self.test_priority_queue.add_to_priority_queue(self.student_ashley)
        self.test_priority_queue.add_to_priority_queue(self.student_ryan)
        self.test_priority_queue.add_to_priority_queue(self.student_jake)
        self.test_priority_queue.add_to_priority_queue(self.student_drake)
        self.test_priority_queue.add_to_priority_queue(self.student_blake)
        self.test_priority_queue.remove_top_priority_node_from_priority_queue()
        self.assertEqual(self.test_priority_queue.get_data_from_priority_queue_index(0), self.student_ashley)

    def test_student_remove_from_priority_queue_size_check(self):
        """
        This unit test is testing the PriorityQueue class definition 'remove_from_priority_queue'.  This test passes
        if a fixed number of 'student' objects which were instantiated in the 'setUp' definition are successfully
        added to the priority queue and then a specified number are removed once the definition
        'remove_from_priority_queue' is called. The number of iterations that the definition
        'remove_from_priority_queue' is called is based on the 'number_of_students_to_remove' variable.
        :return:
        """
        number_of_students_to_add = 15
        number_of_students_to_remove = 10

        self.test_priority_queue.set_priority_strategy(PriorityClass.student())
        for student in range(number_of_students_to_add):
            self.test_priority_queue.add_to_priority_queue(self.student_david)

        for student in range(number_of_students_to_remove):
            self.test_priority_queue.remove_top_priority_node_from_priority_queue()

        self.assertEquals(number_of_students_to_add-number_of_students_to_remove,
                          len(self.test_priority_queue.get_all_data_from_priority_queue()))

    def test_remove_node_from_priority_queue(self):
        """
        This unit test is testing the remove_node_from_priority_queue definition from the
        priority queue class. It passes when a node is removed from the priority queue
        based on the data of which it is passed.
        :return:
        """
        samples = random.sample(list(range(101, 200)),20)
        for new_node_value in samples:
            self.test_priority_queue.add_to_priority_queue(new_node_value)
        for node_to_be_removed in samples:
            self.test_priority_queue.remove_node_from_priority_queue(node_to_be_removed)
            self.assertTrue(node_to_be_removed not in self.test_priority_queue.get_all_data_from_priority_queue())

    def test_remove_top_priority_node_from_priority_queue(self):
        """
        This unit test is testing the remove_top_priority_node_from_priority_queue definition from the
        priority queue class. It passes when the node with the top priority is removed from the priority
        queue.
        :return:
        """
        samples = random.sample(list(range(101, 200)),5)
        number_of_samples = len(samples) - 1
        max_sample = max(samples)
        for new_node_value in samples:
            self.test_priority_queue.add_to_priority_queue(new_node_value)

        for index in range(number_of_samples):
            max_sample = max(self.test_priority_queue.get_all_data_from_priority_queue())
            self.assertEquals(self.test_priority_queue.remove_top_priority_node_from_priority_queue(),
                              [max_sample, max_sample])

    def test_str_def(self):
        """
        This unit test is testing the 'str' def of the 'PriorityQueue' class. It passes when upon proceeding with the
        __str__() def that the '__priority_queue' list is being passed to it.
        :return:
        """
        self.test_priority_queue.add_to_priority_queue(1)
        self.assertEquals(self.test_priority_queue.__str__(), '[1, 1]\n')

        self.test_priority_queue.add_to_priority_queue(2)
        self.assertEquals(self.test_priority_queue.__str__(), '[2, 2]\n[1, 1]\n' )

        self.test_priority_queue.add_to_priority_queue(3)
        self.assertEquals(self.test_priority_queue.__str__(), '[3, 3]\n[2, 2]\n[1, 1]\n')

    def test_swap_priority_queue_index(self):
        """
        This definition tests the swapping of two elements in the priority queue. This test passes
        when the location of two different indices are swapped correctly in the priority queue.
        :return:
        """
        self.test_priority_queue.add_to_priority_queue(0)
        self.test_priority_queue.add_to_priority_queue(1)
        self.test_priority_queue.swap_priority_queue_index(0,1)
        self.assertListEqual(self.test_priority_queue.get_all_data_from_priority_queue(), [0, 1])

if __name__ == '__main__':
    unittest.main()


