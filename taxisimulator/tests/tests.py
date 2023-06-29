import unittest

from controller.controller import Controller, ControllerError
from entity.entities import Taxi
from repository.repository import Repository


class Tests(unittest.TestCase):

    def run_all_tests(self):
        self.setup()
        self.test_add_ride()

    def setup(self) -> None:
        self.__repository = Repository()
        self.__controller = Controller(self.__repository)

    def test_add_ride(self):
        try:
            self.__controller.add_ride(12, 15, 30, 40)
        except ControllerError as controller_error:
            self.assertEqual(str(controller_error), "Oops! No taxis available!")
        self.__controller.add_taxi(2, 0, 0)
        self.__controller.add_ride(12, 15, 30, 40)
        taxi = Taxi(2, 30, 40, 43)
        self.assertEqual(*self.__controller.get_all_taxis(), taxi)
