"""
CP1404 Practical

Class Guitar
"""
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read and Display Guitars Sorted from < to >"""
    guitars = []
    read_file(FILENAME, guitars)
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    add_new_guitars(guitars)
    save_file(FILENAME, guitars)


def read_file(filename, guitars):
    """Read data from a CSV file."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)


def add_new_guitars(guitars):
    """Ask the user to input new guitars."""
    name = input("Guitar name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print(f"{new_guitar} added.")


def save_file(filename, guitars):
    """Save the guitars list to the file."""
    with open(filename, "w", encoding="utf-8-sig") as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    print("Guitars saved to file.")


main()
