"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    print(graded_score(score))

    score = generate_random_score(score)
    print(score)
    print(graded_score(score))


def graded_score(score):
    """Determine grade for score  """
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def generate_random_score(score):
    """"Generate a random integer for score"""
    score = random.randint(0, 100)
    return score


main()
