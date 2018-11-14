import unittest
import io
from contextlib import redirect_stdout
from Assignment_Four import FileReadClass
from Assignment_Four.WebNotifierLoaderClass import WebNotifierLoader
from Assignment_Four.ConsoleObserverClass import ConsoleObserver
from Assignment_Four.MailObserverClass import MailObserver
from Assignment_Four.SMSObserverClass import SMSObserver
from Assignment_Four.WebsiteSubjectClass import WebsiteSubject
from mock import patch

class TestNotifierFactoryClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Web Notifier Loader Class"""

    def setUp(self):
        """
        This is the set up for the 'Web Notifier Loader' class.  We are creating the 'File Read' objects to be
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
        This unit test is testing the __init__ def of the 'Web Notifier Loader' class.  It passes when a
        'Web Notifier Loader' class is successfully created along with its dictionary via 'subject_dictionary'
        being instantiated.
        :return:
        """
        self.test_factory = WebNotifierLoader()
        self.assertIsInstance(self.test_factory, WebNotifierLoader)
        self.assertEqual(self.test_factory.subject_dictionary, {})

    def test_create_notifier_def(self):
        """
        This unit test is testing the 'update' def of the 'Console Observer' class.
        It passes when a message stating that the website has been updated appears on the console.
        :return:
        """
        self.test_factory = WebNotifierLoader()
        for instructions in self.test_file_lines:
            self.website_subjects_list = self.test_factory.create_notifier(instructions)

        self.assertIsInstance(self.website_subjects_list[0], WebsiteSubject)
        self.assertEqual(self.website_subjects_list[0].web_address,
                        'http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html')

        self.assertIsInstance(self.website_subjects_list[0].currently_attached_observers[0], ConsoleObserver)
        self.assertEqual(self.website_subjects_list[0].currently_attached_observers[0].web_address,
                        'http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html')

        self.assertIsInstance(self.website_subjects_list[0].currently_attached_observers[1], SMSObserver)
        self.assertEqual(self.website_subjects_list[0].currently_attached_observers[1].sms_number, '6195943535')

        self.assertIsInstance(self.website_subjects_list[0].currently_attached_observers[2], SMSObserver)
        self.assertEqual(self.website_subjects_list[0].currently_attached_observers[2].sms_number, '6191234567')

        self.assertIsInstance(self.website_subjects_list[1], WebsiteSubject)
        self.assertEqual(self.website_subjects_list[1].web_address, 'http://www.eli.sdsu.edu/index.html')

        self.assertIsInstance(self.website_subjects_list[1].currently_attached_observers[0], MailObserver)
        self.assertEqual(self.website_subjects_list[1].currently_attached_observers[0].email_address, 'whitney@sdsu.edu')

        self.assertIsInstance(self.website_subjects_list[1].currently_attached_observers[1], ConsoleObserver)
        self.assertEqual(self.website_subjects_list[1].currently_attached_observers[1].web_address,
                         'http://www.eli.sdsu.edu/index.html')

if __name__ == '__main__':
    unittest.main()


