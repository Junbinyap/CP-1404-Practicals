
from project import Project

MENU = ("- (L)oad projects""\n- (S)ave projects""\n- (D)isplay projects""\n- (F)ilter projects by date""\n- (A)dd new project""\n- (U)pdate project""\n- (Q)uit")

def main():
    """Main menu loop for project management."""
    filename = "projects.txt"
    projects = load_projects(filename)
    choice = ""

    while choice != "Q":
        print(MENU)
        choice = input("Choose an option: ").strip().upper()

        if choice == "L":
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)

def load_projects(filename):
    """Load projects from a given file."""
    projects = []
    try:
        with open(filename, "r") as file:
            next(file)  # Skip header
            for line in file:
                parts = line.strip().split("\t")
                if len(parts) == 5:
                    projects.append(Project(*parts))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return projects


def save_projects(filename, projects):
    """Save projects to a given file."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")
    print(f"Projects saved to {filename}.")




if __name__ == "__main__":
    main()
