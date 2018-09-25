import unittest
from Assignment_Two import PriorityQueueClass
from Assignment_Two import PriorityClass
from Assignment_Two import StudentClass

class TestPriorityClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Priority Class"""
    def setUp(self):
        """
        This is the set up for the 'Priority' class. We are creating the 'PriorityQueue' to be used later.
        We are also creating instances of the 'StudentClass' via student objects which are set to be added
        and tested.
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

        self.test_priority_queue.set_priority_strategy(PriorityClass.student)
        self.assertEquals(self.test_priority_queue.get_priority_strategy(), PriorityClass.student)
        self.test_priority_queue.set_priority_strategy(PriorityClass.default)
        self.assertEquals(self.test_priority_queue.get_priority_strategy(), PriorityClass.default)

    def test_student_priority(self):
        """
        This unit test is testing the 'student' strategy of the 'Priority' class. It passes when
        the strategy 'student' is set via the 'PriorityQueue' class and when a student object is
        added to the queue, the correct calculations for the priority should occur.
        :return:
        """

        self.test_priority_queue.set_priority_strategy(PriorityClass.student)
        student = StudentClass.Student("Nathan", 777777777, "Nate@aol.com", "134 Home St", 3.0, 75)
        self.test_priority_queue.add_to_priority_queue(student)
        self.assertEquals(self.test_priority_queue.get_priority_strategy(), PriorityClass.student)
        self.assertEquals(self.test_priority_queue.get_priority_from_priority_queue_index(0), 0.575)

if __name__ == '__main__':
    unittest.main()


