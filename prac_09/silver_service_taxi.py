"""
CP1404 Practical

Silver Service Taxi class inherited from Taxi Class
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a Silver Service Taxi object"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise Silver Service Taxi instance"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return string representation of Silver Service Taxi """
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get current fare """
        return self.flagfall + super().get_fare()
