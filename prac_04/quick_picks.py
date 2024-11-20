import random

# Constants
NUMBERS_PER_PICK = 6  # Each quick pick contains 6 numbers
MIN_NUMBER = 1  # Minimum value for numbers
MAX_NUMBER = 45  # Maximum value for numbers


def main():
    """Generate and display the requested number of quick picks."""
    quick_picks_count = int(input("How many quick picks? "))

    for _ in range(quick_picks_count):
        quick_pick = generate_quick_pick()
        print(format_quick_pick(quick_pick))


def generate_quick_pick():
    """Generate a single quick pick with unique numbers in sorted order."""
    numbers = []  # List to store the numbers for this quick pick

    # Keeps adding random numbers the required count
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:  # confirms no repeated numbers
            numbers.append(number)

    return sorted(numbers)


def format_quick_pick(quick_pick):
    """Format a quick pick line with numbers neatly aligned."""
    return " ".join(f"{number:2}" for number in quick_pick)


main()
