class Priority:
    def __init__(self, input):
        self.input = input

def student(gpa, number_of_units_taken):
    gpa = gpa / 4.0
    gpa = gpa * 0.3
    number_of_units_taken = number_of_units_taken / 150
    number_of_units_taken = number_of_units_taken * 0.7
    priority = gpa + number_of_units_taken
    return priority

def faculty(years_of_service):
    return years_of_service

def employee():
    print("employees")

def retiree():
    print("retiree")

def intern():
    print("intern")
