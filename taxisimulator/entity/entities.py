class Taxi:

    def __init__(self, taxi_id, position_x, position_y, fare):
        self.__taxi_id = taxi_id
        self.__position_x = position_x
        self.__position_y = position_y
        self.__fare = fare

    def get_taxi_id(self):
        """Returns the id of the taxi"""
        return self.__taxi_id

    def get_position_x(self):
        """Returns the taxi position x"""
        return self.__position_x

    def get_position_y(self):
        """Returns the taxi position y"""
        return self.__position_y

    def get_fare(self):
        """Returns the taxi fare"""
        return self.__fare

    def set_position_x(self, new_position_x):
        """Sets the position x of the taxi"""
        self.__position_x = new_position_x

    def set_position_y(self, new_position_y):
        """Sets position y of the taxi"""
        self.__position_y = new_position_y

    def set_fare(self, new_fare):
        """Sets the taxi fare"""
        self.__fare += new_fare

    def __str__(self):
        """Return a taxi datas as a string"""
        return f'{self.__taxi_id} ({self.__position_x},{self.__position_y}) {self.__fare}'

    def __eq__(self, other):
        return self.__taxi_id == other.__taxi_id and self.__position_x == other.__position_x \
            and self.__position_y == other.__position_y and self.__fare == other.__fare
