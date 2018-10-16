import unittest
from Assignment_Three import MementoVisitor
from Assignment_Three.CaretakerClass import Caretaker
from Assignment_Three.AbstractSyntaxTreeClass import AbstractSyntaxTree
from Assignment_Three.TurtleInterpreterClass import TurtleInterpreter
from Assignment_Three.FileReadClass import FileRead
from Assignment_Three import NodeClass
from Assignment_Three.TurtleClass import Turtle


class MementoVisitorClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Distance Collector Visitor Class"""

    def test_constructor(self):
        """
        This unit test is testing the instantiation of the 'DistanceColletorVisitor' class.
        It passes when a 'DistanceColletorVisitor' object is instantiated.
        :return:
        """
        self.test_memento_visitor = MementoVisitor.MementoVisitor()
        self.assertIsInstance(self.test_memento_visitor, MementoVisitor.MementoVisitor)

    def test_visit(self):
        """
        This unit test is testing the 'visit' definition of the
        'DistanceColletorVisitor' subclass.  It passes when the correct total amount of distance is
        returned based on a finished abstract syntax tree.
        :return:
        """
        self.test_memento_visitor = MementoVisitor.MementoVisitor()
        # First we need to read in the text file and convert the lines to strings.
        self.test_turtle_interpreter = TurtleInterpreter()
        self.test_abstract_syntax_tree = AbstractSyntaxTree()
        self.test_file_read = FileRead(
            "/Users/RJ/PycharmProjects/AdvancedObjectOrientedProgramming/Assignment_Three/sample_text_with_key")
        self.test_file_read.remove_all_trailing_whitespace()
        self.test_file_read.replace_characters_in_lines("=", " ")
        self.test_file_read.split_lines_into_words()
        self.list_of_string_commands = self.test_file_read.file_lines
        self.assertListEqual(self.list_of_string_commands,
                             [['#side', '15'], ['#side', '10'],
                              ['move', '#side'], ['turn', '90'], ['penDown'], ['move', '20'],
                              ['turn', '-60'], ['move', '15'], ['turn', '-30'],
                              ['repeat' ,'3'], ['move', '1'], ['end']])

        # Now we need to convert those strings to Turtle command nodes via the Turtle Interpreter.
        self.list_of_turtle_commands_nodes = []
        self.test_turtle = Turtle()
        for string_command in self.list_of_string_commands:
            interpreted_command = self.test_turtle_interpreter.string_to_class_interpreter(
                string_command, self.test_turtle)
            if interpreted_command:
                self.list_of_turtle_commands_nodes.append(NodeClass.Node(interpreted_command))

        # Now we need to load those turtle command nodes into the Abstract Syntax Tree
        for command_node in self.list_of_turtle_commands_nodes:
            self.test_abstract_syntax_tree.add_to_tree(command_node)

        # Now we need to execute the tree
        self.test_abstract_syntax_tree.execute_interpretation_tree(self.test_memento_visitor)
        self.assertEqual(self.test_turtle.location(), [25.99, 27.5])

        # Now we can check the visitor
        self.test_new_momento = self.test_memento_visitor.turtle_memento_caretaker.get_memento(0)
        self.test_new_momento.get_turtle_state(self.test_turtle)
        self.assertEqual(self.test_turtle.location(), [10,0])

if __name__ == '__main__':
    unittest.main()