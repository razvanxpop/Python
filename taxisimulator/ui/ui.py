from controller.controller import ControllerError


GENERATE_NUMBER_OF_OPERATIONAL_TAXIS = 1
ADD_RIDE = 2
SIMULATE_RIDE = 3
EXIT = 0


class Ui:

    def __init__(self, controller):
        self.__controller = controller

    @staticmethod
    def menu():
        """The main menu of the application"""
        print("[1] Generate number of operational taxis (between 0 and 10).")
        print("[2] Add a ride.")
        print("[3] Simulate a ride.")
        print("[0] Exit.")

    def generate_taxis(self, number):
        try:
            number = int(number)
            self.__controller.generate_taxis(number)
        except ValueError as value_error:
            print(value_error)

    def add_ride(self, start_position_x, start_position_y, end_position_x, end_position_y):
        try:
            start_position_x = int(start_position_x)
            start_position_y = int(start_position_y)
            end_position_x = int(end_position_x)
            end_position_y = int(end_position_y)
            self.__controller.add_ride(start_position_x, start_position_y, end_position_x, end_position_y)
        except ValueError as value_error:
            print(value_error)
        except ControllerError as controller_error:
            print(controller_error)

    def simulate_ride(self):
        """Simulates a valid ride"""
        try:
            self.__controller.simulate_ride()
        except ControllerError as controller_error:
            print(controller_error)

    def display_taxis_decreasing_order_by_fare(self):
        print(*self.__controller.get_decreasing_order_taxis(), sep='\n')

    def run_console(self):
        while True:
            self.menu()
            valid_option = False
            option = 0
            while not valid_option:
                try:
                    option = int(input("Type your option:"))
                    valid_option = True
                except ValueError as value_error:
                    print(value_error)
            if option == GENERATE_NUMBER_OF_OPERATIONAL_TAXIS:
                number = input("Type the number of taxis:")
                self.generate_taxis(number)
            elif option == ADD_RIDE:
                start_position_x = input("Type start position x:")
                start_position_y = input("Type start position y:")
                end_position_x = input("Type end position x:")
                end_position_y = input("Type end position y:")
                self.add_ride(start_position_x, start_position_y, end_position_x, end_position_y)
                self.display_taxis_decreasing_order_by_fare()
            elif option == SIMULATE_RIDE:
                self.simulate_ride()
                self.display_taxis_decreasing_order_by_fare()
            elif option == EXIT:
                break


