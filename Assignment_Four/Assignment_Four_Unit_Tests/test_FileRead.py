import unittest
from Assignment_Four import FileReadClass

class TestFileReadClass(unittest.TestCase):
    """This is the base class for the unit tests involving the FileRead Class"""

    def setUp(self):
        """
        This is the set up for the 'FileRead' class. We are creating the 'FileRead' objects to be
        set, added and tested later.
        :return:
        """
        self.test_file_read = FileReadClass.FileRead(
            "/Users/RJ/PycharmProjects/AdvancedObjectOrientedProgramming/Assignment_Four/UrlWebPages")

    def test_init_def(self):
        """
        This unit test is testing the __init__ def of the 'FileRead' class.  It passes when a
        'FileRead' class is successfully created along with its variable via 'file' containing
        the file being passed into it and 'file_lines' having all of the lines be aggregated into
        a list.
        :return:
        """
        self.assertIsInstance(self.test_file_read, FileReadClass.FileRead)
        print(self.test_file_read.file_lines)
        self.assertListEqual(self.test_file_read.file_lines,
                             ['http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html console\n',
                              'http://www.eli.sdsu.edu/index.html mail whitney@sdsu.edu\n',
                              'http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html sms 6195943535 verizon\n',
                              'http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html sms 6191234567 att\n',
                              'http://www.eli.sdsu.edu/index.html console'])

    def test_remove_all_trailing_whitespace(self):
        """
        This unit test is testing the 'remove_all_trailing_whitespace' def of the 'FileRead' class.
        It passes when the all of the lines in the 'file_lines' list have had any trailing whitespace
        be removed.
        :return:
        """
        self.test_file_read.remove_all_trailing_whitespace()
        self.assertListEqual(self.test_file_read.file_lines,
                             ['http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html console',
                              'http://www.eli.sdsu.edu/index.html mail whitney@sdsu.edu',
                              'http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html sms 6195943535 verizon',
                              'http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html sms 6191234567 att',
                              'http://www.eli.sdsu.edu/index.html console'])

    def test_replace_characters_in_lines(self):
        """
        This unit test is testing the 'replace_characters_in_lines' def of the 'FileRead' class.
        It passes when the all of the lines in the 'file_lines' list that have a certain character
        sequence are replaced with a "new sequence" of characters in that specific sequence.
        :return:
        """
        self.test_file_read.remove_all_trailing_whitespace()
        self.test_file_read.replace_characters_in_lines("=", " ")
        self.assertListEqual(self.test_file_read.file_lines,
                             ['http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html console',
                              'http://www.eli.sdsu.edu/index.html mail whitney@sdsu.edu',
                              'http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html sms 6195943535 verizon',
                              'http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html sms 6191234567 att',
                              'http://www.eli.sdsu.edu/index.html console'])

    def test_split_lines_into_words(self):
        """
        This unit test is testing the 'split_lines_into_words' def of the 'FileRead' class.
        It passes when the all of the lines in the 'file_lines' list have had any trailing whitespace
        be removed and then are reorganized into lists containing each individual word per
        their respective line.
        :return:
        """
        self.test_file_read.remove_all_trailing_whitespace()
        self.test_file_read.replace_characters_in_lines("=", " ")
        self.test_file_read.split_lines_into_words()
        self.assertListEqual(self.test_file_read.file_lines,
                             [['http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html', 'console'],
                              ['http://www.eli.sdsu.edu/index.html', 'mail', 'whitney@sdsu.edu'],
                              ['http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html', 'sms', '6195943535', 'verizon'],
                              ['http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html', 'sms', '6191234567', 'att'],
                              ['http://www.eli.sdsu.edu/index.html', 'console']
                              ])

if __name__ == '__main__':
    unittest.main()


