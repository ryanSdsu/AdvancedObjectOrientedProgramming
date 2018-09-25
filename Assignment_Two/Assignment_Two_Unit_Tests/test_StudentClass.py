import unittest
from Assignment_Two import StudentClass

class TestStudentClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Student Class"""
    def test_change_address(self):
        """
        This unit test is testing the changing of the 'address' variable. It passes when a student's 'address' variable
        is changed by means of its setter and cross-referenced to the 'new_desired_address'.
        :return:
        """
        new_desired_address = "132 New St."
        student_one = StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, 150)
        student_one.address = new_desired_address
        self.assertEquals(student_one.address, new_desired_address)

    def test_change_email(self):
        """
        This unit test is testing the changing of the 'email' variable. It passes when a student's 'email' variable
        is changed by means of its setter and cross-referenced to the 'new_desired_email'.
        :return:
        """
        new_desired_email = "Nathaniel@aol.com"
        student_one = StudentClass.Student("Nathan", 777777777, "Nate@aol.com", "134 Home St", 4.0, 150)
        student_one.email = new_desired_email
        self.assertEquals(student_one.email, new_desired_email)

    def test_change_gpa(self):
        """
        This unit test is testing the changing of the 'gpa' variable. It passes when a student's 'gpa' variable
        is changed by means of its setter and cross-referenced to the 'new_desired_gpa'.
        :return:
        """
        new_desired_gpa = 3.5
        student_one = StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, 150)
        student_one.gpa = new_desired_gpa
        self.assertEquals(student_one.gpa, new_desired_gpa)

    def test_change_name(self):
        """
        This unit test is testing the changing of the 'name' variable. It passes when a student's 'name' variable
        is changed by means of its setter and cross-referenced to the 'new_desired_name'.
        :return:
        """
        new_desired_name = "David"
        student_one = StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, 150)
        student_one.name = new_desired_name
        self.assertEquals(student_one.name, new_desired_name)

    def test_change_number_of_units_taken(self):
        """
        This unit test is testing the changing of the 'number_of_units_taken' variable. It passes when a
        student's 'number_of_units_taken' variable is changed by means of its setter and cross-referenced to
        the 'new_desired_number_of_units_taken'.
        :return:
        """
        new_desired_number_of_units_taken = 130
        student_one = StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, 150)
        student_one.number_of_units_taken = new_desired_number_of_units_taken
        self.assertEquals(student_one.number_of_units_taken, new_desired_number_of_units_taken)

    def test_change_red_id(self):
        """
        This unit test is testing the changing of the 'red_id' variable. It passes when a student's 'red_id' variable
        is changed by means of its setter and cross-referenced to the 'new_desired_red_id'.
        :return:
        """
        new_desired_red_id = 333333333
        student_one = StudentClass.Student("Nathan", 777777777, "Nate@aol.com", "134 Home St", 4.0, 150)
        student_one.red_id = new_desired_red_id
        self.assertEquals(student_one.red_id, new_desired_red_id)

    def test_constructor(self):
        """
        This unit test is testing the instantiation of the 'Student' object based on the 'StudentClass' via the
        default constructor. It passes when the first 4 arguments ('name', 'red_id', 'email', 'address') are strings, the
        'gpa' is a number between 0 - 4.0 and 'number_of_units_taken' is a number between 0 - 150.
        :return:
        """
        student_one = StudentClass.Student("Nathan", 777777777, "Nate@aol.com", "134 Home St", 4.0, 150)
        self.assertIsInstance(student_one, StudentClass.Student)

    def test_lower_bound_gpa(self):
        """
        This unit test is testing the lower bound of the 'gpa' variable. It passes when the 'gpa' is set to a number
        lower than 4.0, thus raising a 'AttributeError'.
        :return:
        """
        with self.assertRaises(AttributeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", -0.1, 150)

    def test_lower_bound_number_of_units_taken(self):
        """
        This unit test is testing the lower bound of the 'number_of_units_taken' variable. It passes when the
        'number_of_units_taken' is set to a number lower than 0, thus raising a 'AttributeError'.
        :return:
        """
        with self.assertRaises(AttributeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, -0.1)

    def test_numbers_in_name(self):
        """
        This unit test is testing the 'TypeError' check of the 'name' variable. It passes when a character other than the
        letters A through Z are passed into 'name'.
        :return:
        """
        with self.assertRaises(TypeError):
            StudentClass.Student("123NotAValidName", "777777777", "Nate@aol.com", "134 Home St", "4.5", 150)

    def test_print_student(self):
        """
        This unit test is testing the print of the student class. It passes when both the name
        and red_id are returned.
        :return:
        """
        student = StudentClass.Student("Nathan", 777777777, "Nate@aol.com", "134 Home St", 3.6, 110)
        self.assertEquals(student.__str__(), "Red ID: 777777777 Name: Nathan")

    def test_return_address(self):
        """
        This unit test is testing the return of the 'address' variable. It passes when a student's 'address' variable
        is returned by means of its property tag and cross-referenced to the 'original_address'.
        :return:
        """
        original_address = "132 Original St."
        student_one = StudentClass.Student("Nathan", "777777777", "Nate@aol.com", original_address, 4.0, 150)
        self.assertEquals(student_one.address, original_address)

    def test_return_email(self):
        """
        This unit test is testing the return of the 'email' variable. It passes when a student's 'email' variable
        is returned by means of its property tag and cross-referenced to the 'original_email'.
        :return:
        """
        original_email = "Nate@aol.com"
        student_one = StudentClass.Student("Nathan", 777777777, original_email, "134 Home St", 4.0, 150)
        student_one.red_id
        self.assertEquals(student_one.email, original_email)

    def test_return_gpa(self):
        """
        This unit test is testing the return of the 'gpa' variable. It passes when a student's 'gpa' variable
        is returned by means of its property tag and cross-referenced to the 'original_gpa'.
        :return:
        """
        original_gpa = 4.0
        student_one = StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", original_gpa, 150)
        self.assertEquals(student_one.gpa, original_gpa)

    def test_return_name(self):
        """
        This unit test is testing the return of the 'name' variable. It passes when a student's 'name' variable
        is returned by means of its property tag and cross-referenced to the 'original_name'.
        :return:
        """
        original_name = "David"
        student_one = StudentClass.Student(original_name, "777777777", "Nate@aol.com", "134 Home St", 4.0, 150)
        self.assertEquals(student_one.name, original_name)


    def test_return_red_id(self):
        """
        This unit test is testing the return of the 'red_id' variable. It passes when a student's 'red_id' variable
        is returned by means of its property tag and cross-referenced to the 'original_red_id'.
        :return:
        """
        original_red_id = 777777777
        student_one = StudentClass.Student("Nathan", original_red_id, "Nate@aol.com", "134 Home St", 4.0, 150)
        self.assertEquals(student_one.red_id, original_red_id)

    def test_upper_bound_gpa(self):
        """
        This unit test is testing the upper bound of the 'gpa' variable. It passes when the 'gpa' is set to a number
        greater than 4.0, thus raising a 'AttributeError'.
        :return:
        """
        with self.assertRaises(AttributeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.1, 150)

    def test_upper_bound_number_of_units_taken(self):
        """
        This unit test is testing the upper bound of the 'number_of_units_taken' variable. It passes when the
        'number_of_units_taken' is set to a number greater than 150, thus raising a 'AttributeError'.
        :return:
        """
        with self.assertRaises(AttributeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, 151)

    def test_wrong_type_address(self):
        """
        This unit test is testing the 'TypeError' check of the 'address' variable. It passes when the 'address' is set to something
        that doesn't carry both ints and letters.
        :return:
        """
        with self.assertRaises(TypeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "123", "4.5", 150)

    def test_wrong_type_gpa(self):
        """
        This unit test is testing the 'TypeError' check of the 'gpa' variable. It passes when the 'gpa' is set to something
        other than an int or a float which triggers a 'TypeError'.
        :return:
        """
        with self.assertRaises(TypeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", "4.5", 150)

    def test_wrong_type_email(self):
        """
        This unit test is testing the 'TypeError' check of the 'email' variable. It passes when something other than a
        string is passed into 'email'.
        :return:
        """
        with self.assertRaises(AttributeError):
            StudentClass.Student("Nathan", "777777777", 7, "134 Home St", "4.5", 150)

    def test_wrong_type_name(self):
        """
        This unit test is testing the 'TypeError' check of the 'name' variable. It passes when a character other than the
        letters A through Z are passed into 'name'.
        :return:
        """
        with self.assertRaises(AttributeError):
            StudentClass.Student(1, "777777777", "Nate@aol.com", "134 Home St", "4.5", 150)

    def test_wrong_type_number_of_units_taken(self):
        """
        This unit test is testing the 'TypeError' check of the 'number_of_units_taken' variable. It passes when the
        'number_of_units_taken' is set to something other than an int or a float which triggers a 'TypeError'.
        :return:
        """
        with self.assertRaises(TypeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, "150")

    def test_wrong_type_red_id(self):
        """
        This unit test is testing the 'red_id' check of the 'red_id' variable. It passes when a character other than a
        number is passed into 'red_id'.
        :return:
        """
        with self.assertRaises(AttributeError):
            StudentClass.Student(1, "AAAAAAAAA", "Nate@aol.com", "134 Home St", 4.5, 150)

if __name__ == '__main__':
    unittest.main()