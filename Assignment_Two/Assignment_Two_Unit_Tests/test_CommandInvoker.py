import unittest
from Assignment_Two import PriorityQueueClass
from Assignment_Two import CommandInvokerClass
from Assignment_Two import PriorityQueueAddCommandClass
from Assignment_Two import PriorityQueueRemoveCommandClass

class TestCommandInvokerClass(unittest.TestCase):
    """This is the base class for the unit tests involving the Command Invoker Class"""
    def setUp(self):
        """
        This is the set up for the 'CommandInvoker' class. We are creating the 'PriorityQueue' class to
        be invoked later.
        :return:
        """
        self.test_priority_queue = PriorityQueueClass.PriorityQueue()

    def test_init_def(self):
        """
        This unit test is testing the __init__ def of a 'CommandInvoker' class. It passes when a 'CommandInvoker'
        is successfully created along with the undo stack.
        :return:
        """
        command_invoker = CommandInvokerClass.CommandInvoker()
        self.assertIsInstance(command_invoker, CommandInvokerClass.CommandInvoker)
        self.assertListEqual(command_invoker.undo_stack, [])

    def test_execute_def(self):
        """
        This unit test is testing the execute_command def of the 'CommandInvoker' class. It passes when a
        successful command is invoked along with the undo stack. In this case we will be attempting to test
        the executes of the PriorityQueueAddCommand class as well as the PriorityQueueRemoveCommand class.
        :return:
        """
        command_invoker = CommandInvokerClass.CommandInvoker()
        add_command = lambda: PriorityQueueAddCommandClass.PriorityQueueAddCommand(1, self.test_priority_queue)
        add_command = PriorityQueueAddCommandClass.PriorityQueueAddCommand(1, self.test_priority_queue)
        remove_command = PriorityQueueRemoveCommandClass.PriorityQueueRemoveCommand(self.test_priority_queue)
        command_invoker.execute_command(add_command)
        self.assertListEqual(self.test_priority_queue.get_all_data_from_priority_queue(), [1])
        self.assertListEqual(command_invoker.undo_stack, [add_command])
        command_invoker.execute_command(remove_command)
        self.assertListEqual(self.test_priority_queue.get_all_data_from_priority_queue(), [])
        self.assertListEqual(command_invoker.undo_stack, [add_command, remove_command])

    def test_undo_def(self):
        """
        This unit test is testing the undo_command def of the 'CommandInvoker' class. It passes when a
        successful command is invoked along with the undo stack. In this case we will be attempting to test
        the undo of the PriorityQueueAddCommand class as well as the PriorityQueueRemoveCommand class.
        :return:
        """
        command_invoker = CommandInvokerClass.CommandInvoker()
        add_one_command = PriorityQueueAddCommandClass.PriorityQueueAddCommand(1, self.test_priority_queue)
        add_two_command = PriorityQueueAddCommandClass.PriorityQueueAddCommand(2, self.test_priority_queue)
        add_three_command = PriorityQueueAddCommandClass.PriorityQueueAddCommand(3, self.test_priority_queue)
        add_four_command = PriorityQueueAddCommandClass.PriorityQueueAddCommand(4, self.test_priority_queue)
        command_invoker.execute_command(add_one_command)
        command_invoker.execute_command(add_two_command)
        command_invoker.execute_command(add_three_command)
        command_invoker.execute_command(add_four_command)
        self.assertEquals(self.test_priority_queue.get_data_from_priority_queue_index(0),4)
        self.assertListEqual(command_invoker.undo_stack,
                             [add_one_command, add_two_command, add_three_command, add_four_command])
        command_invoker.undo_command()
        self.assertEquals(self.test_priority_queue.get_data_from_priority_queue_index(0),3)
        self.assertListEqual(command_invoker.undo_stack,
                             [add_one_command, add_two_command, add_three_command])
        command_invoker.undo_command()
        self.assertEquals(self.test_priority_queue.get_data_from_priority_queue_index(0),2)
        self.assertListEqual(command_invoker.undo_stack,
                             [add_one_command, add_two_command])
        command_invoker.undo_command()
        self.assertEquals(self.test_priority_queue.get_data_from_priority_queue_index(0),1)
        self.assertListEqual(command_invoker.undo_stack,
                             [add_one_command])
        command_invoker.undo_command()
        self.assertEqual(len(self.test_priority_queue.get_priority_queue()), 0)
        self.assertListEqual(command_invoker.undo_stack,[])

if __name__ == '__main__':
    unittest.main()


