import csv

FILENAME = "wimbledon.csv"

champions = {}
countries = set()
with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
    reader = csv.reader(in_file)
    next(reader)

    for row in reader:
        champion = row[2]
        country = row[1]

        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1

        countries.add(country)

print("Wimbledon Champions:")
for champion, count in sorted(champions.items()):
    print(f"{champion} {count}")

print("\nThese countries have won Wimbledon:")
print(", ".join(sorted(countries)))