class AbstractSubject():
    """
    This is the base class for the Abstract Subject.
    It essentially contains a 'monitor', 'attach' and 'detach' definition which can and will
    be used in conjunction with the Observer class.  This is also the template for which the
    'Website' subject will inherit.
    """

    def monitor(self):
        """
        This is where we monitor the observer(s) and execute a change on them that should happen.
        """
        pass

    def attach(self):
        """
        This is where we attach an observer to the subject.
        """
        pass

    def detach(self):
        """
        This is where we detach an observer from the subject.
        """
        pass