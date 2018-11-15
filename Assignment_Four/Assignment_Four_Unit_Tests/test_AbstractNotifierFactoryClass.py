import unittest
from Assignment_Four.AbstractNotifierFactoryClass import AbstractNotifierFactory
from Assignment_Four.AbstractSubjectClass import AbstractSubject
from Assignment_Four.AbstractObserverClass import AbstractObserver

class TestAbstractNotifierFactoryClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Abstract Notifier Factory Class"""

    def setUp(self):
        """
        This is the set up for the 'Abstract Notifier Factory' class.  We are creating the
        'Abstract Notifier Factory' object to be tested later.
        :return:
        """
        self.test_abstract_factory = AbstractNotifierFactory()

    def test_create_observer_def(self):
        """
        This unit test is testing the create_observer def of the 'Abstract Notifier Factory' class.
        It passes when the definition is executed and returns an Abstract Observer.
        :return:
        """
        self.test_abstract_observer = self.test_abstract_factory.create_observer()
        self.assertIsInstance(self.test_abstract_observer, AbstractObserver)

    def test_create_subject_def(self):
        """
        This unit test is testing the create_subject def of the 'Abstract Notifier Factory' class.
        It passes when the definition is executed and returns an Abstract Subject.
        :return:
        """
        self.test_abstract_subject = self.test_abstract_factory.create_subject()
        self.assertIsInstance(self.test_abstract_subject, AbstractSubject)


if __name__ == '__main__':
    unittest.main()


