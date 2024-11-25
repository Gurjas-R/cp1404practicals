"""
CP1404/CP5632 Practical
Program to simulate using taxis and calculate trip costs
"""

from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Run the taxi simulator, allowing users to choose and drive taxis while tracking costs."""
    available_taxis = [Taxi('Prius', 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_cost = 0
    chosen_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            for i, taxi in enumerate(available_taxis):
                print(f'{i} - {taxi}')
            taxi_choice = int(input("Choose taxi: "))
            try:
                chosen_taxi = available_taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "d":
            if chosen_taxi:
                chosen_taxi.start_fare()
                distance = float(input("Drive how far? "))
                chosen_taxi.drive(distance)
                trip_fare = chosen_taxi.get_fare()
                print(f"Your {chosen_taxi.name} trip cost you ${trip_fare:.2f}")
                total_cost += trip_fare
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_cost:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_cost:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(available_taxis):
        print(f'{i} - {taxi}')


main()
