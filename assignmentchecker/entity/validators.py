class ValidatorError(Exception):
    pass


class ValidateAssignment:

    @staticmethod
    def validate(assignment):

        errors = ""
        if len(assignment.get_student_name()) < 3:
            errors += "Invalid student name!\n"
        if assignment.get_assignment_solution() == "":
            errors += "Invalid assignment solution!\n"

        if len(errors) > 0:
            raise ValidatorError(errors)
