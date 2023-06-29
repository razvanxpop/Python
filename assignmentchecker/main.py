from controller.controller import Controller
from entity.validators import ValidateAssignment
from repository.repository import Repository
from tests.tests import Tests
from ui.ui import Ui


if __name__ == '__main__':
    # Tests
    tests = Tests()
    tests.run_all_tests()

    # Setup application
    path_to_file = "assignments.txt"
    repository = Repository(path_to_file)
    assignment_validator = ValidateAssignment()
    controller = Controller(repository, assignment_validator)
    ui = Ui(controller)

    # Run application
    ui.run_console()
