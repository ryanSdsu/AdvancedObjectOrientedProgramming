#Questions for Whitney
#Ask about graduation and forms being filled out
#Class definition reference
#https://stackoverflow.com/questions/9195455/how-to-document-a-method-with-parameters
#Variable names reference
#https://www.python.org/dev/peps/pep-0008/#class-names


class Student:
    """This is the base class for all students."""

    def __init__(self, name, redId, email, address, gpa=None, numberOfUnitsTaken=None):
        """
        This is the constructor for the Student class.
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

        # In this try block we will attempt to create the gpa for the student.
        # The gpa must be between 0 and 4.0.
        try:
            if gpa >= 0 and gpa <= 4.0:
                self.gpa = float(gpa)
            self.gpa
        except AttributeError:
            print("The gpa of {} is not between 0 and 4.0.".format(self.name))
        except TypeError:
            print("The gpa is not an actual number.".format(self.name))

        # In this try block we will attempt to create the numberOfUnits taken for the student.
        # The number of units taken must be between 0 and 150.
        try:
            if numberOfUnitsTaken >= 0 and numberOfUnitsTaken <= 150:
                self.numberOfUnitsTaken = int(numberOfUnitsTaken)
            self.numberOfUnitsTaken
        except AttributeError:
            print("The number of units taken from {} is not between 0 and 150.".format(self.name))
        except TypeError:
            print("The number of units taken is not an actual number.".format(self.name))

        # In this try block we will attempt to create the studentPriority for the student.
        # The requirement for this is that total be 70% numberOfUnitsTaken and 30% gpa.
        # In order to do this both the gpa and numberOfUnits variables must have been instantiated.
        try:
            if self.gpa >= 0 and self.numberOfUnitsTaken >= 0:
                self.studentPriority = float(0.7*self.numberOfUnitsTaken + 0.3*self.gpa)
        except AttributeError:
            print("Both the gpa and number of units taken for {} are not valid.".format(self.name))