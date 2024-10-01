user_name = input("Enter name: ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = input(">>> ").upper()  # Ensure the choice is uppercase

while choice != 'Q':
    if choice == 'H':
        print(f"Hello {user_name}")
    elif choice == 'G':
        print(f"Goodbye {user_name}")
    else:
        print("Invalid choice")

    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>> ").upper()

print("Finished.")
