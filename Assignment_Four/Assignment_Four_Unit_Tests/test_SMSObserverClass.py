import unittest
from Assignment_Four import FileReadClass
from Assignment_Four.SMSObserverClass import SMSObserver
from mock import patch

class TestSMSObserverClass(unittest.TestCase):
    """This is the base class for the unit tests involving the SMS Observer Class"""

    def setUp(self):
        """
        This is the set up for the 'SMSObserver' class.  We are creating the 'FileRead' objects to be
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
        This unit test is testing the __init__ def of the 'SMSObserver' class.  It passes when a
        'SMSObserver' class is successfully created along with its variable via 'sms_number' containing
        the sms number being passed into it and 'carrier_email' having the correct gateway domain.
        :return:
        """
        self.test_sms_observer = SMSObserver(self.test_file_lines[2])
        self.assertIsInstance(self.test_sms_observer, SMSObserver)
        self.assertEqual(self.test_sms_observer.sms_number, '6195943535')
        self.assertEqual(self.test_sms_observer.carrier_email, '@vzwpix.com')
        self.assertEqual(self.test_sms_observer.web_address, 'http://www.eli.sdsu.edu/courses/fall18/cs635/notes/index.html')
        self.test_sms_observer = SMSObserver(['http://www.google.com', 'sms', '6191234567', 'u.s. cellular'])
        self.assertIsInstance(self.test_sms_observer, SMSObserver)
        self.assertEqual(self.test_sms_observer.web_address, 'http://www.google.com')
        self.assertEqual(self.test_sms_observer.sms_number, '6191234567')
        self.assertEqual(self.test_sms_observer.carrier_email, '@mms.uscc.net')

    def test_update(self):
        """
        This unit test is testing the 'update' def of the 'SMSObserver' class.
        It passes when a mock object receives the correct inputs for
        sending and receiving an sms message.
        :return:
        """
        self.test_sms_observer = SMSObserver(self.test_file_lines[2])
        self.assertIsInstance(self.test_sms_observer, SMSObserver)
        self.assertEqual(self.test_sms_observer.sms_number, '6195943535')
        self.assertEqual(self.test_sms_observer.carrier_email, '@vzwpix.com')
        with patch("smtplib.SMTP") as mock_smtp:
            self.test_sms_observer.update()
            instance = mock_smtp.return_value
            self.assertTrue(instance.sendmail.called)
            instance.sendmail.assert_any_call(
                "jakewhitney86@gmail.com", "6195943535@vzwpix.com",
                "The website '" + self.test_sms_observer.web_address + "' you're monitoring has been updated")

if __name__ == '__main__':
    unittest.main()


