import smtplib
from Assignment_Four.AbstractObserverClass import AbstractObserver

class SMSObserver(AbstractObserver):
    """
    This is the base class for the SMS Observer.
    It essentially sends a text message whenever the subject tells
    it to call the definition 'update'.
    """
    def __init__(self, notifier_instruction_list):
        """
        This is the constructor for the SMSObserver class where the 'notifier_instruction_list' is being passed into
        the def to be read in and have certain elements be stored in various variables, specifically
        'sms_number', 'web_address' and 'carrier'.
        :param notifier_instruction_list: the string instructions that were given in a line via the .txt file
        """
        self.carrier_to_gateway_domain_dictionary = {
            'alltel' : '@mms.alltelwireless.com',
            'at&t' : '@mms.att.net',
            'att' : '@mms.att.net',
            'boost mobile' : '@myboostmobile.com',
            'cricket wireless' : '@mms.cricketwireless.net',
            'project fi' : '@msg.fi.google.com',
            'sprint' : '@pm.sprint.com',
            't-mobile' : '@tmomail.net',
            'u.s. cellular' : '@mms.uscc.net',
            'verizon' : '@vzwpix.com'
        }

        self.web_address = notifier_instruction_list[0]

        try:
            if type(int(notifier_instruction_list[2])) is int:
                self.sms_number = notifier_instruction_list[2]
        except:
            raise Exception("SMS Number: The SMS number must be of type 'int'")
        try:
            carrier_key = notifier_instruction_list[3:]
            carrier_key = ' '.join(carrier_key).lower()
            self.carrier_email = self.carrier_to_gateway_domain_dictionary[carrier_key]
        except:
            raise Exception("Carrier: The carrier provided does not have a valid gateway")

    def update(self):
        """
        This def sends a sms message whenever the subject updates the observer. It is using the email
        'jakewhitney86@gmail.com' as the outgoing. The incoming address is a combination of both the
        'sms_number' as well as the 'carrier_email' variables. And the message is using the 'web_address' variable.
        :return:
        """
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('jakewhitney86@gmail.com', 'JAKE123whitney')
        message = "The website '" + self.web_address + "' you're monitoring has been updated"
        server.sendmail("jakewhitney86@gmail.com", self.sms_number + self.carrier_email, message)
        server.quit()

    def __str__(self):
        """
        This is where we print a message stating the website has been updated.
        :return:
        """
        return "The website '" + self.web_address + "' you're monitoring has been updated"