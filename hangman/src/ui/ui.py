from src.controller.controller import ControllerError
from src.repository.repository import RepositoryError

FIRST_LETTER = 'h'
SECOND_LETTER = 'a'
THIRD_LETTER = 'n'
FORTH_LETTER = 'g'
FIFTH_LETTER = 'm'
SIXTH_LETTER = 'a'
SEVENTH_LETTER = 'n'

ADD_SENTENCE = 1
START_GAME = 2
PLAY_GAME = 3
EXIT_GAME = 0


class Ui:

    def __init__(self, controller):
        self.__controller = controller

    @staticmethod
    def menu():
        print("[1] Add a sentence.")
        print("[2] Start the game.")
        print("[3] Play the game.")
        print("[0] Exit the game.")

    def add_sentence(self, sentence):
        """Adds a sentence"""
        try:
            sentence = str(sentence)
            self.__controller.add_sentence(sentence)
        except RepositoryError as repository_error:
            print(repository_error)
        except ValueError as value_error:
            print(value_error)

    def start_game(self):
        """Starts the game"""
        try:
            sentence, hangman = self.__controller.start_game()
            print(hangman)
        except ControllerError as controller_error:
            print(controller_error)

    def play_game(self):
        """Play the game function ( makes the game run ) """
        game_over = False
        hangman = ""
        initial_sentence = ""
        hangman_sentence = ""
        try:
            initial_sentence, hangman_sentence = self.__controller.start_game()
        except ControllerError as controller_error:
            print(controller_error)

        if initial_sentence != "":
            while not game_over:
                print(hangman_sentence, '|', hangman, sep='\t')
                letter = input("Guess a letter: ")
                new_hangman_sentence = self.__controller.show_letter(hangman_sentence, initial_sentence, letter)

                if new_hangman_sentence == -1:
                    if len(hangman) == 0:
                        hangman += FIRST_LETTER
                    elif len(hangman) == 1:
                        hangman += SECOND_LETTER
                    elif len(hangman) == 2:
                        hangman += THIRD_LETTER
                    elif len(hangman) == 3:
                        hangman += FORTH_LETTER
                    elif len(hangman) == 4:
                        hangman += FIFTH_LETTER
                    elif len(hangman) == 5:
                        hangman += SIXTH_LETTER
                    else:
                        hangman += SEVENTH_LETTER
                else:
                    hangman_sentence = new_hangman_sentence

                if hangman == 'hangman':
                    game_over = True
                    print(initial_sentence, 'You lost the game...')
                elif initial_sentence == hangman_sentence:
                    game_over = True
                    print(initial_sentence, "You won the game !!")

    def run_game(self):
        exit_game = False
        while not exit_game:
            self.menu()
            valid_option = False
            option = 0
            while not valid_option:
                try:
                    option = int(input("Select the option:"))
                    valid_option = True
                except ValueError as value_error:
                    print(value_error)
            if option == ADD_SENTENCE:
                sentence = input("Type your sentence: ")
                self.add_sentence(sentence)
            elif option == START_GAME:
                self.start_game()
            elif option == PLAY_GAME:
                self.play_game()
            elif option == EXIT_GAME:
                exit_game = True
            else:
                print("Oops! This option is not yet implemented:", option)
