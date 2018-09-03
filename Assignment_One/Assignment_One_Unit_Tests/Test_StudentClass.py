import unittest
from Assignment_One import StudentClass

class TestStudentClass(unittest.TestCase):
    def test_Constructor(self):
        """
        This unit test is testing the instantiation of the 'Student' object based on the 'StudentClass' via the
        default constructor. It passes when the first 4 arguments ('name', 'redId', 'email', 'address') are strings, the
        'gpa' is a number between 0 - 4.0 and 'numberOfUnitsTaken' is a number between 0 - 150.
        :return:
        """
        studentOne = StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, 150)
        self.assertIsInstance(studentOne, StudentClass.Student)

    def test_WrongTypeGpa(self):
        """
        This unit test is testing the 'TypeError' check of the 'gpa' variable. It passes when the 'gpa' is set to something
        other than an int or a float which triggers a 'TypeError'.
        :return:
        """
        with self.assertRaises(TypeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", "4.5", 150)

    def test_UpperboundGpa(self):
        """
        This unit test is testing the upper bound of the 'gpa' variable. It passes when the 'gpa' is set to a number
        greater than 4.0, thus raising a 'AttributeError'.
        :return:
        """
        with self.assertRaises(AttributeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.1, 150)

    def test_LowerboundGpa(self):
        """
        This unit test is testing the lower bound of the 'gpa' variable. It passes when the 'gpa' is set to a number
        lower than 4.0, thus raising a 'AttributeError'.
        :return:
        """
        with self.assertRaises(AttributeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", -0.1, 150)

    def test_WrongTypeNumberOfUnitsTaken(self):
        """
        This unit test is testing the 'TypeError' check of the 'numberOfUnitsTaken' variable. It passes when the
        'numberOfUnitsTaken' is set to something other than an int or a float which triggers a 'TypeError'.
        :return:
        """
        with self.assertRaises(TypeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, "150")

    def test_UpperBoundNumberOfUnitsTaken(self):
        """
        This unit test is testing the upper bound of the 'numberOfUnitsTaken' variable. It passes when the
        'numberOfUnitsTaken' is set to a number greater than 150, thus raising a 'AttributeError'.
        :return:
        """
        with self.assertRaises(AttributeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, 151)

    def test_LowerBoundNumberOfUnitsTaken(self):
        """
        This unit test is testing the lower bound of the 'numberOfUnitsTaken' variable. It passes when the
        'numberOfUnitsTaken' is set to a number lower than 0, thus raising a 'AttributeError'.
        :return:
        """
        with self.assertRaises(AttributeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, -0.1)

if __name__ == '__main__':
    unittest.main()