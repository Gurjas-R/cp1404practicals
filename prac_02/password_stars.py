password_minimum_limit = int(input("Minimum Length: "))
password_input = input("Enter your password: ")

if len(password_input) < password_minimum_limit:
    print("Your password does not meet the minimum length required")
    password_input = input("Enter your password: ")
else:
    asterisks = '*' * len(password_input)
    print(f"{asterisks}")
