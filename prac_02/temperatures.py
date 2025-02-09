MENU = """
C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit
"""

def main():
    """main function"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            get_fahrenheit()
        elif choice == "F":
            get_celsius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def get_fahrenheit():
    """convert celsius to fahrenheit"""
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C is {fahrenheit}°F")

def get_celsius():
    """convert fahrenheit to celsius"""
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F is {celsius:.2f}°C")
main()
