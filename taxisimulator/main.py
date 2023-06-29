from controller.controller import Controller
from repository.repository import Repository
from tests.tests import Tests
from ui.ui import Ui

if __name__ == '__main__':
    # Tests
    tests = Tests()
    tests.run_all_tests()

    # Setup application
    repository = Repository()
    controller = Controller(repository)
    ui = Ui(controller)

    # Start application
    ui.run_console()
