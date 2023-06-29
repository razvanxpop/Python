from repository.repository import RepositoryError

ADD_A_QUESTION = 'add'
CREATE_NEW_QUIZ = 'create'
START_A_QUIZ = 'start'
EXIT_GAME = 'exit'


class Ui:

    def __init__(self, controller):
        self.__controller = controller

    @staticmethod
    def read_command():
        """This function reads the user command and returns the command and its arguments"""
        user_command = input(">")
        first_character_found = False
        while not first_character_found:
            check_character = user_command[0]
            if (97 <= ord(check_character) <= 122) or (65 <= ord(check_character) <= 90):
                first_character_found = True
            else:
                user_command = user_command[1:]

        first_white_space = user_command.find(" ")
        if first_white_space == -1:
            return user_command, []
        else:
            command = user_command[:first_white_space]
            arguments = user_command[first_white_space+1:]
            arguments = arguments.split()
            arguments = [element.strip() for element in arguments]
            return command.lower(), arguments

    @staticmethod
    def instructions():
        """The menu of the application"""
        print("Add a question in a quiz -> "
              "[Command add: add <id>;<text>;<choice_a>;<choice_b>;<choice_c>;<correct_answer>;<difficulty> ("
              "difficulty can be: easy, medium, hard)]")
        print("Create quiz -> [Command create: create <difficulty <number_of_questions <file>]")
        print("Start a quiz -> [Command start: start <file>] ")
        print("Exit application -> [Command exit: exit]")

    def add_question(self, question_id, text, choice_a, choice_b, choice_c, correct_answer, difficulty):
        """Adds a question to the quiz"""
        try:
            self.__controller.add_question(question_id, text, choice_a, choice_b, choice_c, correct_answer, difficulty)
        except RepositoryError as repository_error:
            print(repository_error)

    def create_quiz(self, difficulty, number_of_questions, file_name):
        """Creates a new quiz"""
        try:
            number_of_questions = int(number_of_questions)
            self.__controller.create_quiz(difficulty, number_of_questions, file_name)
        except ValueError as value_error:
            print(value_error)
        except RepositoryError as repository_error:
            print(repository_error)

    def start_quiz(self, file_name):
        """Starts a quiz"""
        try:
            self.__controller.start_quiz(file_name)
        except RepositoryError as repository_error:
            print(repository_error)

    def play(self):
        """Starts the game"""
        quiz = self.__controller.get_quiz()
        user_total_points = 0
        for question in quiz:
            text, choice_a, choice_b, choice_c, correct_answer, difficulty=self.__controller.get_question_data(question)
            print(text, "|", choice_a, choice_b, choice_c)
            user_answer = input("Type your answer")
            if user_answer == str(correct_answer):
                if difficulty.lower() == 'easy':
                    user_total_points += 1
                elif difficulty.lower() == 'medium':
                    user_total_points += 2
                else:
                    user_total_points += 3
        print("Your total points are:", user_total_points, sep='\t')

    def start_game(self):
        """Gets user commands"""
        Ui.instructions()
        while True:
            command, arguments = self.read_command()
            if command == ADD_A_QUESTION:
                question = arguments[0]
                parts = question.split(";")
                if len(parts) == 7:
                    self.add_question(*parts)
                else:
                    print("Oops! Incorrect arguments of the question!",
                          "add <id>;<text>;<choice_a>;<choice_b>;<choice_c>;<correct_answer>;<difficulty>", sep='\t')
            elif command == CREATE_NEW_QUIZ:
                if len(arguments) == 3:
                    self.create_quiz(*arguments)
                else:
                    print("Oops! Incorrect arguments for the command create",
                          "create <difficulty <number_of_questions <file>", sep='\t')
            elif command == START_A_QUIZ:
                if len(arguments) == 1:
                    self.start_quiz(*arguments)
                    self.play()
                else:
                    print("Oops! Incorrect arguments for the command start",
                          "start <file>", sep='\t')
            elif command == EXIT_GAME:
                break
            else:
                print("Oops! This command is not yet implemented", command)
