import random

from entity.entities import Question
from repository.repository import Repository


class ControllerError(Exception):
    pass


class Controller:

    def __init__(self, repository):
        self.__repository = repository

    def add_question(self, question_id, text, choice_a, choice_b, choice_c, correct_answer, difficulty):
        """Adds a question to the quiz"""
        question = Question(question_id, text, choice_a, choice_b, choice_c, correct_answer, difficulty)
        self.__repository.add_question(question)

    def create_quiz(self, difficulty, number_of_questions, file_name):
        """Creates a new quiz"""
        self.__repository.create_quiz(difficulty, number_of_questions, file_name)

    def start_quiz(self, file_name):
        """Starts a quiz"""
        self.__repository.start_quiz(file_name)

    def generate_questions(self):
        """Generates 100 random questions to the master quiz"""
        easy_question_largest = "Which number is the largest"
        easy_question_smallest = "Which number is the smallest"
        easy_question_prime = "Which number is prime"
        medium_question_satellite = "Name the first satellite"
        medium_question_country = "Which is the largest country"
        medium_question_fish = "Which is not a fish"
        hard_question_horse = "Name El Cid's horse"
        hard_question_empire = "The Western Roman Empire fell in"
        hard_question_apollo = "Which Apollo mission did not make it to the moon"
        for question_id in range(1, 101):
            if question_id <= 33:
                question = random.choice([easy_question_largest, easy_question_smallest, easy_question_prime])
                if question == easy_question_largest:
                    choice_a = random.randint(1, 57)
                    choice_b = random.randint(58, 98)
                    choice_c = random.randint(10, 43)
                    correct_answer = choice_b
                    difficulty = 'easy'
                    question = Question(question_id, easy_question_largest, choice_a, choice_b, choice_c,
                                        correct_answer, difficulty)
                    self.__repository.add_question(question)
                elif question == easy_question_smallest:
                    choice_a = random.randint(10, 23)
                    choice_b = random.randint(31, 98)
                    choice_c = random.randint(25, 43)
                    correct_answer = choice_a
                    difficulty = 'easy'
                    question = Question(question_id, easy_question_smallest, choice_a, choice_b, choice_c,
                                        correct_answer, difficulty)
                    self.__repository.add_question(question)
                else:
                    choice_a = random.choice([2, 3, 5, 11, 17, 107, 131])
                    choice_b = random.choice([number for number in range(4, 100, 2)])
                    choice_c = random.choice([number for number in range(4, 100, 2)])
                    correct_answer = choice_a
                    difficulty = 'easy'
                    question = Question(question_id, easy_question_prime, choice_a, choice_b, choice_c,
                                        correct_answer, difficulty)
                    self.__repository.add_question(question)
            elif question_id <= 66:
                question = random.choice([medium_question_fish, medium_question_country, medium_question_satellite])
                if question == medium_question_country:
                    choice_a = random.choice(['India', 'Argentina', 'Canada', 'Belgium', 'France', 'Portugal'])
                    choice_b = random.choice(['England', 'China', 'South Korea', 'Germany', 'Spain', 'Romania'])
                    choice_c = 'Russia'
                    correct_answer = choice_c
                    difficulty = 'medium'
                    question = Question(question_id, medium_question_country, choice_a, choice_b, choice_c,
                                        correct_answer, difficulty)
                    self.__repository.add_question(question)
                elif question == medium_question_satellite:
                    choice_a = 'Apollo'
                    choice_b = 'Sputnik'
                    choice_c = 'Zaria'
                    correct_answer = choice_b
                    difficulty = 'medium'
                    question = Question(question_id, medium_question_satellite, choice_a, choice_b, choice_c,
                                        correct_answer, difficulty)
                    self.__repository.add_question(question)
                else:
                    choice_a = random.choice(['Crap', 'Eel'])
                    choice_b = random.choice(['Leopard', 'Orca', 'Shark'])
                    choice_c = random.choice(['Lion', 'Dog', 'Fog'])
                    correct_answer = choice_a
                    difficulty = 'medium'
                    question = Question(question_id, medium_question_fish, choice_a, choice_b, choice_c,
                                        correct_answer, difficulty)
                    self.__repository.add_question(question)
            else:
                question = random.choice([hard_question_apollo, hard_question_empire, hard_question_horse])
                if question == hard_question_empire:
                    choice_a = 476
                    choice_b = random.randint(200, 350)
                    choice_c = random.randint(500, 800)
                    correct_answer = choice_a
                    difficulty = 'hard'
                    question = Question(question_id, hard_question_empire, choice_a, choice_b, choice_c,
                                        correct_answer, difficulty)
                    self.__repository.add_question(question)
                elif question == hard_question_apollo:
                    choice_a = 11
                    choice_b = 13
                    choice_c = 17
                    correct_answer = 13
                    difficulty = 'hard'
                    question = Question(question_id, hard_question_apollo, choice_a, choice_b, choice_c,
                                        correct_answer, difficulty)
                    self.__repository.add_question(question)
                else:
                    choice_a = 'Alex'
                    choice_b = 'Berny'
                    choice_c = 'Babieca'
                    correct_answer = choice_c
                    difficulty = 'hard'
                    question = Question(question_id, hard_question_horse, choice_a, choice_b, choice_c,
                                        correct_answer, difficulty)
                    self.__repository.add_question(question)

    def get_size(self):
        """Returns the number of questions in the quiz"""
        return self.__repository.get_size()

    def get_quiz(self):
        """Returns the questions form the quiz in a list"""
        return self.__repository.get_quiz()

    @staticmethod
    def get_question_data(question):
        """Returns the data of the question"""
        return question.get_text(), question.get_choice_a(), question.get_choice_b(), question.get_choice_c(), \
            question.get_correct_answer(), question.get_difficulty()


repository_file = Repository("quiz.txt")
controller = Controller(repository_file)
controller.generate_questions()
