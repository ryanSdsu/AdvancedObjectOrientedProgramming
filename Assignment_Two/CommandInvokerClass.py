class CommandInvoker():
    """This is the base class for the Command Invoker."""
    def __init__(self):
        """
        This is the constructor for the command invoker. It has an undo stack for which to store the undo commands.
        """
        self.undo_stack = []

    def execute_command(self, command):
        """
        This is where we execute the commands of whatever is passed and then store it's undo for a possible
        future reference.
        :param command:
        :return:
        """
        try:
            command.execute()
            self.undo_stack.append(command)
            return
        except:
            raise ValueError("{} was an invalid commands for which to execute.".format(command))

    def undo_command(self):
        """
        This is where we perform the undo commands by popping them off of the undo stack.
        :return:
        """
        if not self.undo_stack:
            raise ValueError("There are currently no commands for which to undo.")
        command = self.undo_stack.pop()
        command.undo()
