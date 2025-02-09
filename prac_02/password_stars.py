PASSWORD_LENGTH =10

password = input("Enter password: ")
"""Make sure the password is more then 10 length"""
while len(password) <= PASSWORD_LENGTH:
    print("Invalid Password")
    password = input("Enter password: ")

length = len(password)

print(f"{length * "*"}")