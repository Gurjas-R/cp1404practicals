"""
CP1404
program to convert miles to kilometres
"""

MILES_TO_KILOMETRES = 1.60934


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculation output result to label widget """
        value = self.get_validated_miles()
        result = value * MILES_TO_KILOMETRES
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """
        Handle up/Down button press
        """
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """
        Get Text Input From Text Entry
        """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
