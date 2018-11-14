import unittest
from Assignment_Four import FileReadClass
from Assignment_Four.WebsiteSubjectClass import WebsiteSubject
from Assignment_Four.ConsoleObserverClass import ConsoleObserver
from Assignment_Four.SMSObserverClass import SMSObserver
from mock import patch
import _thread
import time

class TestWebsiteSubjectClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Website Subject Class"""

    def setUp(self):
        """
        This is the set up for the 'Website Subject' class.  We are creating the 'FileRead' objects to be
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
        This unit test is testing the __init__ def of the 'Website Subject' class.  It passes when a
        'Website Subject' class is successfully created along with its variable via 'currently_attached_observers'
        containing a list of observers for which to be added.
        :return:
        """
        self.test_website_subject = WebsiteSubject(self.test_file_lines[0])
        self.assertIsInstance(self.test_website_subject, WebsiteSubject)
        self.assertListEqual(self.test_website_subject.currently_attached_observers, [])

    def test_attach_def(self):
        """
        This unit test is testing the attach def of the 'Website Subject' class.  It passes when an
        'Observer' class is successfully created and attached/appended via the 'currently_attached_observers'
        list of the Website Subject class.
        :return:
        """
        self.test_website_subject = WebsiteSubject(self.test_file_lines[0])
        self.assertIsInstance(self.test_website_subject, WebsiteSubject)
        self.assertListEqual(self.test_website_subject.currently_attached_observers, [])
        self.test_console_observer = ConsoleObserver(self.test_file_lines[0])
        self.test_website_subject.attach(self.test_console_observer)
        self.assertListEqual(self.test_website_subject.currently_attached_observers, [self.test_console_observer])

    def test_monitor_def(self):
        """
        This unit test is testing the monitor def of the 'Website Subject' class.  It passes when an
        'Observer' class that is successfully created and attached/appended is updated once the def
        monitor is called and detects a change via the "web_address"
        :return:
        """
        self.test_website_subject = WebsiteSubject(['https://www.nytimes.com', 'sms', '6195943535', 'verizon'])
        self.test_sms_observer = SMSObserver(['https://www.nytimes.com', 'sms', '6195943535', 'verizon'])
        self.test_website_subject.attach(self.test_sms_observer)

        with patch("smtplib.SMTP") as mock_smtp:
            _thread.start_new_thread(self.test_website_subject.monitor, ())
            instance = mock_smtp.return_value
            while instance.sendmail.called == False:
                time.sleep(3)
                instance = mock_smtp.return_value
            instance.sendmail.assert_any_call(
                "jakewhitney86@gmail.com", "6195943535@vzwpix.com",
                "The website '" + self.test_sms_observer.web_address + "' you're monitoring has been updated")
            self.assertTrue(instance.sendmail.called)

    def test_detach_def(self):
        """
        This unit test is testing the detach def of the 'Website Subject' class.  It passes when an
        'Observer' class is successfully detached and removed via the 'currently_attached_observers'
        list of the Website Subject class.
        :return:
        """
        self.test_website_subject = WebsiteSubject(self.test_file_lines[0])
        self.assertIsInstance(self.test_website_subject, WebsiteSubject)
        self.assertListEqual(self.test_website_subject.currently_attached_observers, [])
        self.test_console_observer = ConsoleObserver(self.test_file_lines[0])
        self.test_website_subject.attach(self.test_console_observer)
        self.assertListEqual(self.test_website_subject.currently_attached_observers, [self.test_console_observer])
        self.test_website_subject.detach(self.test_console_observer)
        self.assertListEqual(self.test_website_subject.currently_attached_observers, [])

if __name__ == '__main__':
    unittest.main()


