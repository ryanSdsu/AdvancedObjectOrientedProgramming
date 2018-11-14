import unittest
from Assignment_Four import FileReadClass
from Assignment_Four.AbstractWebNotifierFactoryClass import AbstractWebNotifierFactory
from Assignment_Four.ConsoleObserverClass import ConsoleObserver
from Assignment_Four.MailObserverClass import MailObserver
from Assignment_Four.SMSObserverClass import SMSObserver
from Assignment_Four.WebsiteSubjectClass import WebsiteSubject

class TestAbstractWebNotifierFactoryClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Abstract Web Notifier Factory Class"""

    def setUp(self):
        """
        This is the set up for the 'Abstract Web Notifier Factory' class.  We are creating
        an 'Abstract Web Notifier Factory' as well as a 'FileRead' object to be set, added and tested later.
        :return:
        """
        self.test_abstract_factory = AbstractWebNotifierFactory()
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

    def test_create_website_subject(self):
        """
        This unit test is testing the 'create_web_subject' def of the 'Abstract Web Notifier Factory' class.
        It passes when upon passing in the instructions, a WebsiteSubject object is created and returned.
        :return:
        """
        self.test_website_subject = self.test_abstract_factory.create_website_subject(self.test_file_lines[0])
        self.assertIsInstance(self.test_website_subject, WebsiteSubject)

    def test_create_console_observer(self):
        """
        This unit test is testing the 'create_console_observer' def of the 'Abstract Web Notifier Factory' class.
        It passes when upon passing in the instructions, a ConsoleObserver object is created and returned.
        :return:
        """
        self.test_console_observer = self.test_abstract_factory.create_console_observer(self.test_file_lines[0])
        self.assertIsInstance(self.test_console_observer, ConsoleObserver)

    def test_create_sms_observer(self):
        """
        This unit test is testing the 'create_sms_observer' def of the 'Abstract Web Notifier Factory' class.
        It passes when upon passing in the instructions, a SmsObserver object is created and returned.
        :return:
        """
        self.test_sms_observer = self.test_abstract_factory.create_sms_observer(self.test_file_lines[2])
        self.assertIsInstance(self.test_sms_observer, SMSObserver)

    def test_create_mail_observer(self):
        """
        This unit test is testing the 'create_mail_observer' def of the 'Abstract Web Notifier Factory' class.
        It passes when upon passing in the instructions, a MailObserver object is created and returned.
        :return:
        """
        self.test_mail_observer = self.test_abstract_factory.create_mail_observer(self.test_file_lines[1])
        self.assertIsInstance(self.test_mail_observer, MailObserver)


if __name__ == '__main__':
    unittest.main()


