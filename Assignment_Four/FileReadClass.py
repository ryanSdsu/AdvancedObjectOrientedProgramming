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

    def replace_characters_in_lines(self, characters_to_find, character_to_replace_with):
        """
        This is where we find a sequence of characters in the file lines and replace them
        with a new set of characters
        :param characters_to_find: the characters we want to find in each line
        :param character_to_replace_with: the characters that we want to replace with
        :return:
        """
        for index, line in enumerate(self.file_lines):
            self.file_lines[index]= line.replace(characters_to_find,character_to_replace_with)

    def split_lines_into_words(self):
        """
        This is where we split all of the lines in the file_lines list into individual words contained
        into separate lists.
        :return:
        """
        for index, line in enumerate(self.file_lines):
            self.file_lines[index] = line.split()

