"""
CP1404 Practical

Unreliable Car class inherited from car class
"""

from prac_09.unreliable_car import UnreliableCar


def simulate_tests():
    """Test Unreliable Car class."""
    great_car = UnreliableCar("Great", 100, 80)
    horrible_car = UnreliableCar("Horrible", 100, 15)
    for i in range(1, 15):
        print(f"Trying to drive {i}km:")
        print(f"{great_car.name} drove {great_car.drive(i)}km")
        print(f"{horrible_car.name} drove {horrible_car.drive(i)}km")
    print(great_car)
    print(horrible_car)


simulate_tests()
