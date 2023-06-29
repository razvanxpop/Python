class RepositoryError(Exception):
    pass


class Repository:

    def __init__(self):
        self._taxis = []

    def add_taxi(self, taxi):
        """Adds a taxi"""
        valid_taxi = True
        for check_taxi in self._taxis:
            if check_taxi.get_taxi_id() == taxi.get_taxi_id():
                valid_taxi = False
                raise RepositoryError("Oops! Duplicate taxi id!")
        if valid_taxi:
            self._taxis.append(taxi)

    def get_all_taxis(self):
        """Returns all taxis"""
        return [taxi for taxi in self._taxis]

    def get_size(self):
        """Returns the number of taxis"""
        return len(self._taxis)
