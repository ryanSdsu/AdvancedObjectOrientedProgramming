import unittest
from Assignment_Four.AbstractObserverClass import AbstractObserver

class TestAbstractSubjectClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Abstract Observer Class"""

    def setUp(self):
        """
        This is the set up for the 'Abstract Observer' class.  We are creating the 'Abstract Observer' object to be
        tested later.
        :return:
        """
        self.test_abstract_observer = AbstractObserver()

    def test_update_def(self):
        """
        This unit test is testing the update def of the 'Abstract Observer' class.  It passes when
        the update definition is executed and returns nothing.
        :return:
        """
        self.assertEqual(self.test_abstract_observer.update(), None)

if __name__ == '__main__':
    unittest.main()


