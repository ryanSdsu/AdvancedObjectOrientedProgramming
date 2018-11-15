from Assignment_Four.AbstractObserverClass import AbstractObserver
from Assignment_Four.AbstractSubjectClass import AbstractSubject

class AbstractNotifierFactory():
    """
    This is the base class for the Abstract Notifier Factory.  It allows for one to build
    a selection of abstract observers and abstract subjects.  This will be inherited by the 'Web Notifier' factory
    for creating 'sms', 'console' and 'mail' observers, along with 'website' subjects.
    """

    def create_observer(self):
        """
        This is where we create observer object(s).
        """
        return AbstractObserver()

    def create_subject(self):
        """
        This is where we create subject object(s).
        """
        return AbstractSubject()
