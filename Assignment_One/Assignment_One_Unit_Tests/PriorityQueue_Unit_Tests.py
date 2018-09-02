from Assignment_One import PriorityQueueClass
from Assignment_One import StudentClass

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

myPriorityQueue = PriorityQueueClass.PriorityQueue()
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
studentB = StudentClass.Student("B", "277777777", "Nate@aol.com", "134 Home St", 1.1, 15)
studentC = StudentClass.Student("C", "377777777", "Nate@aol.com", "134 Home St", 1.2, 20)
studentD = StudentClass.Student("D", "477777777", "Nate@aol.com", "134 Home St", 1.3, 25)
studentE = StudentClass.Student("E", "577777777", "Nate@aol.com", "134 Home St", 1.4, 30)
studentF = StudentClass.Student("F", "677777777", "Nate@aol.com", "134 Home St", 1.5, 35)
studentG = StudentClass.Student("G", "777777777", "Nate@aol.com", "134 Home St", 1.6, 40)
studentH = StudentClass.Student("H", "877777777", "Nate@aol.com", "134 Home St", 1.7, 45)
studentI = StudentClass.Student("I", "977777777", "Nate@aol.com", "134 Home St", 1.8, 50)
studentJ = StudentClass.Student("J", "107777777", "Nate@aol.com", "134 Home St", 1.9, 55)
studentK = StudentClass.Student("K", "117777777", "Nate@aol.com", "134 Home St", 2.0, 60)
studentL = StudentClass.Student("L", "127777777", "Nate@aol.com", "134 Home St", 2.5, 65)
studentM = StudentClass.Student("M", "137777777", "Nate@aol.com", "134 Home St", 3.0, 70)
studentN = StudentClass.Student("N", "147777777", "Nate@aol.com", "134 Home St", 3.5, 75)
studentO = StudentClass.Student("O", "157777777", "Nate@aol.com", "134 Home St", 4.0, 80)

myPriorityQueue = PriorityQueueClass.PriorityQueue()
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

print("\n")
myPriorityQueue.printPriorityQueue()