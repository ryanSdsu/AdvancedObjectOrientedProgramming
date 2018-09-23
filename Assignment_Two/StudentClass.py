class Student:
    """This is the base class for all students."""

    def __init__(self, name, red_id, email, address, gpa=None, number_of_units_taken=None):
        """
        This is the constructor for the Student class.
        :param str name: The name of the student
        :param int red_id: The red_id of the student
        :param str email: The email of the student
        :param str address: The address of the student
        :param float gpa: The gpa of the student, must be between 0 and 4.0
        :param int number_of_units_taken: The number of units that the student has taken, must be between 0 and 150
        """
        try:
            if name.isalpha():
                self.__name = name
        except AttributeError:
            raise AttributeError("A student name can only contain letters.")

        try:
            if int(red_id):
                self.__red_id = red_id
        except ValueError:
            raise ValueError("A student red ID can only contain numbers.")

        try:
            if "@" in str(email):
                self.__email = email
            self.__email
        except TypeError:
            raise TypeError("A student email must be in a string format.")
        except AttributeError:
            raise AttributeError("A student email must be in a string format containing a '@' .")

        try:
            if str(address):
                check_for_numbers = any(character.isdigit() for character in address)
                if check_for_numbers == True:
                    self.__address = address
                else:
                    raise ValueError("A student address must have both the number and name of street.")
        except AttributeError:
            raise AttributeError("A student address must be in a string format.")
        except ValueError:
            raise ValueError("A student address must have both the number and name of street.")

        try:
            if gpa >= 0 and gpa <= 4.0:
                self.__gpa = float(gpa)
            self.__gpa
        except AttributeError:
            raise AttributeError("The gpa of {} is not between 0 and 4.0.".format(self.name))
        except TypeError:
            raise TypeError("The gpa is not an actual number.")

        try:
            if number_of_units_taken >= 0 and number_of_units_taken <= 150:
                self.__number_of_units_taken = int(number_of_units_taken)
            self.__number_of_units_taken
        except AttributeError:
            raise  AttributeError("The number of units taken from {} is not between 0 and 150.".format(self.name))
        except TypeError:
            raise TypeError("The number of units taken is not an actual number.")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        try:
            if new_name.isalpha():
                self.__name = new_name
        except AttributeError:
            raise AttributeError("A student name can only contain letters.")

    @property
    def red_id(self):
        return self.__red_id

    @red_id.setter
    def red_id(self, new_red_id):
        try:
            if int(new_red_id):
                self.__red_id = new_red_id
        except ValueError:
            print("A student red ID can only contain numbers.")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        try:
            if "@" in str(new_email):
                self.__email = new_email
            self.__email
        except TypeError:
            raise TypeError("A student email must be in a string format.")
        except AttributeError:
            raise AttributeError("A student email must be in a string format containing a '@' .")

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        try:
            if str(new_address):
                check_for_numbers = any(character.isdigit() for character in new_address)
                if check_for_numbers == True:
                    self.__address = new_address
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
    def gpa(self, new_gpa):
        try:
            if new_gpa >= 0 and new_gpa <= 4.0:
                self.__gpa = float(new_gpa)
        except AttributeError:
            raise AttributeError("The gpa of {} is not between 0 and 4.0.".format(self.name))
        except TypeError:
            raise TypeError("The gpa is not an actual number.")

    @property
    def number_of_units_taken(self):
        return self.__number_of_units_taken

    @number_of_units_taken.setter
    def number_of_units_taken(self, new_number_of_units_taken):
        try:
            if new_number_of_units_taken >= 0 and new_number_of_units_taken <= 150:
                self.__number_of_units_taken = int(new_number_of_units_taken)
        except AttributeError:
            raise  AttributeError("The number of units taken from {} is not between 0 and 150.".format(self.name))
        except TypeError:
            raise TypeError("The number of units taken is not an actual number.")

    def __str__(self):
        return "Red ID: {} Name: {}".format(self.red_id, self.name)
