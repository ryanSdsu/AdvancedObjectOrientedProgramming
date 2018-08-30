#Class definition reference
#https://stackoverflow.com/questions/9195455/how-to-document-a-method-with-parameters
#Variable names reference
#https://www.python.org/dev/peps/pep-0008/#class-names

class Student:
    """This is the base class for all students"""
    def __init__(self, name, redId, email, address, gpa, numberOfUnitsTaken):
        """
        Constructor
        :param str name: The name of the student
        :param str redId: The redID of the student
        :param str email: The email of the student
        :param str address: The address of the student
        :param float gpa: The gpa of the student, must be between 0 and 4.0
        :param int numberOfUnitsTaken: The number of units that the student has taken, must be between 0 and 150
        """
        self.name = str(name)
        self.redId = str(redId)
        self.email = str(email)
        self.address = str(address)
        if gpa >= 0 and gpa <= 4.0:
            self.gpa = float(gpa) #The gpa must be between 0 and 4.0
        if numberOfUnitsTaken >= 0 and numberOfUnitsTaken <= 150:
            self.numberOfUnitsTaken = int(numberOfUnitsTaken) #The number of units taken must be between 0 and 150
        self.studentPriority = float(0.7*self.numberOfUnitsTaken + 0.3*self.gpa)

studentOne = Student("Nate", "777777777", "Nate@aol.com", "134 Home St", 4.0, 150)
print(studentOne.name)
print(studentOne.redId)
print(studentOne.email)
print(studentOne.address)
print(studentOne.gpa)
print(studentOne.numberOfUnitsTaken)
print(studentOne.studentPriority)