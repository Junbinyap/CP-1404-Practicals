"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
- The ValueError occur when you enter a float number as it already stated that need to enter a int number.
2. When will a ZeroDivisionError occur?
- The ZeroDivisionError will occur when the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
- The code can be modified to avoid a ZeroDivisionError by checking if the denominator is zero before performing the division like example add a if else statement.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
       print("Cannot divide by zero!")
    else:
       fraction = numerator / denominator
       print(fraction)
except ValueError:
       print("Numerator and denominator must be valid numbers!")
print("Finished.")

