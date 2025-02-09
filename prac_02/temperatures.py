def main():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is {fahrenheit}°F")

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is {celsius:.2f}°C")

def celsius_to_fahrenheit(celsius):
    """convert celsius to fahrenheit"""
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """convert fahrenheit to celsius"""
    return (fahrenheit - 32) * 5/9

main()
