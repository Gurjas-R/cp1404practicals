"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    it occurs when a value that is not an integer is entered.

2. When will a ZeroDivisionError occur?
    if 0 is used as an input for the numerator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    by including a while loop for if 0 is inputted as a numerator to ask the user to put a new number
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Denominator cannot be zero. Please enter a non-zero denominator.")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")