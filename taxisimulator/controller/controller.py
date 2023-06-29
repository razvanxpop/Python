from entity.entities import Taxi


import random


class ControllerError(Exception):
    pass


class Controller:

    def __init__(self, repository):
        self.__repository = repository

    def add_taxi(self, taxi_id, position_x, position_y):
        """Adds a taxi"""
        taxi = Taxi(taxi_id, position_x, position_y, 0)
        self.__repository.add_taxi(taxi)

    def generate_taxis(self, number):
        """Generates taxis"""
        all_taxis = self.__repository.get_all_taxis()
        for _ in range(number):
            valid_taxi_id = False
            taxi_id = 0
            while not valid_taxi_id:
                valid_taxi_id = True
                taxi_id = random.randint(1, 100)
                for taxi in all_taxis:
                    if taxi.get_taxi_id() == taxi_id:
                        valid_taxi_id = False
            valid_taxi_positions = False
            position_x = 0
            position_y = 0
            while not valid_taxi_positions:
                valid_taxi_positions = True
                position_x = random.randint(0, 100)
                position_y = random.randint(0, 100)
                for taxi in all_taxis:
                    if abs(taxi.get_taxi_position_x()-position_x) + abs(taxi.get_taxi_position_y()-position_y) <= 5:
                        valid_taxi_positions = False
            self.add_taxi(taxi_id, position_x, position_y)

    def get_near_taxi(self, position_x, position_y):
        size = self.__repository.get_size()
        if size == 0:
            raise ControllerError("Oops! No taxis available!")
        else:
            all_taxis = self.__repository.get_all_taxis()
            minimum_distance = abs(all_taxis[0].get_position_x() - position_x) + abs(all_taxis[0].get_position_y() - position_y)
            taxi_id = all_taxis[0].get_taxi_id()
            for taxi_index in range(1, size):
                distance = abs(all_taxis[taxi_index].get_position_x() - position_x) + abs(all_taxis[taxi_index].get_position_y() - position_y)
                if distance < minimum_distance:
                    minimum_distance = distance
                    taxi_id = all_taxis[taxi_index].get_taxi_id()
            return taxi_id

    def add_ride(self, start_position_x, start_position_y, end_position_x, end_position_y):
        """Adds a ride"""
        all_taxis = self.__repository.get_all_taxis()
        taxi_id = self.get_near_taxi(start_position_x, start_position_y)
        taxi_fare = abs(end_position_x - start_position_x) + abs(end_position_y - start_position_y)
        for taxi in all_taxis:
            if taxi.get_taxi_id() == taxi_id:
                taxi.set_position_x(end_position_x)
                taxi.set_position_y(end_position_y)
                taxi.set_fare(taxi_fare)

    def simulate_ride(self):
        """Simulates a random ride"""
        if self.__repository.get_size() == 0:
            raise ControllerError("Oops! No taxis available!")
        else:
            distance = 0
            taxi_id = 0
            start_position_x = 0
            start_position_y = 0
            end_position_x = 0
            end_position_y = 0

            while distance < 10:
                start_position_x = random.randint(1, 100)
                start_position_y = random.randint(1, 100)
                end_position_x = random.randint(1, 100)
                end_position_y = random.randint(1, 100)
                distance = abs(end_position_x - start_position_x) + abs(end_position_y - start_position_y)

            taxi_id = self.get_near_taxi(start_position_x, start_position_y)
            fare = distance
            all_taxis = self.__repository.get_all_taxis()
            for taxi in all_taxis:
                if taxi.get_taxi_id() == taxi_id:
                    taxi.set_position_x(end_position_x)
                    taxi.set_position_y(end_position_y)
                    taxi.set_fare(fare)
                    break

    def get_decreasing_order_taxis(self):
        """Returns all the taxis in decreasing order by fare"""
        all_taxis = self.__repository.get_all_taxis()
        all_taxis = sorted(all_taxis, key=lambda x: x.get_fare(), reverse=True)
        return [taxi for taxi in all_taxis]

    def get_all_taxis(self):
        """Returns all taxis"""
        return self.__repository.get_all_taxis()
