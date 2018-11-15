import smtplib
from Assignment_Four.AbstractObserverClass import AbstractObserver

class ConsoleObserver(AbstractObserver):
    """
    This is the base class for the Console Observer.
    It essentially prints a message whenever the subject tells
    it to call the definition 'update'.
    """
    def __init__(self, notifier_instruction_list):
        """
        This is the constructor for the ConsoleObserver class where the 'notifier_instruction_list' is being passed into
        the def to be read in and have certain elements be stored in various variables specifically 'web_address'
        which is url of the page being monitored.
        :param notifier_instruction_list: the string instructions that were given in a line via the .txt file
        """
        self.web_address = notifier_instruction_list[0]

    def update(self):
        """
        This def prints a message whenever the subject updates the observer.
        :return:
        """
        print(self)

    def __str__(self):
        """
        This is where we print a message stating the website has been updated.
        :return:
        """
        return "The website '" + self.web_address + "' you're monitoring has been updated"