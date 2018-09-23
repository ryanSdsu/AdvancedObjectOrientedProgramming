class CommandInvoker():

    def __init__(self):
        self.undo_stack = []

    def execute_command(self, command):
        try:
            command.execute()
            self.undo_stack.append(command)
            return
        except:
            raise ValueError("{} was an invalid commands for which to execute.".format(command))

    def undo_command(self):
        if not self.undo_stack:
            raise ValueError("There are currently no commands for which to undo.")
        command = self.undo_stack.pop()
        command.undo()
