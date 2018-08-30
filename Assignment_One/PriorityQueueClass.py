from Assignment_One import StudentClass


class PriorityQueue:

    def __init__(self):
        self.pQueue = []

    def addNewElement(self, studentObject = StudentClass.Student):
        #If the pQueue is empty, append to the pQueue
        if len(self.pQueue) == 0:
            self.pQueue.append(studentObject)
        else:
            #Continuously divide the length of the pQueue by 2 and check to see if the student priority
            #is more or less based on the neighboring student object
            priorityQueueDivider = int(len(self.pQueue)/2) # priorityQueueDivider = 0

            while priorityQueueDivider != -1:
                #Check if the student priority is greater than the current divider position...
                #If so the student will be placed on the left side of the pQueue, else the right side.
                if studentObject.studentPriority >= self.pQueue[priorityQueueDivider].studentPriority:
                    #If the student will be placed on the left side, check the element directly to the left of it...
                    #If the element is less than or equal to that element, the element will be placed there.
                    if studentObject.studentPriority <= self.pQueue[priorityQueueDivider - 1].studentPriority:
                        leftSideOfQueue = self.pQueue[:priorityQueueDivider]
                        leftSideOfQueue.append(studentObject)
                        rightSideOfQueue = self.pQueue[priorityQueueDivider:]
                        self.pQueue = leftSideOfQueue + rightSideOfQueue

                        #stop the program
                        priorityQueueDivider = -1

    def returnHighestPriorityElement(self):
        print("Here is the highest element")

    def removeHighestElement(self):
        print("Removing the highest element")


myPriorityQueue = PriorityQueue()

