from Assignment_One import StudentClass


class PriorityQueue:
    """This is the base class for the Priority Queue, the main structure is a max heap"""

    def __init__(self):
        """
        This is the constructor for the PriorityQueue class.
        The initial 'None' ensures that students being added to the list start on index 1
        """
        self.priorityQueue = [None]

    def addNewObject(self, studentObject=StudentClass.Student):
        """
        This is where we add a new object into the priorityQueue.  The main structure is a max heap therefore
        all of the objects being added must traverse to the top of the list based on the highest priority. As a
        reminder the parents of each newly added object in a max heap is the "floor" of the index / 2.
        :param StudentClass.Student studentObject:
        :return: priorityQueue
        :rtype: []
        """

        # To begin we will confirm if the newly added object has any "parents".
        # Since the parents location of the newly added object is the "floor" of the newly added objects index / 2,
        # we can simply compute this by shifting the bits of the newly added objects index to the right.
        self.priorityQueue.append(studentObject)
        newObjectLocation = len(self.priorityQueue) - 1
        newObjectParentLocation = newObjectLocation >> 1

        # If the newly added object has parents we can now check the 'studentPriority'.
        # If the newly added objects 'studentPriority' is lower than that of it's parents, we will traverse it upwards
        # on the priority queue by swapping their locations.
        while (newObjectParentLocation > 0):
            if studentObject.studentPriority > self.priorityQueue[newObjectParentLocation].studentPriority:
                swapTemp = self.priorityQueue[newObjectParentLocation]
                self.priorityQueue[newObjectParentLocation] = studentObject
                self.priorityQueue[newObjectLocation] = swapTemp
                newObjectLocation = newObjectParentLocation
                newObjectParentLocation = newObjectParentLocation >> 1
            else:
                newObjectParentLocation = newObjectParentLocation >> 1
        return self.priorityQueue

    def returnHighestPriorityElement(self):
        print("Here is the highest element")

    def removeHighestElement(self):
        print("Removing the highest element")


#Unit Test for addNewObject
studentDavid = StudentClass.Student("David", "111111111", "David@aol.com", "134 Yolo St", 2.0, 75)
studentEric = StudentClass.Student("Eric", "777777777", "Nate@aol.com", "134 Home St", 3.0, 100)
studentNathan = StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 3.5, 120)
studentPaul = StudentClass.Student("Paul", "777777777", "Nate@aol.com", "134 Home St", 3.8, 148)
studentChris = StudentClass.Student("Chris", "777777777", "Nate@aol.com", "134 Home St", 3.6, 121)
studentBob = StudentClass.Student("Bob", "777777777", "Nate@aol.com", "134 Home St", 2.5, 7.6)
studentLarissa = StudentClass.Student("Larissa", "777777777", "Nate@aol.com", "134 Home St", 3.25, 110)
studentMark = StudentClass.Student("Mark", "777777777", "Nate@aol.com", "134 Home St", 3.65, 122)
studentHeath = StudentClass.Student("Heath", "777777777", "Nate@aol.com", "134 Home St", 0, 0)
studentSarah = StudentClass.Student("Sarah", "777777777", "Nate@aol.com", "134 Home St", 3.7, 123)
studentAshley = StudentClass.Student("Ashley", "777777777", "Nate@aol.com", "134 Home St", 3.9, 149)
studentRyan = StudentClass.Student("Ryan", "777777777", "Nate@aol.com", "134 Home St", 4, 150)
studentJake = StudentClass.Student("Jake", "777777777", "Nate@aol.com", "134 Home St", 1, 1)
studentDrake = StudentClass.Student("Drake", "777777777", "Nate@aol.com", "134 Home St", 1, 1)
studentBlake = StudentClass.Student("Blake", "777777777", "Nate@aol.com", "134 Home St", 1, 1)

myPriorityQueue = PriorityQueue()
myPriorityQueue.addNewObject(studentDavid)
myPriorityQueue.addNewObject(studentEric)
myPriorityQueue.addNewObject(studentNathan)
myPriorityQueue.addNewObject(studentPaul)
myPriorityQueue.addNewObject(studentChris)
myPriorityQueue.addNewObject(studentBob)
myPriorityQueue.addNewObject(studentLarissa)
myPriorityQueue.addNewObject(studentMark)
myPriorityQueue.addNewObject(studentHeath)
myPriorityQueue.addNewObject(studentSarah)
myPriorityQueue.addNewObject(studentAshley)
myPriorityQueue.addNewObject(studentRyan)
myPriorityQueue.addNewObject(studentJake)
myPriorityQueue.addNewObject(studentDrake)
myPriorityQueue.addNewObject(studentBlake)

for idx in range(1, 16):
    print(myPriorityQueue.priorityQueue[idx].name)

