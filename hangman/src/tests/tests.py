import unittest

from src.controller.controller import Controller
from src.repository.repository import Repository, RepositoryError
from src.ui.ui import Ui


class Tests(unittest.TestCase):

    def setUp(self) -> None:
        self.__repository = Repository("tests.txt")
        self.__controller = Controller(self.__repository)
        self.__ui = Ui(self.__controller)

    def run_all_tests(self):
        self.setUp()
        self.test_add_sentence_repository()
        self.test_add_sentence_controller()
        self.test_add_sentence_ui()
        self.test_start_game_controller()
        # self.test_start_game_ui()
        self.test_show_letter_controller()

    def test_add_sentence_repository(self):
        """Test add function in repository"""
        # Wrong input
        sentence = "The sentence is not valid"
        try:
            self.__repository.add_sentence(sentence)
        except RepositoryError as repository_error:
            self.assertEqual(str(repository_error), "Oops! The sentence is not valid!")

        # Correct input
        sentence = "That animal has four legs"
        self.__repository.add_sentence(sentence)
        try:
            self.__repository.add_sentence(sentence)
        except RepositoryError as repository_error:
            self.assertEqual(str(repository_error), "Oops! Duplicate sentence!")

    def test_add_sentence_controller(self):
        """Test add function in controller"""
        # Wrong input
        sentence = "The sentence is not valid"
        try:
            self.__controller.add_sentence(sentence)
            assert False
        except RepositoryError as repository_error:
            self.assertEqual(str(repository_error), "Oops! The sentence is not valid!")

        # Correct input
        sentence = "That animal has two eyes"
        self.__controller.add_sentence(sentence)
        try:
            self.__controller.add_sentence(sentence)
        except RepositoryError as repository_error:
            self.assertEqual(str(repository_error), "Oops! Duplicate sentence!")

    def test_add_sentence_ui(self):
        """Test add function in ui"""

        # Wrong input
        sentence = "The sentence is not valid"
        try:
            self.__ui.add_sentence(sentence)
        except RepositoryError as repository_error:
            self.assertEqual(str(repository_error), "Oops! The sentence is not valid!")

        # Correct input
        sentence = "That bird has two legs"
        self.__ui.add_sentence(sentence)
        try:
            self.__ui.add_sentence(sentence)
        except RepositoryError as repository_error:
            self.assertEqual(str(repository_error), "Oops! Duplicate sentence!")

    def test_start_game_controller(self):
        """Tests the start game function from the controller"""
        self.assertEqual(self.__controller.get_size(), 3)
        sentence, hangman_sentence = self.__controller.start_game()
        self.assertEqual(hangman_sentence in ['T__t b__d has two l__s', "T__t a____l has two e__s",
                                              "T__t a____l has f__r l__s"], 1)

    # def test_start_game_ui(self):
    #     """Tests the start game function from the ui"""
    #     self.assertEqual(self.__controller.get_size(), 1)
    #     hangman_sentence = self.__ui.start_game()
    #     self.assertEqual(hangman_sentence, "T__t b__d has two l__g")

    def test_show_letter_controller(self):
        """Tests the show letter function from the controller"""
        self.assertEqual(self.__controller.get_size(), 3)
        self.assertEqual(self.__controller.show_letter('T__t b__d has two l__s', "That bird has two legs", 'x'), -1)
        self.assertEqual(self.__controller.show_letter('T__t b__d has two l__s', "That bird has two legs", 'a'),
                                                       'T_at b__d has two l__s')


if __name__ == '__main__':
    tests = Tests()
    tests.run_all_tests()
