class AbstractObserver():
    """
    This is the base class for the Abstract Observer.
    It essentially contains an 'update' definition which can and will be used to update a certain state/metric.
    It is the template for which the 'sms', 'console' and 'mail' observers will inherit.
    """

    def update(self):
        """
        This def updates the observer with a certain specific amount of functionality. Its use is
        dependent on what the subject has and will be presenting to them.
        :return:
        """
        pass