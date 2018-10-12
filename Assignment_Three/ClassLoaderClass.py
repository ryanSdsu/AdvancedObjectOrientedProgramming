class ClassLoader:
    """This is the base class for the Class Loader"""
    def __init__(self, module_name, file_name, class_name):
        """
        This allows one to dynamically load a class into a variable in real-time.
        :param module_name: the name of the module to be loaded
        :param file_name: the file to be loaded
        :param class_name: the class name to be loaded
        """
        self.module = __import__(module_name, fromlist=[file_name])
        self.file_object = getattr(self.module, file_name)
        self.class_object = getattr(self.file_object, class_name)

    def get_class(self):
        """
        This returns the class object which was dynamically loaded.
        :return: class_object
        """
        return self.class_object
