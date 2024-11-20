"""
CP1404 Practical

Class Guitar
"""

CURRENT_YEAR = 2024
VINTAGE_AGE_THRESHOLD = 50


class Guitar:
    """Represents the details of a Guitar"""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return Guitar instance str"""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """Return if the guitar object is < than other guitar"""
        return self.year < other.year

    def get_age(self):
        """Get age of a guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if Guitar is vintage"""
        return self.get_age() >= VINTAGE_AGE_THRESHOLD
