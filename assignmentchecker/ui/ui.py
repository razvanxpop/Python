from entity.validators import ValidatorError
from repository.repository import RepositoryError


ADD_ASSIGNMENT = 1
DISPLAY_ALL_ASSIGNMENTS = 2
DISHONESTY_CHECK = 3
EXIT = 0


class Ui:

    def __init__(self, controller):
        self.__controller = controller

    @staticmethod
    def menu():
        """The console-based menu of the application"""
        print("[1] Add an assignment.")
        print("[2] Display all assignments.")
        print("[3] Dishonesty check.")
        print("[0] Exit")

    def add_assignment(self, assignment_id, student_name, solution):
        """Adds an assignment"""
        try:
            assignment_id = int(assignment_id)
            self.__controller.add_assignment(assignment_id, student_name, solution)
        except ValidatorError as validator_error:
            print(validator_error)
        except RepositoryError as repository_error:
            print(repository_error)
        except ValueError as value_error:
            print(value_error)

    def display_all_assignments(self):
        """Displays all assignments"""
        print(*self.__controller.get_all_assignments(), sep='\n')

    def display_dishonesty_check(self):
        """Displays all students pairs where at least 20% of the words in the solution are common"""
        print(*self.__controller.dishonesty_check(), sep='\n')

    def run_console(self):
        while True:
            self.menu()
            valid_option = False
            option = 0
            while not valid_option:
                try:
                    option = int(input("Type your option:"))
                    valid_option = True
                except ValueError as value_error:
                    print(value_error)
            if option == ADD_ASSIGNMENT:
                assignment_id = input("Type the id of the assignment:")
                student_name = input("Type the name of the student:")
                solution = input("Type the solution:")
                self.add_assignment(assignment_id, student_name, solution)
            elif option == DISPLAY_ALL_ASSIGNMENTS:
                self.display_all_assignments()
            elif option == DISHONESTY_CHECK:
                self.display_dishonesty_check()
            elif option == EXIT:
                break
            else:
                print("Oops! This option is not yet implemented", option)
