import csv
FILENAME = "wimbledon.csv"

def main():
    """Main function to orchestrate the program."""
    rows = read_csv_file(FILENAME)
    champions, countries = process_wimbledon_data(rows)
    display_champions(champions)
    display_countries(countries)

def read_csv_file(filename):
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        return list(reader)

def process_wimbledon_data(rows):
    champions = {}
    countries = set()

    for row in rows:
        champion = row[2]
        country = row[1]

        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1

        countries.add(country)
    return champions, countries

def display_champions(champions):
    """Display Wimbledon champions and their win counts."""
    print("Wimbledon Champions:")
    for champion, count in sorted(champions.items()):
        print(f"{champion} {count}")

def display_countries(countries):
    """Display countries of Wimbledon champions in alphabetical order."""
    print("\nThese countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

main()