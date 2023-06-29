from entity.entities import Assignment


class RepositoryError(Exception):
    pass


class Repository:

    def __init__(self, path_to_file):
        self._assignments = []
        self.__path_to_file = path_to_file

    def read_all_form_file(self):
        """Reads all assignments for the file"""
        with open(self.__path_to_file, "r") as file:
            self._assignments.clear()
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    try:
                        parts = line.split(",")
                        assignment_id = parts[0]
                        student_name = parts[1]
                        solution = parts[2]
                        assignment = Assignment(assignment_id, student_name, solution)
                        self._assignments.append(assignment)
                    except IndexError as index_error:
                        pass

    def write_all_to_file(self):
        """Writes all assignments form the list to the file"""
        with open(self.__path_to_file, "w") as file:
            for assignment in self._assignments:
                file.write(str(assignment) + '\n')

    def add_assignment(self, assignment):
        """Adds an assignment"""
        self.read_all_form_file()
        valid_assignment = True
        for check_assignment_id in self._assignments:
            if check_assignment_id.get_assignment_id() == assignment.get_assignment_id():
                valid_assignment = False
                raise RepositoryError("Oops! Duplicate assignment id!")

        if valid_assignment:
            self._assignments.append(assignment)
        self.write_all_to_file()

    def get_all_assignments(self):
        """Returns all assignments"""
        self.read_all_form_file()
        return [assignment for assignment in self._assignments]

    def get_size(self):
        """Returns the number of assignments"""
        return len(self._assignments)
