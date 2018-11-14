import unittest
import io
from contextlib import redirect_stdout
from Assignment_One import PriorityQueueClass
from Assignment_One import StudentClass

class TestPriorityQueueClass(unittest.TestCase):

    def setUp(self):
        """
        This sets up the instances of the 'StudentClass' via student objects which are set to be added and tested via
        the 'PriorityQueueClass'.
        :return:
        """
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


    def test_Constructor(self):
        """
        This unit test is testing the instantiation of the 'PriorityQueue' object based on the 'PriorityQueueClass' via the
        default constructor (there are no arguments).
        :return:
        """
        cs635PriorityQueue = PriorityQueueClass.PriorityQueue()
        self.assertIsInstance(cs635PriorityQueue, PriorityQueueClass.PriorityQueue)

    def test_addNewObject(self):
        """
        This unit test is testing the PriorityQueue class definition 'addNewObject'.  This test passes if all 15 'student'
        objects which were instantiated in the 'setUp' definition are successfully added to the 'priorityQueue' and are in
        priority order.
        :return:
        """
        cs635PriorityQueue = PriorityQueueClass.PriorityQueue()
        cs635PriorityQueue.addNewObject(self.studentDavid)
        cs635PriorityQueue.addNewObject(self.studentEric)
        cs635PriorityQueue.addNewObject(self.studentNathan)
        cs635PriorityQueue.addNewObject(self.studentPaul)
        cs635PriorityQueue.addNewObject(self.studentChris)
        cs635PriorityQueue.addNewObject(self.studentBob)
        cs635PriorityQueue.addNewObject(self.studentLarissa)
        cs635PriorityQueue.addNewObject(self.studentMark)
        cs635PriorityQueue.addNewObject(self.studentHeath)
        cs635PriorityQueue.addNewObject(self.studentSarah)
        cs635PriorityQueue.addNewObject(self.studentAshley)
        cs635PriorityQueue.addNewObject(self.studentRyan)
        cs635PriorityQueue.addNewObject(self.studentJake)
        cs635PriorityQueue.addNewObject(self.studentDrake)
        cs635PriorityQueue.addNewObject(self.studentBlake)
        self.assertListEqual(cs635PriorityQueue.priorityQueue, [None, self.studentRyan, self.studentPaul, self.studentAshley,
                                                                self.studentChris,self.studentSarah, self.studentLarissa,
                                                                self.studentEric, self.studentDavid, self.studentHeath,
                                                                self.studentNathan, self.studentMark, self.studentBob,
                                                                self.studentJake, self.studentDrake, self.studentBlake])

    def test_addNewObjectPriorityQueueSizeCheck(self):
        """
        This unit test is testing the PriorityQueue class definition 'addNewObject'.  This test goes and increments the
        size and ensures that whenever an object is added to the 'priorityQueue' that the length of the 'priorityQueue'
        is growing by an index of 1. The number of iterations can be determined by adjusting the 'numberOfStudentsToAdd'
        variable.
        :return:
        """
        numberOfStudentsToAdd = 5
        cs635PriorityQueue = PriorityQueueClass.PriorityQueue()

        for index in range(numberOfStudentsToAdd):
            cs635PriorityQueue.addNewObject(self.studentDavid)

        lengthOfPriotityQueue = len(cs635PriorityQueue.priorityQueue) - 1

        self.assertEquals(numberOfStudentsToAdd, lengthOfPriotityQueue)

    def test_printPriorityQueue(self):
        """
        This unit test is testing the PriorityQueue class definition 'printPriorityQueue'.  This test passes
        if all 15 'student' objects which were instantiated in the 'setUp' definition are successfully added to the
        'priorityQueue' and then the 'student' objects are printed/stored into a list which is compared to the
        original 'priorityQueue' once the definition 'printPriorityQueue' is called.
        :return:
        """
        cs635PriorityQueue = PriorityQueueClass.PriorityQueue()
        cs635PriorityQueue.addNewObject(self.studentDavid)
        cs635PriorityQueue.addNewObject(self.studentEric)
        cs635PriorityQueue.addNewObject(self.studentNathan)
        cs635PriorityQueue.addNewObject(self.studentPaul)
        cs635PriorityQueue.addNewObject(self.studentChris)
        cs635PriorityQueue.addNewObject(self.studentBob)
        cs635PriorityQueue.addNewObject(self.studentLarissa)
        cs635PriorityQueue.addNewObject(self.studentMark)
        cs635PriorityQueue.addNewObject(self.studentHeath)
        cs635PriorityQueue.addNewObject(self.studentSarah)
        cs635PriorityQueue.addNewObject(self.studentAshley)
        cs635PriorityQueue.addNewObject(self.studentRyan)
        cs635PriorityQueue.addNewObject(self.studentJake)
        cs635PriorityQueue.addNewObject(self.studentDrake)
        cs635PriorityQueue.addNewObject(self.studentBlake)

        with io.StringIO() as buffer, redirect_stdout(buffer):
            cs635PriorityQueue.printPriorityQueue()
            lastPrintStatement = buffer.getvalue()

        namesAndRedIdsOfPrintStatement = lastPrintStatement.splitlines()
        namesAndRedIdsOfPriorityQueue = []
        for student in cs635PriorityQueue.priorityQueue[1:]:
            namesAndRedIdsOfPriorityQueue.append("{} {}".format(student.name, student.red_id))

        self.assertListEqual(namesAndRedIdsOfPrintStatement, namesAndRedIdsOfPriorityQueue)

    def test_removeHighestPriorityObject(self):
        """
        This unit test is testing the PriorityQueue class definition 'removeHighestPriorityObject'.  This test passes
        if all 15 'student' objects which were instantiated in the 'setUp' definition are successfully added to the
        'priorityQueue' and then the 'student' object Ryan is removed once the definition 'removeHighestPriorityObject'
        is called. The 'priorityQueue' must maintain priority order at all times with the 'student' object having the
        highest priority be on the top of the list since the structure is based on a max heap.
        :return:
        """
        cs635PriorityQueue = PriorityQueueClass.PriorityQueue()
        cs635PriorityQueue.addNewObject(self.studentDavid)
        cs635PriorityQueue.addNewObject(self.studentEric)
        cs635PriorityQueue.addNewObject(self.studentNathan)
        cs635PriorityQueue.addNewObject(self.studentPaul)
        cs635PriorityQueue.addNewObject(self.studentChris)
        cs635PriorityQueue.addNewObject(self.studentBob)
        cs635PriorityQueue.addNewObject(self.studentLarissa)
        cs635PriorityQueue.addNewObject(self.studentMark)
        cs635PriorityQueue.addNewObject(self.studentHeath)
        cs635PriorityQueue.addNewObject(self.studentSarah)
        cs635PriorityQueue.addNewObject(self.studentAshley)
        cs635PriorityQueue.addNewObject(self.studentRyan)
        cs635PriorityQueue.addNewObject(self.studentJake)
        cs635PriorityQueue.addNewObject(self.studentDrake)
        cs635PriorityQueue.addNewObject(self.studentBlake)
        cs635PriorityQueue.removeHighestPriorityObject()
        self.assertListEqual(cs635PriorityQueue.priorityQueue, [None, self.studentAshley, self.studentPaul, self.studentLarissa,
                                                                self.studentChris,self.studentSarah, self.studentBob,
                                                                self.studentEric, self.studentDavid, self.studentHeath,
                                                                self.studentNathan, self.studentMark, self.studentBlake,
                                                                self.studentJake, self.studentDrake])

    def test_removeHighestPriorityObjectQueueSizeCheck(self):
        """
        This unit test is testing the PriorityQueue class definition 'removeHighestPriorityObject'.  This test passes
        if a fixed number of 'student' objects which were instantiated in the 'setUp' definition are successfully
        added to the 'priorityQueue' and then a specified number are removed once the definition
        'removeHighestPriorityObject' is called. The number of iterations that the definition 'removeHighestPriorityQueue'
        is called is based on the 'numberOfStudentsToRemove' variable.
        :return:
        """
        cs635PriorityQueue = PriorityQueueClass.PriorityQueue()

        numberOfStudentsToAdd = 15
        numberOfStudentsToRemove = 10

        for student in range(numberOfStudentsToAdd):
            cs635PriorityQueue.addNewObject(self.studentDavid)

        for student in range(numberOfStudentsToRemove):
            cs635PriorityQueue.removeHighestPriorityObject()

        self.assertEquals(numberOfStudentsToAdd-numberOfStudentsToRemove,len(cs635PriorityQueue.priorityQueue)-1)

    def test_returnHighestPriorityObject(self):
        """
        This unit test is testing the PriorityQueue class definition 'returnHighestPriorityObject'. This test passes
        if all 15 'student' objects which were instantiated in the 'setUp' definition are successfully added to the
        'priorityQueue' and then the 'student' object Ryan (which has the highest 'studentPriority') is returned
        once the definition 'returnHighestPriorityObject' is called.
        :return:
        """
        cs635PriorityQueue = PriorityQueueClass.PriorityQueue()
        cs635PriorityQueue.addNewObject(self.studentDavid)
        cs635PriorityQueue.addNewObject(self.studentEric)
        cs635PriorityQueue.addNewObject(self.studentNathan)
        cs635PriorityQueue.addNewObject(self.studentPaul)
        cs635PriorityQueue.addNewObject(self.studentChris)
        cs635PriorityQueue.addNewObject(self.studentBob)
        cs635PriorityQueue.addNewObject(self.studentLarissa)
        cs635PriorityQueue.addNewObject(self.studentMark)
        cs635PriorityQueue.addNewObject(self.studentHeath)
        cs635PriorityQueue.addNewObject(self.studentSarah)
        cs635PriorityQueue.addNewObject(self.studentAshley)
        cs635PriorityQueue.addNewObject(self.studentRyan)
        cs635PriorityQueue.addNewObject(self.studentJake)
        cs635PriorityQueue.addNewObject(self.studentDrake)
        cs635PriorityQueue.addNewObject(self.studentBlake)
        self.assertEqual(cs635PriorityQueue.returnHighestPriorityObject(), self.studentRyan)

    def test_swapObjectIndexInPriorityQueue(self):
        """
        This unit test is testing the PriorityQueue class definition 'swapObjectIndexInPriorityQueue'. This test passes
        if 2 of 'student' objects (David and Eric) which were instantiated in the 'setUp' definition are successfully added to the
        'priorityQueue' and then they swap places once the definition 'swapObjectIndexInPriorityQueue' is called.
        :return:
        """
        cs635PriorityQueue = PriorityQueueClass.PriorityQueue()
        cs635PriorityQueue.addNewObject(self.studentEric)
        indexEric = len(cs635PriorityQueue.priorityQueue) - 1
        cs635PriorityQueue.addNewObject(self.studentDavid)
        indexDavid =len(cs635PriorityQueue.priorityQueue) - 1
        cs635PriorityQueue.traverseObjectIndexInPriorityQueue(indexDavid, indexEric, indexDavid)
        self.assertListEqual(cs635PriorityQueue.priorityQueue, [None, self.studentDavid, self.studentEric])

if __name__ == '__main__':
    unittest.main()


