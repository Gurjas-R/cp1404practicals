"""
CP1404 Practical
Programming Language class
"""


class ProgrammingLanguage:
    """Showcase Programming Language."""

    def __init__(self, name, typing, reflection, year):
        """Create Programming Language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return Programming Language instance str"""
        return f"{self.name}: Typing - {self.typing}, Reflection - {self.reflection}, Released - {self.typing}"

    def is_dynamic(self):
        """Determine if a Programming Language is dynamic"""
        return self.typing == "Dynamic"
