import unittest
import io
from contextlib import redirect_stdout
from Assignment_Four import FileReadClass
from Assignment_Four.ConsoleObserverClass import ConsoleObserver

class TestConsoleObserverClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Console Observer Class"""

    def setUp(self):
        """
        This is the set up for the 'Console Observer' class.  We are creating the 'FileRead' objects to be
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
        This unit test is testing the __init__ def of the 'Console Observer' class.  It passes when a
        'Console Observer' class is successfully created along with its variable via 'web_address' containing
        the url of the website being passed into it.
        :return:
        """
        self.test_console_observer = ConsoleObserver(self.test_file_lines[0])
        self.assertIsInstance(self.test_console_observer, ConsoleObserver)
        self.assertEqual(self.test_console_observer.web_address, 'http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html')

    def test_update(self):
        """
        This unit test is testing the 'update' def of the 'Console Observer' class.
        It passes when a message stating that the website has been updated appears on the console.
        :return:
        """
        self.test_console_observer = ConsoleObserver(self.test_file_lines[0])
        self.assertIsInstance(self.test_console_observer, ConsoleObserver)
        self.assertEqual(self.test_console_observer.web_address, 'http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html')
        with io.StringIO() as buffer, redirect_stdout(buffer):
            self.test_console_observer.update()
            lastPrintStatement = buffer.getvalue()
            lastPrintStatement = lastPrintStatement.strip('\n')
        self.assertEqual("The website '" + self.test_console_observer.web_address + "' you're monitoring has been updated",
                         lastPrintStatement)

    def test_str_def(self):
        """
        This unit test is testing the 'str' def of the 'Console observer' class. It passes when upon proceeding with the
        __str__() def that the 'web_address' variable is being passed to it.
        :return:
        """
        self.test_console_observer = ConsoleObserver(self.test_file_lines[0])
        self.assertIsInstance(self.test_console_observer, ConsoleObserver)
        self.assertEqual(self.test_console_observer.web_address, 'http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html')
        self.assertEquals(self.test_console_observer.__str__(),
                          "The website '" + self.test_console_observer.web_address + "' you're monitoring has been updated")

if __name__ == '__main__':
    unittest.main()


