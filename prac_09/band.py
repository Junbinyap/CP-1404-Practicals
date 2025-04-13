class Band:
    """Band class to manage a collection of Musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a Musician to the Band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return string representation of the Band and its Musicians."""
        musician_strings = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_strings})"

    def play(self):
        """Return string of each Musician playing or needing an instrument."""
        return "\n".join(musician.play() for musician in self.musicians)