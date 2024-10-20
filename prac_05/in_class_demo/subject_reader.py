"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    # print(data)
    # display_subject_details(data)
    subject_to_data = convert_data(data)
    print(subject_to_data)
    subject = input("Subject code: ")
    print(f"{subject_to_data[subject][0]} teaches {subject}")


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    # empty list to store subject details
    data = []

    input_file = open(FILENAME)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    input_file.close()
    # returned nested list of subjects
    return data


def convert_data(data):
    subject_to_data = {}
    for subject_data in data:
        subject_to_data[subject_data[0]] = subject_data[1:]
    return subject_to_data


# def display_subject_details(data):
#     """Display the subject details in a formatted way."""
#     for subject_data in data:
#         print(f"{} is taught by {:12} and has {:3} students on {}".format(*subject_data))


main()
