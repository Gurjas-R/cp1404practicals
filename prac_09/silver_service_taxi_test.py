"""
CP1404 Practical

Silver Service Taxi class inherited from Taxi Class
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def simulate_test():
    """Test Silver Service Taxi """
    my_taxi = SilverServiceTaxi("Luxury Taxi", 100, 2)
    my_taxi.drive(18)
    print(my_taxi)
    assert my_taxi.get_fare() == 48.78
    print(my_taxi.get_fare())


simulate_test()
