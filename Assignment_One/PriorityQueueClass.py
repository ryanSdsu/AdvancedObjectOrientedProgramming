from Assignment_One import StudentClass


class PriorityQueue:
    """This is the base class for the Priority Queue, the main structure is a max heap."""

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
        :return: The priorityQueue
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

    def returnHighestPriorityObject(self):
        """
        This returns the highest 'studentPriority' object in the 'priorityQueue' if there is one.
        :return: self.priorityQueue[1]
        :rtype: StudentClass.student
        """
        if len(self.priorityQueue) > 1:
            return self.priorityQueue[1]
        else:
            return self.priorityQueue[0]

    def removeHighestPriorityObject(self):
        """
        This is where we remove the object with the highest 'studentPriority' in the 'priorityQueue'.
        After removing this object we then re-heapify the entire queue in order to ensure that the next
        object on top of the list is the one with the highest 'studentPriority'.
        :return: priorityQueue
        :rtype: []
        """
        #If there are no objects in the 'priorityQueue' we will return the none in the list.
        if (len(self.priorityQueue) == 1):
            return self.priorityQueue[0]


        # To begin we will swap the root object with the one that was last put in the 'priorityQueue' and then remove it.
        # If there is just the root object we will remove it.
        if (len(self.priorityQueue) >= 3):
            lastObjectInPriorityQueue = self.priorityQueue.pop()
            self.priorityQueue[1] = lastObjectInPriorityQueue
        elif (len(self.priorityQueue) == 2):
            self.priorityQueue.pop()


        # Now we need confirm if the new root object has any "children". If so we need to traverse downwards should they
        # happen to have a higher 'studentPriority'. The location of the children can be found via index * 2 and
        # index * 2 + 1. With this in mind, if the length of the 'priorityQueue' is 3 there is only 1 child and
        # anything else that is bigger it has more.
        rootObjectCurrentPosition = 1
        if len(self.priorityQueue) == 3:
            #If the child is greater than the parent
            if self.priorityQueue[rootObjectCurrentPosition + 1].studentPriority > \
                    self.priorityQueue[rootObjectCurrentPosition].studentPriority:
                swapTemp = self.priorityQueue[rootObjectCurrentPosition + 1]
                self.priorityQueue[rootObjectCurrentPosition + 1] = self.priorityQueue[rootObjectCurrentPosition]
                self.priorityQueue[rootObjectCurrentPosition] = swapTemp

        while len(self.priorityQueue) >= 4:
            #Check if there is a left or right child
            if rootObjectCurrentPosition * 2 <= len(self.priorityQueue) - 1:
                leftChild = True
            else:
                leftChild = False
            if rootObjectCurrentPosition * 2 + 1 <= len(self.priorityQueue) - 1:
                rightChild = True
            else:
                rightChild = False

            #If there are 2 children present under the parent node we can now check their 'studentPriority'
            if leftChild and rightChild:
                #If the left or right child is greater than the parent, proceed to check the left child.
                if self.priorityQueue[rootObjectCurrentPosition * 2].studentPriority or \
                                self.priorityQueue[rootObjectCurrentPosition * 2 + 1].studentPriority > \
                                self.priorityQueue[rootObjectCurrentPosition].studentPriority:
                    #If the left child is greater than the right child, swap the parent and and left child.
                    if self.priorityQueue[rootObjectCurrentPosition * 2].studentPriority > \
                            self.priorityQueue[rootObjectCurrentPosition * 2 + 1].studentPriority:
                        swapTemp = self.priorityQueue[rootObjectCurrentPosition * 2]
                        self.priorityQueue[rootObjectCurrentPosition * 2] = self.priorityQueue[rootObjectCurrentPosition]
                        self.priorityQueue[rootObjectCurrentPosition] = swapTemp
                        rootObjectCurrentPosition = rootObjectCurrentPosition * 2
                    #Otherwise if the right child is greater, swap the parent and and right child.
                    else:
                        swapTemp = self.priorityQueue[rootObjectCurrentPosition * 2 + 1]
                        self.priorityQueue[rootObjectCurrentPosition * 2 + 1] = self.priorityQueue[rootObjectCurrentPosition]
                        self.priorityQueue[rootObjectCurrentPosition] = swapTemp
                        rootObjectCurrentPosition = rootObjectCurrentPosition * 2 + 1
                else:
                    return self.priorityQueue
            elif leftChild == True and rightChild == False:
                #If the left child is greater than the parent, swap the parent and the left child
                if self.priorityQueue[rootObjectCurrentPosition * 2].studentPriority > \
                        self.priorityQueue[rootObjectCurrentPosition].studentPriority:
                    swapTemp = self.priorityQueue[rootObjectCurrentPosition * 2]
                    self.priorityQueue[rootObjectCurrentPosition * 2] = self.priorityQueue[rootObjectCurrentPosition]
                    self.priorityQueue[rootObjectCurrentPosition] = swapTemp
                    rootObjectCurrentPosition = rootObjectCurrentPosition * 2
                else:
                    return self.priorityQueue
            else:
                return self.priorityQueue

            leftChild = True
            rightChild = False


