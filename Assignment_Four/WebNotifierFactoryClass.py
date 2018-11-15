from Assignment_Four.AbstractNotifierFactoryClass import AbstractNotifierFactory
from Assignment_Four.SMSObserverClass import SMSObserver
from Assignment_Four.ConsoleObserverClass import ConsoleObserver
from Assignment_Four.MailObserverClass import MailObserver
from Assignment_Four.WebsiteSubjectClass import WebsiteSubject

class WebNotifierFactory(AbstractNotifierFactory):
    """
    This is the base class for the Web Notifier Factory.  It allows for one to build
    a selection of observers and subjects.  For the observers, the main collection
    includes a 'sms', 'console' and 'mail' objects while the subject includes
    'website'.
    """

    def create_observer(self, *choice_of_observer):
        """
        This is where we create an observer based on a given string.
        :param choice_of_observer: a string containing the choice of the desired observer
        :return: create_observer: the desired observer
        """
        self.observer_dictionary = {"sms" : (lambda x : SMSObserver(x)),
                                    "console" : (lambda x : ConsoleObserver(x)),
                                    "mail" : (lambda x : MailObserver(x))}
        try:
            self.chosen_observer = self.observer_dictionary[choice_of_observer[0]]
        except:
            raise KeyError("There is no such observer in the dictionary.")
        return self.chosen_observer

    def create_subject(self, *notifier_instruction):
        """
        This is where we create a web subject given a list of instructions.
        :param notifier_instruction: a list of string instructions
        :return: WebsiteSubject
        """
        return WebsiteSubject(notifier_instruction[0])