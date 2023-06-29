from src.controller.controller import Controller
from src.repository.repository import Repository
from src.tests.tests import Tests
from src.ui.ui import Ui

if __name__ == '__main__':
    # Setup
    path_to_file = "sentences.txt"
    repository = Repository(path_to_file)
    controller = Controller(repository)
    ui = Ui(controller)

    # Run program
    ui.run_game()


