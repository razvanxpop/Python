class Assignment:

    def __init__(self, assignment_id, student_name, solution):
        self.__assignment_id = assignment_id
        self.__student_name = student_name
        self.__solution = solution

    def get_assignment_id(self):
        """Returns the assignment id"""
        return self.__assignment_id

    def get_student_name(self):
        """Returns the student name"""
        return self.__student_name

    def get_assignment_solution(self):
        """Returns the assignment solution"""
        return self.__solution

    def __str__(self):
        """Returns the assignment"""
        return f'{self.__assignment_id},{self.__student_name},{self.__solution}'