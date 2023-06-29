from entity.entities import Assignment


class Controller:

    def __init__(self, repository, assignment_validator):
        self.__repository = repository
        self.__assignment_validator = assignment_validator

    def add_assignment(self, assignment_id, student_name, solution):
        """Adds an assignment"""
        assignment = Assignment(assignment_id, student_name, solution)
        self.__assignment_validator.validate(assignment)
        self.__repository.add_assignment(assignment)

    def dishonesty_check(self):
        """Dishonesty checker returns the students which have at least a 20% words similarity in the solution"""
        all_assignments = self.__repository.get_all_assignments()
        number_of_assignments = self.__repository.get_size()

        list_to_return = []
        for first_assignment_index in range(number_of_assignments):
            for second_assignment_index in range(first_assignment_index+1, number_of_assignments):
                first_assignment_solution = all_assignments[first_assignment_index].get_assignment_solution()
                second_assignment_solution = all_assignments[second_assignment_index].get_assignment_solution()
                words_first_solution = first_assignment_solution.split()
                words_second_solution = second_assignment_solution.split()
                length_of_first_solution = len(words_first_solution)
                similarity = 0
                for first_word in words_first_solution:
                    for second_word in words_second_solution:
                        if first_word == second_word:
                            similarity += 1

                similarity_percentage = similarity*100 // length_of_first_solution
                if similarity_percentage >= 20:
                    first_student_name = all_assignments[first_assignment_index].get_student_name()
                    second_student_name = all_assignments[second_assignment_index].get_student_name()
                    element = f"{first_student_name}  {second_student_name} ({similarity_percentage} of " \
                              f"{second_student_name}'s solution)"
                    list_to_return.append(element)
        return [dishonesty for dishonesty in list_to_return]

    def get_all_assignments(self):
        """Returns all assignments"""
        return self.__repository.get_all_assignments()
