class RepositoryError(Exception):
    pass


class Repository:

    def __init__(self, path_to_file):
        self.__path_to_file = path_to_file
        self._sentences = []

    def read_all_from_file(self):
        """Reads all sentences form the text file"""
        with open(self.__path_to_file, "r") as file:
            lines = file.readlines()
            self._sentences.clear()
            for line in lines:
                line = line.strip()
                if line != "" and line != '\n':
                    try:
                        self._sentences.append(line)
                    except RepositoryError as repository_error:
                        pass

    def write_all_to_file(self):
        """Writes all valid sentences to the text file"""
        with open(self.__path_to_file, "w") as file:
            for sentence in self._sentences:
                file.write(sentence + "\n")

    def add_sentence(self, sentence):
        """Adds a sentence to the list and text file"""
        self.read_all_from_file()
        valid_sentence = True
        for character in sentence:
            if (33 <= ord(character) <= 64) or (91 <= ord(character) <= 96) or (123 <= ord(character) <= 126):
                valid_sentence = False
        if valid_sentence:
            for check_sentence in self._sentences:
                if check_sentence == sentence:
                    valid_sentence = False
            if valid_sentence:
                words = sentence.split(" ")
                for word in words:
                    if len(word) < 3:
                        valid_sentence = False
                if valid_sentence:
                    self._sentences.append(sentence)
                else:
                    raise RepositoryError("Oops! The sentence is not valid!")
            else:
                raise RepositoryError("Oops! Duplicate sentence!")
        else:
            raise RepositoryError("Oops! The sentence contains invalid elements!")
        self.write_all_to_file()

    def get_all_sentences(self):
        """Returns all sentences in the list"""
        self.read_all_from_file()
        return [sentence for sentence in self._sentences]

    def get_size(self):
        """Returns the size of the list"""
        self.read_all_from_file()
        return len(self._sentences)