#Unit Test for addNewObject and returnHighestPriorityObject
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
print(myPriorityQueue.returnHighestPriorityObject())
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

print(myPriorityQueue.priorityQueue)
myPriorityQueue.priorityQueue.pop()
print(myPriorityQueue.priorityQueue)

print(myPriorityQueue.returnHighestPriorityObject().name)


#Unit Test for removeNewObject
studentA = StudentClass.Student("A", "111111111", "David@aol.com", "134 Yolo St", 1.0, 10)
studentB = StudentClass.Student("B", "777777777", "Nate@aol.com", "134 Home St", 1.1, 15)
studentC = StudentClass.Student("C", "777777777", "Nate@aol.com", "134 Home St", 1.2, 20)
studentD = StudentClass.Student("D", "777777777", "Nate@aol.com", "134 Home St", 1.3, 25)
studentE = StudentClass.Student("E", "777777777", "Nate@aol.com", "134 Home St", 1.4, 30)
studentF = StudentClass.Student("F", "777777777", "Nate@aol.com", "134 Home St", 1.5, 35)
studentG = StudentClass.Student("G", "777777777", "Nate@aol.com", "134 Home St", 1.6, 40)
studentH = StudentClass.Student("H", "777777777", "Nate@aol.com", "134 Home St", 1.7, 45)
studentI = StudentClass.Student("I", "777777777", "Nate@aol.com", "134 Home St", 1.8, 50)
studentJ = StudentClass.Student("J", "777777777", "Nate@aol.com", "134 Home St", 1.9, 55)
studentK = StudentClass.Student("K", "777777777", "Nate@aol.com", "134 Home St", 2.0, 60)
studentL = StudentClass.Student("L", "777777777", "Nate@aol.com", "134 Home St", 2.5, 65)
studentM = StudentClass.Student("M", "777777777", "Nate@aol.com", "134 Home St", 3.0, 70)
studentN = StudentClass.Student("N", "777777777", "Nate@aol.com", "134 Home St", 3.5, 75)
studentO = StudentClass.Student("O", "777777777", "Nate@aol.com", "134 Home St", 4.0, 80)

myPriorityQueue = PriorityQueue()
myPriorityQueue.addNewObject(studentA)
myPriorityQueue.addNewObject(studentB)
myPriorityQueue.addNewObject(studentC)
myPriorityQueue.addNewObject(studentD)
myPriorityQueue.addNewObject(studentE)
myPriorityQueue.addNewObject(studentF)
myPriorityQueue.addNewObject(studentG)
myPriorityQueue.addNewObject(studentH)
myPriorityQueue.addNewObject(studentI)
myPriorityQueue.addNewObject(studentJ)
myPriorityQueue.addNewObject(studentK)
myPriorityQueue.addNewObject(studentL)
myPriorityQueue.addNewObject(studentM)
myPriorityQueue.addNewObject(studentN)
myPriorityQueue.addNewObject(studentO)

print(myPriorityQueue.priorityQueue)
print("\n")

print("Before the removal we have:")
for i in range(1,16):
    print(myPriorityQueue.priorityQueue[i].name)

print("\n")
myPriorityQueue.removeHighestPriorityObject()

print("After the removal we have:")
for i in range(1,15):
    print(myPriorityQueue.priorityQueue[i].name)