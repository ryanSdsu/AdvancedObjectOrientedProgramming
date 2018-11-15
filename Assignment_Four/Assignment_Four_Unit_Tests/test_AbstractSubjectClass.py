import unittest
from Assignment_Four.AbstractSubjectClass import AbstractSubject

class TestAbstractSubjectClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Abstract Subject Class"""

    def setUp(self):
        """
        This is the set up for the 'Abstract Subject' class.  We are creating the 'Abstract Subject' object to be
        tested later.
        :return:
        """
        self.test_abstract_subject = AbstractSubject()


    def test_monitor_def(self):
        """
        This unit test is testing the monitor def of the 'Abstract Subject' class.  It passes when
        the monitor definition is executed and returns nothing.
        :return:
        """
        self.assertEqual(self.test_abstract_subject.monitor(), None)

    def test_attach_def(self):
        """
        This unit test is testing the attach def of the 'Abstract Subject' class.  It passes when
        the attach definition is executed and returns nothing.
        :return:
        """
        self.assertEqual(self.test_abstract_subject.attach(), None)

    def test_detach_def(self):
        """
        This unit test is testing the detach def of the 'Abstract Subject' class.  It passes when
        the detach definition is executed and returns nothing.
        :return:
        """
        self.assertEqual(self.test_abstract_subject.detach(), None)

if __name__ == '__main__':
    unittest.main()


