from Assignment_One import StudentClass


class PriorityQueue:
    """This is the base class for the Priority Queue, the main structure is a max heap."""

    def __init__(self):
        """
        This is the constructor for the PriorityQueue class.
        The initial 'None' ensures that students being added to the list start on index 1.
        """
        self.priorityQueue = [None]

    def addNewObject(self, studentObject=StudentClass.Student):
        """
        This is where we add a new object into the 'priorityQueue'.  The main structure is a max heap therefore
        all of the objects being added must traverse to the top of the list based on the highest priority. As a
        reminder the parents of each newly added object in a max heap is the "floor" of the index / 2.
        :param StudentClass.Student studentObject:
        :return: The priorityQueue
        :rtype: []
        """
        # To begin we will confirm if the newly added object has any "parents".
        # Since the parents location of the newly added object is the "floor" of the newly added objects index / 2,
        # we can simply compute this by doing a bit shift to the right.
        self.priorityQueue.append(studentObject)
        self.rootObjectCurrentIndex = len(self.priorityQueue) - 1
        newObjectParentLocation = self.rootObjectCurrentIndex >> 1

        # If the newly added object has parents we can now check the 'studentPriority'.
        # If the newly added objects 'studentPriority' is lower than that of it's parents, we will traverse it upwards
        # on the 'priorityQueue' by swapping their locations.
        while (newObjectParentLocation > 0):
            if studentObject.studentPriority > self.priorityQueue[newObjectParentLocation].studentPriority:
                self.traverseObjectIndexInPriorityQueue(newObjectParentLocation, self.rootObjectCurrentIndex, newObjectParentLocation)
                newObjectParentLocation = newObjectParentLocation >> 1
            else:
                newObjectParentLocation = newObjectParentLocation >> 1
        return self.priorityQueue

    def printPriorityQueue(self):
        """
        This definition prints out the objects in the 'priorityQueue' via priority order, displaying the name and redId.
        :return:
        """
        for studentObject in self.priorityQueue[1:]:
            print("{} {}".format(studentObject.name, studentObject.redId))

    def removeHighestPriorityObject(self):
        """
        This is where we remove the object with the highest 'studentPriority' in the 'priorityQueue'.
        After removing this object we then re-heapify the entire queue in order to ensure that the next
        object with the highest 'studentPriority' is at the top.
        :return: priorityQueue
        :rtype: []
        """
        #If there are no objects in the 'priorityQueue' we will return the 'None' variable in the list.
        if (len(self.priorityQueue) == 1):
            return self.priorityQueue[0]

        #If there is only 1 'student' object ie. the root, we will just remove it.
        if (len(self.priorityQueue) == 2):
            self.priorityQueue.pop()
            return self.priorityQueue

        # In the case of there being at least 2 or more 'student' objects, we will swap the root object with the
        # object that is "last" in the 'priorityQueue' and then remove it.
        if (len(self.priorityQueue) >= 3):
            lastObjectInPriorityQueue = self.priorityQueue.pop()
            self.priorityQueue[1] = lastObjectInPriorityQueue

        # With this completed we now have a new root 'student' object which we will traverse downwards to see if it
        # has any "children".  If it does, we need to traverse downwards should it happen to have a higher
        # 'studentPriority'.  The location of the "children" can be found via index * 2 and index * 2 + 1.
        self.rootObjectCurrentIndex = 1
        childOfRootObject = self.rootObjectCurrentIndex + 1

        if len(self.priorityQueue) == 3:
            # If the child is greater than the parent, we will swap their indexes.
            if self.priorityQueue[childOfRootObject].studentPriority > self.priorityQueue[self.rootObjectCurrentIndex].studentPriority:
                self.traverseObjectIndexInPriorityQueue(self.rootObjectCurrentIndex, childOfRootObject, self.rootObjectCurrentIndex)

        while len(self.priorityQueue) >= 4:
            # First we check to see if the root 'student' object has any children.
            if self.rootObjectCurrentIndex * 2 <= len(self.priorityQueue) - 1:
                leftChild = self.rootObjectCurrentIndex * 2
            else:
                leftChild = False
            if self.rootObjectCurrentIndex * 2 + 1 <= len(self.priorityQueue) - 1:
                rightChild = self.rootObjectCurrentIndex * 2 + 1
            else:
                rightChild = False

            # If there are 2 children present under the parent node we can now check their 'studentPriority'.
            if leftChild and rightChild:
                # If the left or right child is greater than the parent, proceed to check the left child.
                if self.priorityQueue[leftChild].studentPriority or self.priorityQueue[rightChild].studentPriority > \
                        self.priorityQueue[self.rootObjectCurrentIndex].studentPriority:
                    # If the left child is greater than the right child, we will swap the parent and left child indexes.
                    if self.priorityQueue[leftChild].studentPriority > self.priorityQueue[rightChild].studentPriority:
                        self.traverseObjectIndexInPriorityQueue(leftChild, self.rootObjectCurrentIndex, leftChild)
                    # Otherwise if the right child is greater, we will swap the parent and right childs index.
                    else:
                        self.traverseObjectIndexInPriorityQueue(rightChild, self.rootObjectCurrentIndex, rightChild)
                else:
                    return self.priorityQueue
            elif leftChild and rightChild == False:
                # If there is only one child we first check if the only child is greater than the parent,
                # and if this is true we swap the parent and the child.
                if self.priorityQueue[leftChild].studentPriority > self.priorityQueue[self.rootObjectCurrentIndex].studentPriority:
                    self.traverseObjectIndexInPriorityQueue(leftChild, self.rootObjectCurrentIndex, leftChild)
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

    def traverseObjectIndexInPriorityQueue(self, objectOneIndex, objectTwoIndex, updatedRootObjectIndex):
        """
        This traverses an object in the 'priorityQueue' by swapping the indexes of two objects and then updating
        the current root objects index.
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