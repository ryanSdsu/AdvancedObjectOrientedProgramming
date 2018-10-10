import unittest
import random
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

        third_node = NodeClass.Node([3, 3])
        self.test_abstract_syntax_tree.add_to_tree(third_node)
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

    def test_init_def(self):
        """
        This unit test is testing the __init__ def of the 'AbstractSyntaxTree' class.
        It passes when a 'AbstractSyntaxTree' class is successfully created along with its variable
        via 'root_node' being instantiated as well.
        :return:
        """
        self.assertIsInstance(self.test_abstract_syntax_tree, AbstractSyntaxTreeClass.AbstractSyntaxTree)
        self.assertEquals(self.test_abstract_syntax_tree.root_node, None)

    def test_iter(self):
        """
        This unit test is testing the '__iter__' def of the 'AbstractSyntaxTree' class.
        It passes when upon being iterated through (i.e. '__next__'), the first node which
        was added via the tree gets returned followed by the previous one and then the one
        after until there are no more nodes left on the tree.
        :return:
        """
        samples = random.sample(list(range(101, 200)),50)
        for new_node_value in samples:
            new_node = NodeClass.Node([new_node_value, new_node_value])
            self.test_abstract_syntax_tree.add_to_tree(new_node)

        for index, node in enumerate(self.test_abstract_syntax_tree):
            self.assertListEqual(node, [samples[index],samples[index]])

if __name__ == '__main__':
    unittest.main()


