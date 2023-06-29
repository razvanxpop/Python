class ReadTextFile:

    def __init__(self, patterns, path_to_file):
        self._patters = patterns
        self.__path_to_file = path_to_file

    def __read_all_from_file(self):
        """Reads cell patterns from text file"""
        with open(self.__path_to_file, "r") as file:
            lines = file.readline()
            self._patters.clear()
            for line in lines:
                if line != "":
                    pattern = line[6:13]
                    row = line[15]
                    column = line[17]
                    self.give_the_input(pattern, row, column)

    @staticmethod
    def give_the_input(pattern, row, column):
        """Returns the input from the text file"""
        return pattern, row, column
                