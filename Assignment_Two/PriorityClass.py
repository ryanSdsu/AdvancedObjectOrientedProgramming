from Assignment_Two import StudentClass

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
    return (data)

def student(data = StudentClass.Student):
    """
    This is the student strategy used to determine the priority. It is set by creating normalized
    weights on the gpa (30%) as well as the number of units taken (70%).
    :param gpa: the gpa of the student (range: 0.0 - 4.0)
    :param number_of_units_taken: the number of units taken by the student (range: 0 - 150)
    :return:
    """
    from Assignment_Two import StudentClass

    gpa = data.gpa / 4.0
    gpa = gpa * 0.3
    number_of_units_taken = data.number_of_units_taken / 150
    number_of_units_taken = number_of_units_taken * 0.7
    priority = gpa + number_of_units_taken
    return priority