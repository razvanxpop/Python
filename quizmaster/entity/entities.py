class Question:

    def __init__(self, question_id, text, choice_a, choice_b, choice_c, correct_answer, difficulty):
        self.__question_id = question_id
        self.__text = text
        self.__choice_a = choice_a
        self.__choice_b = choice_b
        self.__choice_c = choice_c
        self.__correct_answer = correct_answer
        self.__difficulty = difficulty

    def get_difficulty(self):
        """Returns the difficulty of the question"""
        return self.__difficulty

    def get_text(self):
        """Returns the text of the question"""
        return self.__text

    def get_choice_a(self):
        """Returns choice A of the question"""
        return self.__choice_a

    def get_choice_b(self):
        """Returns choice B of the question"""
        return self.__choice_b

    def get_choice_c(self):
        """Returns choice C of the question"""
        return self.__choice_c

    def get_correct_answer(self):
        """Returns the correct answer"""
        return self.__correct_answer

    def __str__(self):
        return f'{self.__question_id};{self.__text};{self.__choice_a};{self.__choice_b};{self.__choice_c}' \
               f';{self.__correct_answer};{self.__difficulty}'
