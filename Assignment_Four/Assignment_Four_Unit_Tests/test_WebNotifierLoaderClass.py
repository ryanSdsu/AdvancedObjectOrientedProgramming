import unittest
from mock import patch
import time
import io
from contextlib import redirect_stdout
from Assignment_Four import FileReadClass
from Assignment_Four.WebNotifierLoaderClass import WebNotifierLoader
from Assignment_Four.ConsoleObserverClass import ConsoleObserver
from Assignment_Four.MailObserverClass import MailObserver
from Assignment_Four.SMSObserverClass import SMSObserver
from Assignment_Four.WebsiteSubjectClass import WebsiteSubject
from Assignment_Four.WebNotifierFactoryClass import WebNotifierFactory

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
        being instantiated as well as a 'Web Notifier Factory'.
        :return:
        """
        self.test_loader = WebNotifierLoader()
        self.assertIsInstance(self.test_loader, WebNotifierLoader)
        self.assertEqual(self.test_loader.subject_dictionary, {})
        self.assertIsInstance(self.test_loader.web_notifier_factory, WebNotifierFactory)

    def test_load_notifier_def(self):
        """
        This unit test is testing the 'load_notifier' def of the 'Web Notifier Loader' class.
        It passes when various subjects and observers get loaded correctly via a list of string
        instructions.
        :return:
        """
        self.test_loader = WebNotifierLoader()
        for instructions in self.test_file_lines:
            self.website_subjects_list = self.test_loader.load_notifier(instructions)

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

    def test_execute_web_notifiers_def(self):
        """
        This unit test is testing the 'execute_web_notifiers' def of the 'Web Notifier Loader' class.
        It passes when a loaded 'subject_list' gets linked via RxPy and there is now a separate thread
        for each subject monitoring a website and updating the observers whenever there is a change within
        a certain time interval.
        :return:
        """
        self.test_loader = WebNotifierLoader()
        self.test_loader.load_notifier(['https://www.nytimes.com', 'sms', '6195943535', 'verizon'])
        self.test_loader.load_notifier(['https://www.nytimes.com', 'console'])

        with patch("smtplib.SMTP") as mock_smtp:
            with io.StringIO() as buffer, redirect_stdout(buffer):
                self.test_loader.execute_web_notifiers()
                instance = mock_smtp.return_value
                while instance.sendmail.called == False:
                    time.sleep(3)
                    instance = mock_smtp.return_value
                instance.sendmail.assert_any_call(
                    "jakewhitney86@gmail.com", "6195943535@vzwpix.com",
                    "The website 'https://www.nytimes.com' you're monitoring has been updated")
                self.assertTrue(instance.sendmail.called)

                last_print_statement = ""
                while "The website 'https://www.nytimes.com' you're monitoring has been updated" not in last_print_statement:
                    last_print_statement = buffer.getvalue()
                    last_print_statement = last_print_statement.strip('\n')
                last_print_statement = "The website 'https://www.nytimes.com' you're monitoring has been updated"
                self.assertEqual("The website 'https://www.nytimes.com' you're monitoring has been updated", last_print_statement)

if __name__ == '__main__':
    unittest.main()


