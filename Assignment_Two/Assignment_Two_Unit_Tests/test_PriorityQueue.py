import unittest
from Assignment_Two import NodeClass
from Assignment_Two import PriorityQueueClass
from Assignment_Two import PriorityClass
from Assignment_Two import StudentClass

class TestPriorityQueueClass(unittest.TestCase):

    def setUp(self):
        self.test_priority_queue = PriorityQueueClass.PriorityQueue()
        self.studentDavid = StudentClass.Student("David", 111111111, "David@aol.com", "134 Red St", 2.0, 75)
        self.studentEric = StudentClass.Student("Eric", 222222222, "Eric@aol.com", "135 Yolo St", 3.0, 100)
        self.studentNathan = StudentClass.Student("Nathan", 333333333, "Nathan@aol.com", "136 Welp St", 3.5, 120)
        self.studentPaul = StudentClass.Student("Paul", 444444444, "Paul@aol.com", "137 Uinx St", 3.8, 148)
        self.studentChris = StudentClass.Student("Chris", 555555555, "Chris@aol.com", "138 Down St", 3.6, 121)
        self.studentBob = StudentClass.Student("Bob", 666666666, "Bob@aol.com", "139 Up St", 2.5, 7.6)
        self.studentLarissa = StudentClass.Student("Larissa", 777777777, "Larissa@aol.com", "140 Cool St", 3.25, 110)
        self.studentMark = StudentClass.Student("Mark", 888888888, "Mark@aol.com", "141 Pole St", 3.65, 122)
        self.studentHeath = StudentClass.Student("Heath", 999999999, "Heath@aol.com", "142 Red St", 0, 0)
        self.studentSarah = StudentClass.Student("Sarah", 100000000, "Sarah@aol.com", "143 Oil St", 3.7, 123)
        self.studentAshley = StudentClass.Student("Ashley", 110000000, "Ashley@aol.com", "144 Far St", 3.9, 149)
        self.studentRyan = StudentClass.Student("Ryan", 120000000, "Ryan@aol.com", "145 Guard St", 4, 150)
        self.studentJake = StudentClass.Student("Jake", 130000000, "Jake@aol.com", "146 Palace St", 1, 1)
        self.studentDrake = StudentClass.Student("Drake", 140000000, "Drake@aol.com", "147 Nom St", 1, 1)
        self.studentBlake = StudentClass.Student("Blake", 150000000, "Blake@aol.com", "148 Lol St", 1, 1)

    def test_init_def(self):
        """
        This unit test is testing the __init__ def of a 'PriorityQueue' class. It passes when a 'PriorityQueue'
        is successfully created.
        :return:
        """
        cs635_priority_queue = PriorityQueueClass.PriorityQueue()
        self.assertIsInstance(cs635_priority_queue, PriorityQueueClass.PriorityQueue)

    def test_node_add_to_priority_queue(self):
        """
        This unit test is testing the 'PriorityQueue' class definition 'add_to_priority_queue'.  This test passes
        if a Node of any type is successfully added into the '__priority_queue' along with it's priority.
        It also passes if the Node with the highest priority remains at the top of the queue via the max heap.
        :return:
        """
        import random

        self.test_priority_queue.set_priority_strategy(PriorityClass.node)
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
        self.test_priority_queue.set_priority_strategy(PriorityClass.node)
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
        self.test_priority_queue.set_priority_strategy(PriorityClass.node)
        for new_node_value in range(100):
            self.test_priority_queue.add_to_priority_queue(NodeClass.Node(new_node_value))
            self.assertEquals(self.test_priority_queue.get_priority_from_priority_queue_index(0), new_node_value)

    def test_student_add_to_priority_queue(self):
        """
        This unit test is testing the PriorityQueue class definition 'add_to_priority_queue' with student objects.
        This test passes if all 15 'student' objects which were instantiated in the 'setUp' definition are
        successfully added to the priority queue and are in priority order.
        :return:
        """
        self.test_priority_queue.set_priority_strategy(PriorityClass.student)
        self.test_priority_queue.add_to_priority_queue(self.studentDavid)
        self.test_priority_queue.add_to_priority_queue(self.studentEric)
        self.test_priority_queue.add_to_priority_queue(self.studentNathan)
        self.test_priority_queue.add_to_priority_queue(self.studentPaul)
        self.test_priority_queue.add_to_priority_queue(self.studentChris)
        self.test_priority_queue.add_to_priority_queue(self.studentBob)
        self.test_priority_queue.add_to_priority_queue(self.studentLarissa)
        self.test_priority_queue.add_to_priority_queue(self.studentMark)
        self.test_priority_queue.add_to_priority_queue(self.studentHeath)
        self.test_priority_queue.add_to_priority_queue(self.studentSarah)
        self.test_priority_queue.add_to_priority_queue(self.studentAshley)
        self.test_priority_queue.add_to_priority_queue(self.studentRyan)
        self.test_priority_queue.add_to_priority_queue(self.studentJake)
        self.test_priority_queue.add_to_priority_queue(self.studentDrake)
        self.test_priority_queue.add_to_priority_queue(self.studentBlake)
        self.assertListEqual(self.test_priority_queue.get_all_data_from_priority_queue(),
            [self.studentRyan, self.studentPaul, self.studentAshley,
            self.studentChris,self.studentSarah, self.studentLarissa,
            self.studentEric, self.studentDavid, self.studentHeath,
            self.studentNathan, self.studentMark, self.studentBob,
            self.studentJake, self.studentDrake, self.studentBlake])

    def test_student_add_to_priority_queue_size_check(self):
        """
        This unit test is testing the PriorityQueue class definition 'add_to_priority_queue'.
        This test goes and increments the size and ensures that whenever an object is added to the priority queue
        that the length is growing by an index of 1. The number of iterations can be determined by
        adjusting the 'number_of_students_to_add'variable.
        :return:
        """
        number_of_students_to_add = 5
        self.test_priority_queue.set_priority_strategy(PriorityClass.student)
        for index in range(number_of_students_to_add):
            self.test_priority_queue.add_to_priority_queue(self.studentDavid)

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
        self.test_priority_queue.set_priority_strategy(PriorityClass.student)
        self.test_priority_queue.add_to_priority_queue(self.studentDavid)
        self.test_priority_queue.add_to_priority_queue(self.studentEric)
        self.test_priority_queue.add_to_priority_queue(self.studentNathan)
        self.test_priority_queue.add_to_priority_queue(self.studentPaul)
        self.test_priority_queue.add_to_priority_queue(self.studentChris)
        self.test_priority_queue.add_to_priority_queue(self.studentBob)
        self.test_priority_queue.add_to_priority_queue(self.studentLarissa)
        self.test_priority_queue.add_to_priority_queue(self.studentMark)
        self.test_priority_queue.add_to_priority_queue(self.studentHeath)
        self.test_priority_queue.add_to_priority_queue(self.studentSarah)
        self.test_priority_queue.add_to_priority_queue(self.studentAshley)
        self.test_priority_queue.add_to_priority_queue(self.studentRyan)
        self.test_priority_queue.add_to_priority_queue(self.studentJake)
        self.test_priority_queue.add_to_priority_queue(self.studentDrake)
        self.test_priority_queue.add_to_priority_queue(self.studentBlake)
        self.test_priority_queue.remove_top_priority_from_priority_queue()
        self.assertEqual(self.test_priority_queue.get_data_from_priority_queue_index(0), self.studentAshley)

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

        self.test_priority_queue.set_priority_strategy(PriorityClass.student)
        for student in range(number_of_students_to_add):
            self.test_priority_queue.add_to_priority_queue(self.studentDavid)

        for student in range(number_of_students_to_remove):
            self.test_priority_queue.remove_top_priority_from_priority_queue()

        self.assertEquals(number_of_students_to_add-number_of_students_to_remove,len(self.test_priority_queue.get_all_data_from_priority_queue()))


    def test_iter_next_def(self):
        """
        This unit test is testing the __iter__ of a 'PriorityQueue' object. It passes when the '__priority_queue' list
        and all of its elements are iterated upon via the __next__ definition. Each of the iterations must be with the
        highest priority.
        :return:
        """
        self.test_priority_queue.set_priority_strategy(PriorityClass.node)
        int_one_node = NodeClass.Node(1)
        int_two_node = NodeClass.Node(2)
        int_three_node = NodeClass.Node(3)
        int_four_node = NodeClass.Node(4)

        self.test_priority_queue.add_to_priority_queue(int_one_node)
        self.test_priority_queue.add_to_priority_queue(int_two_node)
        self.test_priority_queue.add_to_priority_queue(int_three_node)
        self.test_priority_queue.add_to_priority_queue(int_four_node)

        iter_priority = self.test_priority_queue.__iter__()

        self.assertEquals(iter_priority.__next__()[1], int_four_node.node_data)
        self.assertEquals(iter_priority.__next__()[1], int_three_node.node_data)
        self.assertEquals(iter_priority.__next__()[1], int_two_node.node_data)
        self.assertEquals(iter_priority.__next__()[1], int_one_node.node_data)

    def test_str_def(self):
        """
        This unit test is testing the 'str' def of the 'PriorityQueue' class. It passes when upon proceeding with the
        __str__() def that the '__priority_queue' list is being passed to it.
        :return:
        """
        self.test_priority_queue.add_to_priority_queue(1)
        self.assertEquals(self.test_priority_queue.__str__(), "['[1, 1]']" )

        self.test_priority_queue.add_to_priority_queue(2)
        self.assertEquals(self.test_priority_queue.__str__(), "['[2, 2]', '[1, 1]']" )

        self.test_priority_queue.add_to_priority_queue(3)
        self.assertEquals(self.test_priority_queue.__str__(), "['[3, 3]', '[1, 1]', '[2, 2]']")


if __name__ == '__main__':
    unittest.main()


