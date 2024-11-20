def main():
    """Get 5 inputs from users and store them in a list and display certain values, and ask for user name and
    authorisation"""

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    user_input = input("Enter your username: ")
    if user_input in usernames:
        print("Access granted")
    else:
        print("Access denied")

    numbers = []  # Initialize an empty list to store the numbers

    # Collect 5 numbers from the user
    for i in range(5):
        number = float(input(f"Number {i + 1}: "))  # Use float to handle decimals
        numbers.append(number)  # Add the number to the list

    # Display the summary information
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")


main()
