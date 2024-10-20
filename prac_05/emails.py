"""
Emails Program
Estimate Time: 25 minutes
Actual: 30
This program stores users' emails and names in a dictionary.
It extracts a name from the email, asks for confirmation, and allows changes.
"""


def main():
    """Main function to collect emails and names."""
    emails_to_names = {}
    email = input("Email: ")

    while email != "":
        name = get_name_from_email(email)
        is_correct_name = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if is_correct_name not in ("y", ""):
            name = input("Name: ")
        emails_to_names[email] = name
        email = input("Email: ")

    for email, name in emails_to_names.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract name from email."""
    name_part = email.split('@')[0]  # Get the part before '@'
    name_parts = name_part.split('.')  # Split by '.' if there is one
    name = ' '.join(name_parts).title()  # Join and capitalize words
    return name


main()
