import csv
from guitar import Guitar


def main():
    """Read guitars from a CSV file and display them."""
    guitars = load_guitars("guitars.csv")
    print("\nGuitars loaded from file:")
    for guitar in guitars:
        print(guitar)


def load_guitars(filename):
    """Read guitar data from a CSV file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                name, year, cost = row[0], int(row[1]), float(row[2])
                guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return guitars


if __name__ == "__main__":
    main()
