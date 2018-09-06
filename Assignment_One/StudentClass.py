class Student:
    """This is the base class for all students."""

    def __init__(self, name, redId, email, address, gpa=None, numberOfUnitsTaken=None):
        """
        This is the constructor for the Student class.
        :param str name: The name of the student
        :param int redId: The redID of the student
        :param str email: The email of the student
        :param str address: The address of the student
        :param float gpa: The gpa of the student, must be between 0 and 4.0
        :param int numberOfUnitsTaken: The number of units that the student has taken, must be between 0 and 150
        """

        # In this try block we will attempt to create the name for the student.
        # The name must be a string with no numbers in it.
        try:
            if name.isalpha():
                self.__name = name
        except AttributeError:
            raise AttributeError("A student name can only contain letters.")

        # In this try block we will attempt to create the redId for the student.
        # The redId must be or have only int(s).
        try:
            if int(redId):
                self.__redId = redId
        except ValueError:
            raise ValueError("A student redId can only contain numbers.")

        # In this try block we will attempt to create the address for the student.
        # The address must be a string with a '@' character.
        try:
            if "@" in str(email):
                self.__email = email
            self.__email
        except TypeError:
            raise TypeError("A student email must be in a string format.")
        except AttributeError:
            raise AttributeError("A student email must be in a string format containing a '@' .")

        # In this try block we will attempt to create the address for the student.
        # The address must be a string holding both ints and letters.
        try:
            if str(address):
                checkForNumbers = any(character.isdigit() for character in address)
                if checkForNumbers == True:
                    self.__address = address
                else:
                    raise ValueError("A student address must have both the number and name of street.")
        except AttributeError:
            raise AttributeError("A student address must be in a string format.")
        except ValueError:
            raise ValueError("A student address must have both the number and name of street.")

        # In this try block we will attempt to create the gpa for the student.
        # The gpa must be between 0 and 4.0.
        try:
            if gpa >= 0 and gpa <= 4.0:
                self.__gpa = float(gpa)
        except AttributeError:
            raise AttributeError("The gpa of {} is not between 0 and 4.0.".format(self.name))
        except TypeError:
            raise TypeError("The gpa is not an actual number.".format(self.name))

        # In this try block we will attempt to create the numberOfUnits taken for the student.
        # The number of units taken must be between 0 and 150.
        try:
            if numberOfUnitsTaken >= 0 and numberOfUnitsTaken <= 150:
                self.__numberOfUnitsTaken = int(numberOfUnitsTaken)
        except AttributeError:
            raise  AttributeError("The number of units taken from {} is not between 0 and 150.".format(self.name))
        except TypeError:
            raise TypeError("The number of units taken is not an actual number.".format(self.name))

        # In this try block we will attempt to create the studentPriority for the student.
        # The requirement for this is that total be 70% numberOfUnitsTaken and 30% gpa.
        # In order to do this both the gpa and numberOfUnits variables must have been instantiated.
        try:
            if self.gpa >= 0 and self.numberOfUnitsTaken >= 0:
                self.__studentPriority = float(0.7*self.numberOfUnitsTaken + 0.3*self.gpa)
        except AttributeError:
            raise  AttributeError("Both the gpa and number of units taken for {} are not valid.".format(self.name))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        try:
            if newName.isalpha():
                self.__name = newName
        except AttributeError:
            raise AttributeError("A student name can only contain letters.")

    @property
    def redId(self):
        return self.__redId

    @redId.setter
    def redId(self, newRedId):
        try:
            if int(newRedId):
                self.__redId = newRedId
        except ValueError:
            print("A student redId can only contain numbers.")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, newEmail):
        try:
            if "@" in str(newEmail):
                self.__email = newEmail
            self.__email
        except TypeError:
            raise TypeError("A student email must be in a string format.")
        except AttributeError:
            raise AttributeError("A student email must be in a string format containing a '@' .")

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, newAddress):
        try:
            if str(newAddress):
                checkForNumbers = any(character.isdigit() for character in newAddress)
                if checkForNumbers == True:
                    self.__address = newAddress
                else:
                    raise ValueError("A student address must have both the number and name of street.")
        except AttributeError:
            raise AttributeError("A student address can only be in a string format.")
        except ValueError:
            raise ValueError("A student address must have both the number and name of street.")

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, newGpa):
        try:
            if newGpa >= 0 and newGpa <= 4.0:
                self.__gpa = float(newGpa)
                self.__studentPriority = float(0.7*self.numberOfUnitsTaken + 0.3*self.gpa)
        except AttributeError:
            raise AttributeError("The gpa of {} is not between 0 and 4.0.".format(self.name))
        except TypeError:
            raise TypeError("The gpa is not an actual number.".format(self.name))

    @property
    def numberOfUnitsTaken(self):
        return self.__numberOfUnitsTaken

    @numberOfUnitsTaken.setter
    def numberOfUnitsTaken(self, newNumberOfUnitsTaken):
        try:
            if newNumberOfUnitsTaken >= 0 and newNumberOfUnitsTaken <= 150:
                self.__numberOfUnitsTaken = int(newNumberOfUnitsTaken)
                self.__studentPriority = float(0.7*self.numberOfUnitsTaken + 0.3*self.gpa)
        except AttributeError:
            raise  AttributeError("The number of units taken from {} is not between 0 and 150.".format(self.name))
        except TypeError:
            raise TypeError("The number of units taken is not an actual number.".format(self.name))

    @property
    def studentPriority(self):
        return self.__studentPriority