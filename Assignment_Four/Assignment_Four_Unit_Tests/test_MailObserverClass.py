import unittest
from Assignment_Four import FileReadClass
from Assignment_Four.MailObserverClass import MailObserver
from mock import patch

class TestMailObserverClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Mail Observer Class"""

    def setUp(self):
        """
        This is the set up for the 'MailObserver' class.  We are creating the 'FileRead' objects to be
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
        This unit test is testing the __init__ def of the 'MailObserver' class.  It passes when a
        'MailObserver' class is successfully created along with its variable via 'email_address' containing
        the email passed into it and 'web_address' having the web .
        :return:
        """
        self.test_email_observer = MailObserver(self.test_file_lines[1])
        self.assertIsInstance(self.test_email_observer, MailObserver)
        self.assertEqual(self.test_email_observer.email_address, 'whitney@sdsu.edu')
        self.assertEqual(self.test_email_observer.web_address, 'http://www.eli.sdsu.edu/index.html')

    def test_update(self):
        """
        This unit test is testing the 'update' def of the 'SMSObserver' class.
        It passes when a mock object receives the correct inputs for
        sending and receiving an sms message.
        :return:
        """
        self.test_email_observer = MailObserver(['http://www.eli.sdsu.edu/index.html', 'mail', 'russell.james.ucf@gmail.com'])
        self.assertIsInstance(self.test_email_observer, MailObserver)
        self.assertEqual(self.test_email_observer.email_address, 'russell.james.ucf@gmail.com')
        with patch("smtplib.SMTP") as mock_smtp:
            self.test_email_observer.update()
            instance = mock_smtp.return_value
            self.assertTrue(instance.sendmail.called)
            instance.sendmail.assert_any_call(
                "jakewhitney86@gmail.com", "russell.james.ucf@gmail.com",
                "The website '" + self.test_email_observer.web_address + "' you're monitoring has been updated")

if __name__ == '__main__':
    unittest.main()


