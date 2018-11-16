import multiprocessing
from datetime import datetime
from threading import current_thread
from rx.subjects import Subject
from rx.concurrency import ThreadPoolScheduler
import threading
from Assignment_Four.WebNotifierFactoryClass import WebNotifierFactory

class WebNotifierLoader:
    """
    This is the base class for the Web Notifier Loader.  It allows for one to build
    a selection of observers and subjects by means of list of strings.  For the observers,
    the main collection includes a 'sms', 'console' and 'mail' objects while the subject includes
    'website'.
    """

    def __init__(self):
        """
        This is the constructor for the Web Notifier Loader class where the 'subject_dictionary' is being instantiated
        as well as the 'observer_dictionary'.  The 'subject_dictionary' contains an empty dictionary that will
        hold all of the website subjects while the 'observer_dictionary' will contain instructions for which
        observers are to be created.
        """
        self.web_notifier_factory = WebNotifierFactory()
        self.subject_dictionary = {}

    def load_notifier(self, notifier_instruction_list):
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
            self.subject_dictionary[web_address] = self.web_notifier_factory.create_subject(notifier_instruction_list)
        self.newly_built_website_subject = self.subject_dictionary[web_address]

        try:
            observer_type = self.web_notifier_factory.create_observer(notifier_instruction_list[1])
            observer_selection = observer_type(notifier_instruction_list)
            self.newly_built_website_subject.attach(observer_selection)
            self.subject_dictionary[web_address] = self.newly_built_website_subject
            return list(self.subject_dictionary.values())
        except:
            raise KeyError("There is no such key in dictionary.")

    def execute_web_notifiers(self, wait_interval=5000):
        """
        This is where we create the linkage between the subjects and the observers via RxPy. We create a
        separate thread per subject and in certain 'wait_intervals' check on whether or not the observers
        need to be updated.
        :return:
        """
        subject_list = list(self.subject_dictionary.values())
        optimal_thread_count = multiprocessing.cpu_count()
        pool_scheduler = ThreadPoolScheduler(optimal_thread_count)

        for web_subject in subject_list:
            Subject.interval(wait_interval).observe_on(pool_scheduler).subscribe(on_next=lambda s: web_subject.monitor())
