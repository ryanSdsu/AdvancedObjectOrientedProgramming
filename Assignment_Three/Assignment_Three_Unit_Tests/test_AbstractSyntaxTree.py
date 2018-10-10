import unittest
from Assignment_Three import AbstractSyntaxTreeClass
from Assignment_Three import NodeClass

class TestAbstractSyntaxTreeClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Abstract Syntax Tree Class"""

    def setUp(self):
        """
        This is the set up for the 'Abstract Syntax Tree Class' class. We are creating the
        'Node' objects to be set, added and tested later. As well as the Abstract Syntax
        Tree which we will be adding/deleting from.
        :return:
        """
        self.test_node = NodeClass.Node()
        self.test_abstract_syntax_tree = AbstractSyntaxTreeClass.AbstractSyntaxTree()

    def test_init_def(self):
        """
        This unit test is testing the __init__ def of the Abstract Syntax Tree Class class.
        It passes when a 'AbstractSyntaxTree' class is successfully created along with its variable
        via 'root_node' being instantiated as well.
        :return:
        """
        self.assertIsInstance(self.test_abstract_syntax_tree, AbstractSyntaxTreeClass.AbstractSyntaxTree)
        self.assertEquals(self.test_abstract_syntax_tree.root_node, None)
    #
    # def test_remove_all_trailing_whitespace(self):
    #     """
    #     This unit test is testing the 'remove_all_trailing_whitespace' def of the 'FileRead' class.
    #     It passes when the all of the lines in the 'file_lines' list have had any trailing whitespace
    #     be removed.
    #     :return:
    #     """
    #     self.test_file_read.remove_all_trailing_whitespace()
    #     self.assertListEqual(self.test_file_read.file_lines,
    #                          ['move 10', 'turn 90', 'move 20', 'turn -60', 'move 15'])
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


