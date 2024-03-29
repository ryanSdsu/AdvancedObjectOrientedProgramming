from Assignment_Two import StudentClass
from Assignment_Two import NodeClass

class Priority:
    """This is the base class for the Priority Strategy."""
    def __init__(self, input):
        """
        This is the constructor of 'Priority' class in which the class strategy can be set.
        :param input: the strategy of which the 'Priority' class can be set to.
        """
        self.input = input

def default(data):
    """
    This is the default strategy used to determine the priority. It simply sets the priority
    to whatever is being passed into it.
    :param data: the value of which is being passed into the strategy
    :return:
    """
    return data

def node(node = NodeClass.Node):
    """
    This is the node strategy used to determine the priority. It simply sets the priority
    to whatever node data is being passed into it via the node class.
    :param data: the value of which is being passed into the strategy
    :return:
    """
    return lambda node: node.node_data

def student(student = StudentClass.Student):
    """
    This is the student strategy used to determine the priority. It is set by creating normalized
    weights on the gpa (30%) as well as the number of units taken (70%).
    :param gpa: the gpa of the student (range: 0.0 - 4.0)
    :param number_of_units_taken: the number of units taken by the student (range: 0 - 150)
    :return:
    """
    return lambda student: student.gpa / 4.0 * 0.3 + student.number_of_units_taken / 150 * 0.7