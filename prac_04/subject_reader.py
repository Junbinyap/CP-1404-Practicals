"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data"
def main():
    data = load_data()
    display_subject_details(data)

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)

    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        data.append(parts)
    input_file.close()
    return data

def display_subject_details(data):
    """Display subject details in a readable format."""
    print(f"{'Subject':<10} {'Lecturer':<20} {'Number of Students'}")
    print("-" * 50)  # Print a separator line
    for subject in data:
        print(f"{subject[0]:<10} {subject[1]:<20} {subject[2]:<15}")
main()