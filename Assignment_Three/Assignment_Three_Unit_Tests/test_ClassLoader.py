import unittest
from Assignment_Three import ClassLoaderClass
from Assignment_Three import NodeClass

class TestClassLoaderClass(unittest.TestCase):
    """This is the base class for the unit test involving the Class Loader Class"""

    def test_init_def(self):
        """
        This unit test is testing the __init__ def of the 'ClassLoader' class.
        It passes when a 'ClassLoader' class is successfully created along with its 'class'
        type then being instantiated as well.
        :return:
        """
        self.test_class = ClassLoaderClass.ClassLoader("Assignment_Three", "NodeClass", "Node")
        self.assertEquals(self.test_class.class_object, NodeClass.Node)

    def test_get_class(self):
        """
        This unit test is testing the get_class def of the 'ClassLoader' class.  It passes when after
        executing the definition, if the 'class_object' is returned.
        :return:
        """
        self.test_class = ClassLoaderClass.ClassLoader("Assignment_Three", "NodeClass", "Node")
        self.test_class = self.test_class.get_class()
        self.assertEquals(self.test_class, NodeClass.Node)

if __name__ == '__main__':
    unittest.main()


