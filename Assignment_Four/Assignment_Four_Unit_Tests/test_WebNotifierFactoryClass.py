import unittest
from Assignment_Four import FileReadClass
from Assignment_Four.WebNotifierFactoryClass import WebNotifierFactory
from Assignment_Four.ConsoleObserverClass import ConsoleObserver
from Assignment_Four.MailObserverClass import MailObserver
from Assignment_Four.SMSObserverClass import SMSObserver
from Assignment_Four.WebsiteSubjectClass import WebsiteSubject

class TestAbstractWebNotifierFactoryClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Web Notifier Factory Class"""

    def setUp(self):
        """
        This is the set up for the 'Web Notifier Factory' class.  We are creating
        an 'Web Notifier Factory' as well as a 'FileRead' object to be set, added and tested later.
        :return:
        """
        self.test_abstract_factory = WebNotifierFactory()
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

    def test_create_subject(self):
        """
        This unit test is testing the 'create_subject' def of the 'Web Notifier Factory' class.
        It passes when upon passing in the instructions, a WebsiteSubject object is created and returned.
        And it also passes when an invalid url is passed thus throwing a value error exception.
        :return:
        """
        self.test_website_subject = self.test_abstract_factory.create_subject(self.test_file_lines[0])
        self.assertIsInstance(self.test_website_subject, WebsiteSubject)
        with self.assertRaises(ValueError):
            self.test_abstract_factory.create_subject("Invalid Url")

    def test_create_observer(self):
        """
        This unit test is testing the 'create_observer' def of the 'Web Notifier Factory' class.
        It passes when upon passing in the instructions, a ConsoleObserver, SMSObserver and MailObserver
        object are created and returned.  It also passes when an invalid key is passed thus throwing
        a key error exception.
        :return:
        """
        self.test_console_observer = self.test_abstract_factory.create_observer(self.test_file_lines[0][1])
        self.assertIsInstance(self.test_console_observer(self.test_file_lines[0]), ConsoleObserver)

        self.test_sms_observer = self.test_abstract_factory.create_observer(self.test_file_lines[2][1])
        self.assertIsInstance(self.test_sms_observer(self.test_file_lines[2]), SMSObserver)

        self.test_mail_observer = self.test_abstract_factory.create_observer(self.test_file_lines[1][1])
        self.assertIsInstance(self.test_mail_observer(self.test_file_lines[1]), MailObserver)

        with self.assertRaises(KeyError):
            self.test_abstract_factory.create_observer("Invalid Key")


if __name__ == '__main__':
    unittest.main()


