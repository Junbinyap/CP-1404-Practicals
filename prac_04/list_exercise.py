def main():
    numbers = []
    for i in range(5):
        num = float(input(f"Enter number {i + 1}: "))  # Get the number as a float
        numbers.append(num)  # Add the number to the list

    print("The numbers you entered are:", numbers)
    print("The smallest number is:", min(numbers))
    print("The largest number is:", max(numbers))
    print("The sum of the numbers is:", sum(numbers))
    print("The average of the numbers is:", sum(numbers) / len(numbers))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_input = input("Please enter your username: ")
if user_input in usernames:
    print("Access granted")
else:
    print("Access denied")

main()
