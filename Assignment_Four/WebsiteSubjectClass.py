import urllib.request
from time import sleep

class WebsiteSubject:
    """
    This is the base class for the Website Subject.
    It essentially can 'attach/remove' observers of all types and initiate a call via 'update' i.e.
    informing them of a modification that happens via a specific 'web_address'.
    """
    def __init__(self, web_address):
        """
        This is the constructor for the Website Subject class where the 'web_address' is being passed into
        the def to be read in/set.
        :param web_address: the url of which the Website subject will monitor
        """
        self.last_reported_web_address_modified_time = None
        self.currently_attached_observers = []
        try:
            self.web_address = str(web_address)
        except:
            raise Exception("The URL could not be converted via type: str.")

    def monitor(self):
        """
        This is where we monitor the website once every hour in order to inform the
        observers of whenever a change happens during that time frame.
        :return:
        """
        web_address_response = urllib.request.urlopen(self.web_address)
        web_address_modified_time = str(web_address_response.info().get('Last-Modified'))
        self.last_reported_web_address_modified_time = web_address_modified_time

        while True:
            web_address_response = urllib.request.urlopen(self.web_address)
            web_address_modified_time = str(web_address_response.info().get('Last-Modified'))
            if web_address_modified_time != self.last_reported_web_address_modified_time:
                self.last_reported_web_address_modified_time = web_address_modified_time
                for observer in self.currently_attached_observers:
                    observer.update()
            sleep(3)

    def attach(self, observer):
        """
        This is where we attach an observer to the subject for which it will now be updated via the
        monitor def.
        :param observer: an observer that will be attached to the subject
        :return:
        """
        self.currently_attached_observers.append(observer)

    def detach(self, observer):
        """
        This is where we detach an observer from the subject, preventing it from being updated via the
        monitor def.
        :param observer: an observer that will be detached from the subject
        :return:
        """
        try:
            self.currently_attached_observers.remove(observer)
        except:
            raise Exception("The observer could not be removed.")
