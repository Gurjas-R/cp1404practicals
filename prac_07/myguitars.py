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


def read_file(filename, guitars):
    """Read data from a CSV file."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)


main()