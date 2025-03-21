import datetime
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
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        elif choice == "Q":
             save_choice = input(f"Would you like to save to {filename}? (Y/N): ").strip().upper()
             if save_choice == "Y":
                 save_projects(filename, projects)
             print("Thank you for using custom-built project management software.")
    else:
        print("Invalid choice. Try again.")

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

def display_projects(projects):
    """Display completed and incomplete projects, sorted by priority."""
    incomplete = sorted([p for p in projects if p.completion_percentage < 100])
    completed = sorted([p for p in projects if p.completion_percentage == 100])

    print("\nIncomplete projects:")
    for project in incomplete:
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in completed:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter and display projects starting after a given date."""
    date_str = input("Show projects that start after date (dd/mm/yy): ")
    try:
        filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        filtered_projects = sorted(
            [p for p in projects if datetime.datetime.strptime(p.start_date, "%d/%m/%Y").date() > filter_date],
            key=lambda p: datetime.datetime.strptime(p.start_date, "%d/%m/%Y").date()
        )

        if filtered_projects:
            print("\nProjects starting after", date_str)
            for project in filtered_projects:
                print(f"  {project}")
        else:
            print("No projects found starting after", date_str)
    except ValueError:
        print("Invalid date format. Please enter the date as DD-MM-YYYY.")

def add_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate:$ ")
    completion_percentage = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate,completion_percentage ))

def update_project(projects):
    """Update a project's completion percentage or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    index = int(input("Project choice: "))
    project = projects[index]

    new_completion = input(f"New Percentage: ")
    new_priority = input(f"New Priority: ")

    if new_completion:
        project.completion_percentage = int(new_completion)
    if new_priority:
        project.priority = int(new_priority)

main()
