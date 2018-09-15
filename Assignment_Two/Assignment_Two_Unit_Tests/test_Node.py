import unittest
from Assignment_Two import NodeClass

class TestStudentClass(unittest.TestCase):

    def test_create_node(self):
        """
        This unit test is testing the creation of a 'Node' object. It passes when a Node of various types are created
        and compared to Nodes of similar types from the same class script of which they came.
        :return:
        """
        int_node = NodeClass.Node(1)
        self.assertIsInstance(NodeClass.Node(), type(int_node))
        string_node = NodeClass.Node("2")
        self.assertIsInstance(NodeClass.Node(), type(string_node))
        float_node = NodeClass.Node(3.0)
        self.assertIsInstance(NodeClass.Node(), type(float_node))
        list_node = NodeClass.Node([])
        self.assertIsInstance(NodeClass.Node(), type(list_node))
        multiple_argument_node = NodeClass.Node(1,2,3)
        self.assertIsInstance(NodeClass.Node(), type(multiple_argument_node))

if __name__ == '__main__':
    unittest.main()