class FileRead:
    """This is the base class for FileRead Class"""

    def __init__(self, file_path):
        """
        This is the constructor for the FileRead class where the 'file_path' is being passed into
        the def to be read in and have each of the lines stored in the 'file_lines' variable.
        :param file_path:
        """
        self.file = open(file_path, "r")
        self.file_lines = self.file.readlines()

    def remove_all_trailing_whitespace(self):
        """
        This is where we remove all of the whitespace from the file lines in the 'file_lines' variable.
        :return:
        """
        for index, line in enumerate(self.file_lines):
             self.file_lines[index]= line.rstrip()