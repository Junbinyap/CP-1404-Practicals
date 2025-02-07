PASSWORD_LENGTH =10

password = input("Enter password: ")
while len(password) <= PASSWORD_LENGTH:
    print("Invalid Password")
    password = input("Enter password: ")

length = len(password)

print(f"{length * "*"}")