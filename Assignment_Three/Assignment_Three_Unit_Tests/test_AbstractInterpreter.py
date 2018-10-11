import unittest
import random
from Assignment_Three import AbstractInterpreterClass


class TestAbstractInterpreterClass(unittest.TestCase):
    """This is the base class for the Abstract Interpreter Class"""

    def setUp(self):
        """
        This is the set up for the 'AbstractInterpreter' class. We are creating the
        Abstract Interpreter which we will be inheriting/extending from.
        :return:
        """
        self.test_abstract_interpreter = AbstractInterpreterClass.AbstractInterpreter(None)

    def test_init_def(self):
        """
        This unit test is testing the __init__ def of the 'AbstractInterpreter' class.
        It passes when a 'AbstractInterpreter' class is successfully created along with its variable
        via 'expression' being instantiated as well.
        :return:
        """
        self.assertIsInstance(self.test_abstract_interpreter, AbstractInterpreterClass.AbstractInterpreter)
        self.assertEquals(self.test_abstract_interpreter.expression, None)

    def test_interpretation_of_expression(self):
        """
        This unit test is testing the 'interpretation_of_expression' def of the
        'AbstractInterpreter' class. It passes when the 'value' passed to it is successfully returned.
        :return:
        """
        self.assertEquals(self.test_abstract_interpreter.
                          interpretation_of_expression("some_value"), "some_value")

if __name__ == '__main__':
    unittest.main()


