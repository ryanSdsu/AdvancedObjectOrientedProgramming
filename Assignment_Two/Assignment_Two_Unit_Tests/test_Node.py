import unittest
from Assignment_Two import NodeClass

class TestNodeClass(unittest.TestCase):

    def test_init_def(self):
        """
        This unit test is testing the init of a 'Node' object. It passes when a Node of various types are created
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

    def test_data_variable(self):
        """
        This unit test is testing the 'data' variable of the 'Node' class. It passes when upon proceeding with the
        __init__() def that 'data' is being set to its arguments (it will be in a list form if there is more
        than 1 argument) and it will be set to "None" if no arguments are being passed.
        :return:
        """
        none_node = NodeClass.Node()
        self.assertEquals(none_node.data, None)
        one_argument_node = NodeClass.Node(1)
        self.assertEquals(one_argument_node.data, 1)
        multiple_argument_node = NodeClass.Node("Hi!", "I'm", "a", "Node")
        self.assertEquals(multiple_argument_node.data, ["Hi!", "I'm", "a", "Node"])

if __name__ == '__main__':
    unittest.main()