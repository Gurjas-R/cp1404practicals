"""
CP1404 Prac

Band class
"""


class Band:
    """Represent a Band """

    def __init__(self, name):
        """Initialise Band instance """
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of Band """
        return str(vars(self))

    def add(self, musician):
        """Add a musician to the musicians list """
        self.musicians.append(musician)

    def play(self):
        """Return string representation of song musician is playing """
        return "\n".join([musician.play() for musician in self.musicians])
