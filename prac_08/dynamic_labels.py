from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """Kivy app that dynamically creates labels from a list of names."""

    def __init__(self, **kwargs):
        """Initialize the app with a list of names."""
        super().__init__ (**kwargs)
        self.names = ["Alvin", "JunBin", "Mayur", "Marcus", "Kieran"]

    def build(self):
        """Load the Kivy file and return the root widget."""
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def on_start(self):
        """Dynamically create labels for each name in the list."""
        main_layout = self.root.ids.main
        for name in self.names:
            main_layout.add_widget(Label(text=name))

DynamicLabelsApp().run()