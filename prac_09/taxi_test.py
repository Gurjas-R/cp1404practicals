"""
CP1404 Practical
Taxi Class
"""

from prac_09.taxi import Taxi


def simulate_tests():
    """Test Taxi class."""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


simulate_tests()
