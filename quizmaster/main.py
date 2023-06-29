from controller.controller import Controller
from repository.repository import Repository
from ui.ui import Ui

if __name__ == '__main__':
    # Setup game
    path_to_file = "quiz.txt"
    repository = Repository(path_to_file)
    controller = Controller(repository)
    ui = Ui(controller)

    # Run game
    ui.start_game()
