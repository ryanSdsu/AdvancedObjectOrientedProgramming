import smtplib
from Assignment_Four.AbstractObserverClass import AbstractObserver

class MailObserver(AbstractObserver):
    """
    This is the base class for the Mail Observer.
    It essentially sends an email message whenever the subject tells
    it to call the definition 'update'.
    """
    def __init__(self, notifier_instruction_list):
        """
        This is the constructor for the MailObserver class where the 'notifier_instruction_list' is being passed into
        the def to be read in and have certain elements be stored in various variables, specifically
        'email_address' and 'web_address'.
        :param notifier_instruction_list: the string instructions that were given in a line via the .txt file
        """
        self.web_address = notifier_instruction_list[0]

        try:
            if "@" in str(notifier_instruction_list[2]):
                self.email_address = notifier_instruction_list[2]
        except TypeError:
            raise TypeError("A student email must be in a string format.")
        except AttributeError:
            raise AttributeError("A student email must be in a string format containing a '@' .")

    def update(self):
        """
        This def sends an email message whenever the subject updates the observer. It is using the email
        'jakewhitney86@gmail.com' as the outgoing. The incoming address is the 'email_address' variable. And the
        message is using the 'web_address' variable.
        :return:
        """
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('jakewhitney86@gmail.com', 'JAKE123whitney')
        message = "The website '" + self.web_address + "' you're monitoring has been updated"
        server.sendmail("jakewhitney86@gmail.com", self.email_address, message)
        server.quit()

    def __str__(self):
        """
        This is where we print a message stating the website has been updated.
        :return:
        """
        return "The website '" + self.web_address + "' you're monitoring has been updated"