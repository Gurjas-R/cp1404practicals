""""display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>"""

MENU = """(G)et a valid score
(P)rint result 
(S)how stars
(Q)uit
"""


def main():
    score = get_valid_score
    choice = input(f"{MENU}: ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = float(input("Enter score: "))
            get_valid_score(score)
            choice = input(f"{MENU}: ").upper()
        elif choice == 'P':
            print(graded_score(score))
            choice = input(f"{MENU}: ").upper()
        elif choice == 'S':
            show_stars(score)
            choice = input(f"{MENU}: ").upper()
        else:
            print("Invalid Input")
            choice = input(f"{MENU}: ").upper()
    print("farewell")


def get_valid_score(score):
    """"Get a valid score"""
    if score < 0:
        print("Invalid score")
        score = float(input("Enter score: "))
    elif score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))


def graded_score(score):
    """Determine grade for score  """
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Convert to stars"""
    star = '*' * int(score)
    print(f"{star}")


main()
