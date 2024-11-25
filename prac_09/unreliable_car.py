"""
CP1404 Practical

Unreliable Car class inherited from car class
"""

from random import randint

from prac_09.car import Car


class UnreliableCar(Car):
    """Simulate an unreliable vehicle object"""

    def __init__(self, name, fuel, reliability):
        """ Initialise an Unreliable Car instance. """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Drive unreliable car based on reliability attribute
        """
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
