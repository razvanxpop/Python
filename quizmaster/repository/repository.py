from entity.entities import Question


class RepositoryError(Exception):
    pass


class Repository:

    def __init__(self, path_to_file):
        self._quiz = []
        self.__path_to_file = path_to_file
        self._files = [path_to_file]

    def read_all_from_file(self):
        """Reads from file"""
        with open(self.__path_to_file, "r") as file:
            lines = file.readlines()
            self._quiz.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    elements = line.split(";")
                    if len(elements) == 7:
                        question_id = elements[0]
                        sentence = elements[1]
                        choice_a = elements[2]
                        choice_b = elements[3]
                        choice_c = elements[4]
                        correct_answer = elements[5]
                        difficulty = elements[6]
                        question = Question(question_id, sentence, choice_a, choice_b, choice_c,
                                            correct_answer, difficulty)
                        self._quiz.append(question)

    def write_all_to_file(self):
        """Write in file"""
        with open(self.__path_to_file, "w") as file:
            for question in self._quiz:
                file.write(str(question) + '\n')

    def add_question(self, question):
        """Adds a question to the quiz"""
        self.read_all_from_file()
        elements = str(question).split(";")
        if len(elements) != 7:
            raise RepositoryError("Oops! The question is not formulated correctly!")
        elif elements[-1].lower() not in ['easy', 'medium', 'hard']:
            raise RepositoryError("Oops! The difficulty of the question is not valid!")
        else:
            self._quiz.append(question)
        self.write_all_to_file()

    def create_quiz(self, difficulty, number_of_questions, file_name):
        """Creates quiz"""
        self.read_all_from_file()
        self._files.append(file_name)
        if not difficulty.lower() in ['easy', 'medium', 'hard']:
            raise RepositoryError("The difficulty of the questions is invalid!")
        else:
            if difficulty.lower() == 'easy':
                create_quiz = []
                number_of_easy_questions = 0
                for question in self._quiz:
                    if 'easy' == question.get_difficulty() and number_of_questions > number_of_easy_questions:
                        number_of_easy_questions += 1
                        create_quiz.append(question)
                if number_of_easy_questions == number_of_questions:
                    with open(file_name, "w") as file:
                        for question in create_quiz:
                            file.write(str(question) + "\n")
                else:
                    raise RepositoryError("Oops! Not enough easy questions!")
            elif difficulty.lower() == 'medium':
                create_quiz = []
                number_of_medium_questions = 0
                for question in self._quiz:
                    if 'medium' == question.get_difficulty() and number_of_questions > number_of_medium_questions:
                        number_of_medium_questions += 1
                        create_quiz.append(question)
                if number_of_medium_questions == number_of_questions:
                    with open(file_name, "w") as file:
                        for question in create_quiz:
                            file.write(str(question) + "\n")
                else:
                    raise RepositoryError("Oops! Not enough medium questions!")
            else:
                create_quiz = []
                number_of_hard_questions = 0
                for question in self._quiz:
                    if 'hard' == question.get_difficulty() and number_of_questions > number_of_hard_questions:
                        number_of_hard_questions += 1
                        create_quiz.append(question)
                if number_of_hard_questions == number_of_questions:
                    with open(file_name, "w") as file:
                        for question in create_quiz:
                            file.write(str(question) + "\n")
                else:
                    raise RepositoryError("Oops! Not enough hard questions")

    def start_quiz(self, file_name):
        """Starts a quiz"""
        if file_name not in self._files:
            raise RepositoryError("Oops! The file does not exit!")
        else:
            self.__path_to_file = file_name

    def get_size(self):
        """Returns the number of questions in the quiz"""
        self.read_all_from_file()
        return len(self._quiz)

    def get_quiz(self):
        """Returns the questions in the quiz"""
        self.read_all_from_file()
        return [question for question in self._quiz]
