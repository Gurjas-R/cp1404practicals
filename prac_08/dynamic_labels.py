"""
CP1404
Kivy program dynamic labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):
    """Kivy program dynamic labels."""

    def __init__(self, **kwargs):
        super(DynamicLabels, self).__init__(**kwargs)
        self.names = ["Nick", "Gurjas", "Dylan", "Nickdem", "Dean"]

    def build(self):
        """
        Build the app layout and dynamically create Labels for each name.
        """
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_dynamic_labels()
        return self.root

    def create_dynamic_labels(self):
        """Create labels from data and add them to the Kivy UI"""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabels().run()
