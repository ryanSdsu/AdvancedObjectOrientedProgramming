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
        self.rootObjectCurrentIndex = len(self.priorityQueue) - 1
        newObjectParentLocation = self.rootObjectCurrentIndex >> 1

        # If the newly added object has parents we can now check the 'studentPriority'.
        # If the newly added objects 'studentPriority' is lower than that of it's parents, we will traverse it upwards
        # on the priority queue by swapping their locations.
        while (newObjectParentLocation > 0):
            if studentObject.studentPriority > self.priorityQueue[newObjectParentLocation].studentPriority:
                self.swapObjectIndexInPriorityQueue(newObjectParentLocation, self.rootObjectCurrentIndex, newObjectParentLocation)
                newObjectParentLocation = newObjectParentLocation >> 1
            else:
                newObjectParentLocation = newObjectParentLocation >> 1
        return self.priorityQueue

    def printPriorityQueue(self):
        """
        This definition prints out the objects in the 'priorityQueue' via priority order, displaying the name and redId.
        :return: the last student name and redId
        :rtype: str
        """
        iteratorPriorityQueue = iter(self.priorityQueue)
        next(iteratorPriorityQueue)
        for studentObject in iteratorPriorityQueue:
            student = studentObject.name + " " + studentObject.redId
            print(student)
        return student

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
        # anything else that is bigger than 4 has more.
        self.rootObjectCurrentIndex = 1
        childOfRootObject = self.rootObjectCurrentIndex + 1
        if len(self.priorityQueue) == 3:
            #If the child is greater than the parent
            if self.priorityQueue[childOfRootObject].studentPriority > self.priorityQueue[self.rootObjectCurrentIndex].studentPriority:
                self.swapObjectIndexInPriorityQueue(self.rootObjectCurrentIndex, childOfRootObject, self.rootObjectCurrentIndex)

        while len(self.priorityQueue) >= 4:
            #Check if there is a left or right child
            if self.rootObjectCurrentIndex * 2 <= len(self.priorityQueue) - 1:
                leftChild = self.rootObjectCurrentIndex * 2
            else:
                leftChild = False
            if self.rootObjectCurrentIndex * 2 + 1 <= len(self.priorityQueue) - 1:
                rightChild = self.rootObjectCurrentIndex * 2 + 1
            else:
                rightChild = False

            #If there are 2 children present under the parent node we can now check their 'studentPriority'
            if leftChild and rightChild:
                #If the left or right child is greater than the parent, proceed to check the left child.
                if self.priorityQueue[leftChild].studentPriority or self.priorityQueue[rightChild].studentPriority > \
                        self.priorityQueue[self.rootObjectCurrentIndex].studentPriority:
                    #If the left child is greater than the right child, swap the parent and and left child.
                    if self.priorityQueue[leftChild].studentPriority > self.priorityQueue[rightChild].studentPriority:
                        self.swapObjectIndexInPriorityQueue(leftChild, self.rootObjectCurrentIndex, leftChild)
                    #Otherwise if the right child is greater, swap the parent and and right child.
                    else:
                        self.swapObjectIndexInPriorityQueue(rightChild, self.rootObjectCurrentIndex, rightChild)
                else:
                    return self.priorityQueue
            elif leftChild and rightChild == False:
                #If the left child is greater than the parent, swap the parent and the left child
                if self.priorityQueue[leftChild].studentPriority > self.priorityQueue[self.rootObjectCurrentIndex].studentPriority:
                    self.swapObjectIndexInPriorityQueue(leftChild, self.rootObjectCurrentIndex, leftChild)
                else:
                    return self.priorityQueue
            else:
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

    def swapObjectIndexInPriorityQueue(self, objectOneIndex, objectTwoIndex, updatedRootObjectIndex):
        """
        This swaps the indexes of two objects within the priorityQueue and updates the index of the current root object.
        :param int objectOneIndex: The index of one location in the priorityQueue
        :param int objectTwoIndex: The index of another location in the priorityQueue
        :param int rootObjectCurrentPosition: The new index of the root Object
        :return: priorityQueue
        :rtype: []
        """
        tempObject = self.priorityQueue[objectOneIndex]
        self.priorityQueue[objectOneIndex] = self.priorityQueue[objectTwoIndex]
        self.priorityQueue[objectTwoIndex] = tempObject
        self.rootObjectCurrentIndex = updatedRootObjectIndex
        return self.priorityQueue