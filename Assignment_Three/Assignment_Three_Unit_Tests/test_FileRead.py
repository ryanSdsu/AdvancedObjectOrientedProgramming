import unittest
from Assignment_Three import FileReadClass
from Assignment_Three import TurtleClass
from Assignment_Three import LocationClass

class TestFileReadClass(unittest.TestCase):
    """This is the base class for the unit tests involving the FileRead Class"""

    def setUp(self):
        """
        This is the set up for the 'FileRead' class. We are creating the 'FileRead' objects to be
        set, added and tested later.
        :return:
        """
        self.test_file_read = FileReadClass.FileRead(
            "/Users/RJ/PycharmProjects/AdvancedObjectOrientedProgramming/Assignment_Three/sample_text")

    def test_init_def(self):
        """
        This unit test is testing the __init__ def of the 'FileRead' class.  It passes when a
        'FileRead' class is successfully created along with its variable via 'file' containing
        the file being passed into it and 'file_lines' having all of the lines be aggregated into
        a list.
        :return:
        """
        self.assertIsInstance(self.test_file_read, FileReadClass.FileRead)
        self.assertListEqual(self.test_file_read.file_lines,
                             ['move 10\n', 'turn 90\n', 'move 20\n', 'turn -60\n', 'move 15'])

    def test_remove_all_trailing_whitespace(self):
        """
        This unit test is testing the 'remove_all_trailing_whitespace' def of the 'FileRead' class.
        It passes when the all of the lines in the 'file_lines' list have had any trailing whitespace
        be removed.
        :return:
        """
        self.test_file_read.remove_all_trailing_whitespace()
        self.assertListEqual(self.test_file_read.file_lines,
                             ['move 10', 'turn 90', 'move 20', 'turn -60', 'move 15'])

if __name__ == '__main__':
    unittest.main()


