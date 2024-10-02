def main():
    password_minimum_limit = 10
    password = get_password(password_minimum_limit)
    get_asterisks(password)


def get_password(password_minimum_limit):
    password = input("Enter your password: ")
    while len(password) < password_minimum_limit:
        print("Your password does not meet the minimum length required.")
        password = input("Enter your password: ")
    return password


def get_asterisks(password):
    asterisks = '*' * len(password)
    print(f"{asterisks}")


main()
