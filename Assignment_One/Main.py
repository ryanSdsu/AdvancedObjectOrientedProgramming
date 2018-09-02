#Ryan Ragasa
#Red ID: 817560426
#I am currently enrolled in this class => CS 635 Advanced Object-Oriented Design & Programming.

from Assignment_One import StudentClass
from Assignment_One import PriorityQueueClass

studentNathan = StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, 150)
studentDavid = StudentClass.Student("David", "111111111", "David@aol.com", "134 Yolo St", 2.0, 75)
studentEric = StudentClass.Student("Eric", "222222222", "Eric@aol.com", "134 Sky St", 3.4, 20)

priorityQueue = PriorityQueueClass.PriorityQueue()

print("{}'s priority is {}".format(studentNathan, studentNathan.studentPriority))
print("{}'s priority is {}".format(studentDavid, studentDavid.studentPriority))
print("{}'s priority is {}".format(studentEric, studentEric.studentPriority))

print(priorityQueue.pQueue)

priorityQueue.addNewElement(studentNathan)
priorityQueue.pQueue.append(studentDavid)
priorityQueue.pQueue.append(studentEric)

for student in priorityQueue.pQueue:
    print(student.studentPriority)

print(priorityQueue.pQueue)

studentDavi = StudentClass.Student("David", "111111111", "David@aol.com", "134 Yolo St", 2.5, 75)
priorityQueue.addNewElement(studentDavi)

print(priorityQueue.pQueue)

for student in priorityQueue.pQueue:
    print(student.studentPriority)