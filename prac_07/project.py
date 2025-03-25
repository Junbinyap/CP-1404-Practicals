class Project:
    """Represent a project with attributes: name, start_date, priority, cost_estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return a string representation of a project."""
        return (f"{self.name}, Start: {self.start_date}, Priority: {self.priority}, "
                f"Cost: ${self.cost_estimate:.2f}, Completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare projects by priority (lower number = higher priority)."""
        return self.priority < other.priority
