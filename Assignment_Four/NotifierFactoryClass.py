from Assignment_Four.SMSObserverClass import SMSObserver
from Assignment_Four.ConsoleObserverClass import ConsoleObserver
from Assignment_Four.MailObserverClass import MailObserver
from Assignment_Four.WebsiteSubjectClass import WebsiteSubject


class NotifierFactory:
    """
    This is the base class for the Notifier Factory.  It allows for one to build
    a selection of observers and subjects.  For the observers, the main collection
    includes a 'sms', 'console' and 'mail' objects while the subject includes
    'website'.
    """

    def __init__(self):
        """
        This is the constructor for the Notifier Factory class where the 'subject_dictionary' is being instantiated
        as well as the 'observer_dictionary'.  The 'subject_dictionary' contains an empty dictionary that will
        hold all of the website subjects while the 'observer_dictionary' will contain instructions for which
        observers are to be created.
        """
        self.observer_dictionary = {"sms" : (lambda x : SMSObserver(x)),
                                   "console": (lambda x : ConsoleObserver(x)),
                                   "mail" : (lambda x : MailObserver(x))}
        self.subject_dictionary = {}

    def create_notifier(self, notifier_instruction_list):
        """
        This is where we create a notifier and update the subject dictionary based on the instructions that
        are given via a list of strings. The website url acts as a key and the creation of a website subject
        acts as the value.  The proper observer is also selected before attaching it to the website subject itself.
        :param notifier_instruction_list: the list of instructions needed to create both the subject and observer
        :return: subject_dictionary_values: a list of all the website subject objects
        """
        self.newly_built_website_subject = None

        web_address = notifier_instruction_list[0]
        if web_address not in self.subject_dictionary:
            print("not in here")
            self.subject_dictionary[web_address] = WebsiteSubject(web_address)


        self.newly_built_website_subject = self.subject_dictionary[web_address]
        print(self.subject_dictionary)
        # print(type(self.newly_built_website_subject))
        try:
            observer_selection = self.observer_dictionary[notifier_instruction_list[1]]
            self.newly_built_website_subject.attach(observer_selection)
            self.subject_dictionary[web_address] = self.newly_built_website_subject
            return self.subject_dictionary.values()
        except:
            raise KeyError("There is no such key in dictionary.")