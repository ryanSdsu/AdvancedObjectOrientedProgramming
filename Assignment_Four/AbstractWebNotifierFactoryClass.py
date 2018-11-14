from Assignment_Four.SMSObserverClass import SMSObserver
from Assignment_Four.ConsoleObserverClass import ConsoleObserver
from Assignment_Four.MailObserverClass import MailObserver
from Assignment_Four.WebsiteSubjectClass import WebsiteSubject

class AbstractWebNotifierFactory:
    """
    This is the base class for the Abstract Web Notifier Factory.  It allows for one to build
    a selection of observers and subjects.  For the observers, the main collection
    includes a 'sms', 'console' and 'mail' objects while the subject includes
    'web'.
    """

    def create_web_subject(self, notifier_instruction):
        """
        This is where we create a web subject given a list of instructions.
        :param notifier_instruction: a list of string instructions
        :return:
        """
        return WebsiteSubject(notifier_instruction)

    def create_console_observer(self, notifier_instruction):
        """
        This is where we create a console observer given a list of instructions.
        :param notifier_instruction: a list of string instructions
        :return:
        """
        return ConsoleObserver(notifier_instruction)

    def create_mail_observer(self, notifier_instruction):
        """
        This is where we create a mail observer given a list of instructions.
        :param notifier_instruction: a list of string instructions
        :return:
        """
        return MailObserver(notifier_instruction)

    def create_sms_observer(self, notifier_instruction):
        """
        This is where we create a sms observer given a list of instructions.
        :param notifier_instruction: a list of string instructions
        :return:
        """
        return SMSObserver(notifier_instruction)