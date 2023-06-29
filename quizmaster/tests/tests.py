import unittest

from controller.controller import Controller
from entity.entities import Question
from repository.repository import Repository, RepositoryError
from ui.ui import Ui


class Tests(unittest.TestCase):

    def setUp(self) -> None:
        self.__repository = Repository("tests.txt")
        self.__controller = Controller(self.__repository)
        self.__ui = Ui(self.__controller)

    @staticmethod
    def clear_tests():
        """Clears the test file"""
        with open("tests.txt", "w"):
            pass

    def run_all_tests(self):
        self.clear_tests()
        self.setUp()
        self.test_add_question_repository()

    def test_add_question_repository(self):
        # Correct input
        question = Question(1, 'Which number is the largest', 1, 4, 3, 4, 'easy')
        self.__repository.add_question(question)
        self.assertEqual(self.__repository.get_size(), 1)

        # Wrong input
        question = Question(1, 'Which number is the largest', 1, 4, 3, 4, 'easyA')
        try:
            self.__repository.add_question(question)
            assert False
        except RepositoryError as repository_error:
            self.assertEqual(str(repository_error), "Oops! The difficulty of the question is not valid!")

    def test_add_question_controller(self):
        # Correct input
        self.__controller.add_question(1, 'Which number is the largest', 1, 4, 3, 4, 'easy')
        self.assertEqual(self.__controller.get_size(), 1)

        # Wrong input
        try:
            self.__controller.add_question(1, 'Which number is the largest', 1, 4, 3, 4, 'easyA')
            assert False
        except RepositoryError as repository_error:
            self.assertEqual(str(repository_error), "Oops! The difficulty of the question is not valid!")


if __name__ == '__main__':
    tests = Tests()
    tests.run_all_tests()
