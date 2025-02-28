"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))
    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)



def print_income_report(incomes):
    """Print the income report given a list of incomes."""
    print("\nIncome Report\n-------------")
    total = 0
    for i in range(len(incomes)):
        month = i + 1
        income = incomes[i]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

main()