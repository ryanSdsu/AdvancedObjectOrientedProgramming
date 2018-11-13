import unittest
import io
from contextlib import redirect_stdout
from Assignment_Four import FileReadClass
from Assignment_Four.NotifierFactoryClass import NotifierFactory
from mock import patch

class TestFileReadClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Notifier Factory Class"""

    def setUp(self):
        """
        This is the set up for the 'Notifier Factory' class. We are creating the 'FileRead' objects to be
        set, added and tested later.
        :return:
        """
        self.test_file_read = FileReadClass.FileRead(
            "/Users/RJ/PycharmProjects/AdvancedObjectOrientedProgramming/Assignment_Four/UrlWebPages")
        self.test_file_read.split_lines_into_words()
        self.test_file_lines = self.test_file_read.file_lines
        self.assertListEqual(self.test_file_lines,
                             [['http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html', 'console'],
                              ['http://www.eli.sdsu.edu/index.html', 'mail', 'whitney@sdsu.edu'],
                              ['http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html', 'sms', '6195943535', 'verizon'],
                              ['http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html', 'sms', '6191234567', 'att'],
                              ['http://www.eli.sdsu.edu/index.html', 'console']
                              ])

    def test_init_def(self):
        """
        This unit test is testing the __init__ def of the 'Notifier Factory' class.  It passes when a
        'Notifier Factory' class is successfully created along with its dictionary via 'subject_dictionary'
        being instantiated.
        :return:
        """
        self.test_factory = NotifierFactory()
        self.assertIsInstance(self.test_factory, NotifierFactory)
        self.assertEqual(self.test_factory.subject_dictionary, {})

    def test_create_notifier_def(self):
        """
        This unit test is testing the 'update' def of the 'Console Observer' class.
        It passes when a message stating that the website has been updated appears on the console.
        :return:
        """
        self.test_factory = NotifierFactory()
        for instructions in self.test_file_lines:
            self.website_subjects_list = self.test_factory.create_notifier(instructions)

if __name__ == '__main__':
    unittest.main()


