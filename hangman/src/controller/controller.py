import random

FIRST_WORD_LETTER = 0
LAST_WORD_LETTER = -1


class ControllerError(Exception):
    pass


class Controller:

    def __init__(self, repository):
        self.__repository = repository

    def add_sentence(self, sentence):
        """Adds a sentence"""
        self.__repository.add_sentence(sentence)

    def get_all_sentences(self):
        """Returns all sentences form the list"""
        return self.__repository.get_all_sentences()

    def get_size(self):
        """Returns the size of the list"""
        return self.__repository.get_size()

    def start_game(self):
        """Starts the game and displays a random sentence in hangman-style"""
        if self.__repository.get_size() == 0:
            raise ControllerError("Oops! There are no sentences left!")
        else:
            sentences = self.__repository.get_all_sentences()
            size = self.__repository.get_size()
            selected_sentence = random.randint(0, size)
            if selected_sentence == size:
                selected_sentence -= 1
            sentence = sentences[selected_sentence]
            words = sentence.split(" ")
            hangman_style_sentence = ""
            for word in words:
                if len(word) == 3:
                    hangman_style_sentence += word
                else:
                    hangman_style_sentence += word[FIRST_WORD_LETTER]
                    for letter in range(1, len(word)-1):
                        hangman_style_sentence += '_'
                    hangman_style_sentence += word[LAST_WORD_LETTER]
                hangman_style_sentence += " "
            return sentence, hangman_style_sentence[:-1]

    @staticmethod
    def show_letter(hangman_sentence, initial_sentence, letter):
        """Returns -1 if the letter does not apper in the sentence
        or if it does will return the sentence filled with the specified letter"""
        found_letter = False
        words = initial_sentence.split(" ")
        for word in words:
            if len(word) > 3:
                if letter in word[1:-1]:
                    found_letter = True

        if found_letter:
            new_hangman_sentence = ""
            for index_letter in range(len(initial_sentence)):
                if initial_sentence[index_letter] == letter:
                    new_hangman_sentence += letter
                else:
                    new_hangman_sentence += hangman_sentence[index_letter]
            return new_hangman_sentence
        else:
            return -1
