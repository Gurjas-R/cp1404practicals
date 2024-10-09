"""Module 3 Lecture Video Example Codes and Activity below.
z"""

# FILENAME = "secret.txt"
#
#
# def main():
#     secret = load_number(FILENAME)
#     guess = get_valid_number()
#     while guess != secret:
#         print("Guess again")
#         guess = get_valid_number()
#     print("You got it!")
#
#
# def get_valid_number():
#     is_valid_input = False
#     while not is_valid_input:
#         try:
#             guess = int(input("? "))
#             is_valid_input = True
#         except ValueError:
#             print("Invalid integer")
#     return guess
#
#
# def load_number(filename):
#     """Load integer from file filename."""
#     try:
#         infile = open(filename, "r")
#         number = int(infile.read())
#     except ValueError:
#         print(f"Invalid contents in {filename}")
#         number = 6
#     except FileNotFoundError:
#         print(f"{filename} not found")
#         number = 4
#     else:
#         infile.close()
#     return number
#
#
# main()

"""is_valid_input = False
while not is_valid_input:
    try:
        age = int(input("Age: "))
        if age < 0:
            print("Age must be >= 0")
        else:
            is_valid_input = True
    except ValueError:
        print("Invalid (not an integer)")
print("Next year you will be", age + 1)"""

# print lines with a certain element required.
#
# def print_header_lines(filename):
#     try:
#            in_file = open(filename, r)
#            file = str(infile.read)
#         (with open(filename, 'r') as file:)
#             for line in file:
#                 # Check if the line starts with '#'
#                 if line.startswith('#'):
#                     print(line, end='')  # Print the line without adding extra newlines
#     except FileNotFoundError:
#         print(f"The file '{filename}' was not found.")
#
# filename = 'example.txt'
# print_header_lines(filename)
#

"""CSV Example Below"""
with open("data.txt", "r") as in_file:
    # in_file.readline() #Used to ignore header.
    for line in in_file:
        # print(line)
        parts = line.lstrip().split(',')
        # print(parts)
        product_name = parts[0]
        product_year = parts[1]
        product_price = float(parts[2])
        print(f"Product Name: {product_name}")
        print(f"Year: {product_year}")
        print(f"Price: ${product_price:.2f}")
        print(" ")
