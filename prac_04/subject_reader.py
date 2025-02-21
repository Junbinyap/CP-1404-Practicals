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
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            data.append(parts)  # Add the raw data as it is (keeping number as string)
    return data

def display_subject_details(data):
    """Display subject details in a readable sentence format."""
    for subject in data:
        subject_code = subject[0]
        lecturer = subject[1]
        # Convert the number of students when displaying
        num_students = int(subject[2])
        print(f"{subject_code} is taught by {lecturer} and has {num_students} students.")

