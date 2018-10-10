import unittest
from Assignment_Three import AbstractSyntaxTreeClass
from Assignment_Three import NodeClass

class TestAbstractSyntaxTreeClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Abstract Syntax Tree Class"""

    def setUp(self):
        """
        This is the set up for the 'AbstractSyntaxTree' class. We are creating the
        Abstract Syntax Tree which we will be adding/deleting from.
        :return:
        """
        self.test_abstract_syntax_tree = AbstractSyntaxTreeClass.AbstractSyntaxTree()

    def test_init_def(self):
        """
        This unit test is testing the __init__ def of the 'AbstractSyntaxTree' class.
        It passes when a 'AbstractSyntaxTree' class is successfully created along with its variable
        via 'root_node' being instantiated as well.
        :return:
        """
        self.assertIsInstance(self.test_abstract_syntax_tree, AbstractSyntaxTreeClass.AbstractSyntaxTree)
        self.assertEquals(self.test_abstract_syntax_tree.root_node, None)

    def test_add_to_tree(self):
        """
        This unit test is testing the 'add_to_tree' def of the 'AbstractSyntaxTree' class.
        It passes when a new 'node' is added to the tree and if the 'root_node' has not yet been
        set to anything, it will be set to it before starting to branch off.
        :return:
        """
        zero_node = NodeClass.Node([0,0])
        self.test_abstract_syntax_tree.add_to_tree(zero_node)
        self.assertEquals(self.test_abstract_syntax_tree.root_node.node_data, 0)
        self.assertEquals(self.test_abstract_syntax_tree.root_node.left_child, None)
        self.assertEquals(self.test_abstract_syntax_tree.root_node.right_child.node_data, 0)

        first_node = NodeClass.Node([1,1])
        self.test_abstract_syntax_tree.add_to_tree(first_node)
        self.assertEquals(self.test_abstract_syntax_tree.root_node.node_data, 0)
        self.assertEquals(self.test_abstract_syntax_tree.root_node.left_child.node_data, 1)
        self.assertEquals(self.test_abstract_syntax_tree.root_node.right_child.node_data, 0)

        self.assertEquals(self.test_abstract_syntax_tree.root_node.left_child.left_child, None)
        self.assertEquals(self.test_abstract_syntax_tree.root_node.left_child.right_child.node_data, 1)

        second_node = NodeClass.Node([2, 2])
        self.test_abstract_syntax_tree.add_to_tree(second_node)
        self.assertEquals(self.test_abstract_syntax_tree.root_node.node_data, 0)
        self.assertEquals(self.test_abstract_syntax_tree.root_node.left_child.node_data, 1)
        self.assertEquals(self.test_abstract_syntax_tree.root_node.right_child.node_data, 0)

        self.assertEquals(self.test_abstract_syntax_tree.root_node.left_child.left_child.node_data, 2)
        self.assertEquals(self.test_abstract_syntax_tree.root_node.left_child.right_child.node_data, 1)

        self.assertEquals(self.test_abstract_syntax_tree.root_node.
                          left_child.left_child.left_child, None)
        self.assertEquals(self.test_abstract_syntax_tree.root_node.
                          left_child.left_child.right_child.node_data, 2)

        second_node = NodeClass.Node([3, 3])
        self.test_abstract_syntax_tree.add_to_tree(second_node)
        self.assertEquals(self.test_abstract_syntax_tree.root_node.node_data, 0)
        self.assertEquals(self.test_abstract_syntax_tree.root_node.left_child.node_data, 1)
        self.assertEquals(self.test_abstract_syntax_tree.root_node.right_child.node_data, 0)

        self.assertEquals(self.test_abstract_syntax_tree.root_node.left_child.left_child.node_data, 2)
        self.assertEquals(self.test_abstract_syntax_tree.root_node.left_child.right_child.node_data, 1)

        self.assertEquals(self.test_abstract_syntax_tree.root_node.
                          left_child.left_child.left_child.node_data, 3)
        self.assertEquals(self.test_abstract_syntax_tree.root_node.
                          left_child.left_child.right_child.node_data, 2)

        self.assertEquals(self.test_abstract_syntax_tree.root_node.
                          left_child.left_child.left_child.left_child, None)
        self.assertEquals(self.test_abstract_syntax_tree.root_node.
                          left_child.left_child.left_child.right_child.node_data, 3)

        #
    # def test_split_lines_into_words(self):
    #     """
    #     This unit test is testing the 'split_lines_into_words' def of the 'FileRead' class.
    #     It passes when the all of the lines in the 'file_lines' list have had any trailing whitespace
    #     be removed and then are reorganized into lists containing each individual word per
    #     their respective line.
    #     :return:
    #     """
    #     self.test_file_read.split_lines_into_words()
    #     self.assertListEqual(self.test_file_read.file_lines,
    #                          [['move', '10'], ['turn', '90'], ['move', '20'],
    #                           ['turn', '-60'], ['move', '15']])

if __name__ == '__main__':
    unittest.main()


