#Class definition reference
#https://stackoverflow.com/questions/9195455/how-to-document-a-method-with-parameters
#Variable names reference
#https://www.python.org/dev/peps/pep-0008/#class-names

class Student:
    """This is the base class for all students"""
    def __init__(self, name, redId, email, address, gpa=None, numberOfUnitsTaken=None):
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

        try:
            #Attempt to create gpa for the student
            if gpa >= 0 and gpa <= 4.0: #The gpa must be between 0 and 4.0
                self.gpa = float(gpa)
            self.gpa
        except AttributeError:
            print("The gpa of {} is not between 0 and 4.0.".format(self.name))
        except TypeError:
            print("The gpa is not an actual number.".format(self.name))

        try:
            #Attempt to create numberOfUnits taken for the student
            if numberOfUnitsTaken >= 0 and numberOfUnitsTaken <= 150: #The number of units taken must be between 0 and 150
                self.numberOfUnitsTaken = int(numberOfUnitsTaken)
            self.numberOfUnitsTaken
        except AttributeError:
            print("The number of units taken from {} is not between 0 and 150.".format(self.name))
        except TypeError:
            print("The number of units taken is not an actual number.".format(self.name))

        try:
            #Attempt to create studentPriority for the student
            if self.gpa and self.numberOfUnitsTaken: #Both the gpa and number of units taken must be valid
                self.studentPriority = float(0.7*self.numberOfUnitsTaken + 0.3*self.gpa)
        except AttributeError:
            print("Both the gpa and number of units taken for {} are not valid.".format(self.name))


studentOne = Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, 150)
