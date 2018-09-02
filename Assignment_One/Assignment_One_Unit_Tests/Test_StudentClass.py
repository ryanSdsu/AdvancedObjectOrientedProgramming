import unittest
from Assignment_One import StudentClass

class TestStudentClass(unittest.TestCase):
    def test_Constructor(self):
        studentOne = StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, 150)
        self.assertIsInstance(studentOne, StudentClass.Student)

    def test_WrongTypeGpa(self):
        with self.assertRaises(TypeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", "4.5", 150)

    def test_UpperboundGpa(self):
        with self.assertRaises(AttributeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.1, 150)

    def test_LowerboundGpa(self):
        with self.assertRaises(AttributeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", -0.1, 150)

    def test_WrongTypeNumberOfUnitsTaken(self):
        with self.assertRaises(TypeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, "150")

    def test_UpperBoundNumberOfUnitsTaken(self):
        with self.assertRaises(AttributeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, 151)

    def test_LowerBoundNumberOfUnitsTaken(self):
        with self.assertRaises(AttributeError):
            StudentClass.Student("Nathan", "777777777", "Nate@aol.com", "134 Home St", 4.0, -0.1)

if __name__ == '__main__':
    unittest.main()