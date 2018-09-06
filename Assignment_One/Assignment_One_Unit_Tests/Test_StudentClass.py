import unittest
from Assignment_One import StudentClass

class TestStudentClass(unittest.TestCase):

    def test_ChangeAddress(self):
        """
        This unit test is testing the changing of the 'address' variable. It passes when a student's 'address' variable
        is changed by means of its setter and cross-referenced to the 'newDesiredAddress'.
        :return:
        """
        newDesiredAddress = "132 New St."
        studentOne = StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, 150)
        studentOne.address = newDesiredAddress
        self.assertEquals(studentOne.address, newDesiredAddress)

    def test_ChangeEmail(self):
        """
        This unit test is testing the changing of the 'email' variable. It passes when a student's 'email' variable
        is changed by means of its setter and cross-referenced to the 'newDesiredEmail'.
        :return:
        """
        newDesiredEmail = "Nathaniel@aol.com"
        studentOne = StudentClass.Student("Nathan", 777777777, "Nate@aol.com", "134 Home St", 4.0, 150)
        studentOne.email = newDesiredEmail
        self.assertEquals(studentOne.email, newDesiredEmail)

    def test_ChangeGpa(self):
        """
        This unit test is testing the changing of the 'gpa' variable. It passes when a student's 'gpa' variable
        is changed by means of its setter and cross-referenced to the 'newDesiredGpa'.
        :return:
        """
        newDesiredGpa = 3.5
        studentOne = StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, 150)
        studentOne.gpa = newDesiredGpa
        self.assertEquals(studentOne.gpa, newDesiredGpa)

    def test_ChangeName(self):
        """
        This unit test is testing the changing of the 'name' variable. It passes when a student's 'name' variable
        is changed by means of its setter and cross-referenced to the 'newDesiredName'.
        :return:
        """
        newDesiredName = "David"
        studentOne = StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, 150)
        studentOne.name = newDesiredName
        self.assertEquals(studentOne.name, newDesiredName)

    def test_ChangeNumberOfUnitsTaken(self):
        """
        This unit test is testing the changing of the 'numberOfUnitsTaken' variable. It passes when a
        student's 'numberOfUnitsTaken' variable is changed by means of its setter and cross-referenced to
        the 'newDesiredNumberOfUnitsTaken'.
        :return:
        """
        newDesiredNumberOfUnitsTaken = 130
        studentOne = StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, 150)
        studentOne.numberOfUnitsTaken = newDesiredNumberOfUnitsTaken
        self.assertEquals(studentOne.numberOfUnitsTaken, newDesiredNumberOfUnitsTaken)

    def test_ChangeRedId(self):
        """
        This unit test is testing the changing of the 'redId' variable. It passes when a student's 'redId' variable
        is changed by means of its setter and cross-referenced to the 'newDesiredRedId'.
        :return:
        """
        newDesiredRedId = 333333333
        studentOne = StudentClass.Student("Nathan", 777777777, "Nate@aol.com", "134 Home St", 4.0, 150)
        studentOne.redId = newDesiredRedId
        self.assertEquals(studentOne.redId, newDesiredRedId)

    def test_Constructor(self):
        """
        This unit test is testing the instantiation of the 'Student' object based on the 'StudentClass' via the
        default constructor. It passes when the first 4 arguments ('name', 'redId', 'email', 'address') are strings, the
        'gpa' is a number between 0 - 4.0 and 'numberOfUnitsTaken' is a number between 0 - 150.
        :return:
        """
        studentOne = StudentClass.Student("Nathan", 777777777, "Nate@aol.com", "134 Home St", 4.0, 150)
        self.assertIsInstance(studentOne, StudentClass.Student)

    def test_LowerboundGpa(self):
        """
        This unit test is testing the lower bound of the 'gpa' variable. It passes when the 'gpa' is set to a number
        lower than 4.0, thus raising a 'AttributeError'.
        :return:
        """
        with self.assertRaises(AttributeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", -0.1, 150)

    def test_LowerBoundNumberOfUnitsTaken(self):
        """
        This unit test is testing the lower bound of the 'numberOfUnitsTaken' variable. It passes when the
        'numberOfUnitsTaken' is set to a number lower than 0, thus raising a 'AttributeError'.
        :return:
        """
        with self.assertRaises(AttributeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, -0.1)

    def test_NumbersInName(self):
        """
        This unit test is testing the 'TypeError' check of the 'name' variable. It passes when a character other than the
        letters A through Z are passed into 'name'.
        :return:
        """
        with self.assertRaises(AttributeError):
            StudentClass.Student("123NotAValidName", "777777777", "Nate@aol.com", "134 Home St", "4.5", 150)

    def test_ReturnAddress(self):
        """
        This unit test is testing the return of the 'address' variable. It passes when a student's 'address' variable
        is returned by means of its property tag and cross-referenced to the 'originalAddress'.
        :return:
        """
        originalAddress = "132 Original St."
        studentOne = StudentClass.Student("Nathan", "777777777", "Nate@aol.com", originalAddress, 4.0, 150)
        self.assertEquals(studentOne.address, originalAddress)

    def test_ReturnEmail(self):
        """
        This unit test is testing the return of the 'email' variable. It passes when a student's 'email' variable
        is returned by means of its property tag and cross-referenced to the 'originalEmail'.
        :return:
        """
        originalEmail = "Nate@aol.com"
        studentOne = StudentClass.Student("Nathan", 777777777, originalEmail, "134 Home St", 4.0, 150)
        self.assertEquals(studentOne.email, originalEmail)

    def test_ReturnGpa(self):
        """
        This unit test is testing the return of the 'gpa' variable. It passes when a student's 'gpa' variable
        is returned by means of its property tag and cross-referenced to the 'originalGpa'.
        :return:
        """
        originalGpa = 4.0
        studentOne = StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", originalGpa, 150)
        self.assertEquals(studentOne.gpa, originalGpa)

    def test_ReturnName(self):
        """
        This unit test is testing the return of the 'name' variable. It passes when a student's 'name' variable
        is returned by means of its property tag and cross-referenced to the 'originalName'.
        :return:
        """
        originalName = "David"
        studentOne = StudentClass.Student(originalName, "777777777", "Nate@aol.com", "134 Home St", 4.0, 150)
        self.assertEquals(studentOne.name, originalName)


    def test_ReturnRedId(self):
        """
        This unit test is testing the return of the 'redId' variable. It passes when a student's 'redId' variable
        is returned by means of its property tag and cross-referenced to the 'originalRedId'.
        :return:
        """
        originalRedId = 777777777
        studentOne = StudentClass.Student("Nathan", originalRedId, "Nate@aol.com", "134 Home St", 4.0, 150)
        self.assertEquals(studentOne.redId, originalRedId)

    def test_UpperboundGpa(self):
        """
        This unit test is testing the upper bound of the 'gpa' variable. It passes when the 'gpa' is set to a number
        greater than 4.0, thus raising a 'AttributeError'.
        :return:
        """
        with self.assertRaises(AttributeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.1, 150)

    def test_UpperBoundNumberOfUnitsTaken(self):
        """
        This unit test is testing the upper bound of the 'numberOfUnitsTaken' variable. It passes when the
        'numberOfUnitsTaken' is set to a number greater than 150, thus raising a 'AttributeError'.
        :return:
        """
        with self.assertRaises(AttributeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, 151)

    def test_WrongTypeAddress(self):
        """
        This unit test is testing the 'TypeError' check of the 'address' variable. It passes when the 'address' is set to something
        that doesn't carry both ints and letters.
        :return:
        """
        with self.assertRaises(TypeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "123", "4.5", 150)

    def test_WrongTypeGpa(self):
        """
        This unit test is testing the 'TypeError' check of the 'gpa' variable. It passes when the 'gpa' is set to something
        other than an int or a float which triggers a 'TypeError'.
        :return:
        """
        with self.assertRaises(TypeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", "4.5", 150)

    def test_WrongTypeEmail(self):
        """
        This unit test is testing the 'TypeError' check of the 'email' variable. It passes when something other than a
        string is passed into 'email'.
        :return:
        """
        with self.assertRaises(AttributeError):
            StudentClass.Student("Nathan", "777777777", 7, "134 Home St", "4.5", 150)

    def test_WrongTypeName(self):
        """
        This unit test is testing the 'TypeError' check of the 'name' variable. It passes when a character other than the
        letters A through Z are passed into 'name'.
        :return:
        """
        with self.assertRaises(AttributeError):
            StudentClass.Student(1, "777777777", "Nate@aol.com", "134 Home St", "4.5", 150)

    def test_WrongTypeNumberOfUnitsTaken(self):
        """
        This unit test is testing the 'TypeError' check of the 'numberOfUnitsTaken' variable. It passes when the
        'numberOfUnitsTaken' is set to something other than an int or a float which triggers a 'TypeError'.
        :return:
        """
        with self.assertRaises(TypeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, "150")

    def test_WrongTypeRedId(self):
        """
        This unit test is testing the 'redId' check of the 'redId' variable. It passes when a character other than a
        number is passed into 'redId'.
        :return:
        """
        with self.assertRaises(AttributeError):
            StudentClass.Student(1, "AAAAAAAAA", "Nate@aol.com", "134 Home St", 4.5, 150)

if __name__ == '__main__':
    unittest.main()