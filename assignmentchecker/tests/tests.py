import unittest

from controller.controller import Controller
from entity.entities import Assignment
from entity.validators import ValidateAssignment, ValidatorError
from repository.repository import Repository, RepositoryError


class Tests(unittest.TestCase):

    def run_all_tests(self):
        self.clear_test_file()
        self.setup()
        self.test_add_function_repository()
        self.test_add_function_controller()

    @staticmethod
    def clear_test_file():
        with open("tests.txt", "w"):
            pass

    def setup(self) -> None:
        self.repository = Repository("tests.txt")
        self.validator = ValidateAssignment()
        self.controller = Controller(self.repository, self.validator)

    def test_add_function_repository(self):
        assignment = Assignment(1, "Alex", "Draw an apple")
        self.repository.add_assignment(assignment)

        try:
            assignment = Assignment(1, "Luca", "History")
            self.repository.add_assignment(assignment)
        except RepositoryError as repository_error:
            self.assertEqual(str(repository_error), "Oops! Duplicate assignment id!")

    def test_add_function_controller(self):
        self.controller.add_assignment(102, "Daniel", "Math problem")

        try:
            self.controller.add_assignment(2, "Lu", "History")
        except ValidatorError as validator_error:
            self.assertEqual(str(validator_error), "Invalid student name!\n")
        try:
            self.controller.add_assignment(2, "Luca", "")
        except ValidatorError as validator_error:
            self.assertEqual(str(validator_error), "Invalid assignment solution!\n")
        try:
            self.controller.add_assignment(2, "Lu", "")
        except ValidatorError as validator_error:
            self.assertEqual(str(validator_error), "Invalid student name!\nInvalid assignment solution!\n")
