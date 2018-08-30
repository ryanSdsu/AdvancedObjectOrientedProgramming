from Assignment_One import StudentClass
from Assignment_One import PriorityQueueClass

studentNathan = StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, 150)
priorityQueue = PriorityQueueClass.PriorityQueue()

print(studentNathan.name)
print(studentNathan.redId)
print(studentNathan.email)
print(studentNathan.address)
print(studentNathan.gpa)
print(studentNathan.numberOfUnitsTaken)
print(studentNathan.studentPriority)

print(priorityQueue.pQueue)