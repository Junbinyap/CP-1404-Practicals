FILENAME= "name.txt"
name = input("Please enter your name: ")
file = open("FILENAME", "w")
file.write(name)
file.close()

# Q2
file = open("name.txt", "r")#open file in read mode
name = file.read().strip()  # strip() removes any extra spaces or newlines
file.close()#close file
print(f"Hi {name}!")

#Q3
with open("numbers.txt", "r") as file:
    number1 = int(file.readline().strip())
    number2 = int(file.readline().strip())

result = number1 + number2
print(result)

#Q4
total = 0

with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())
print(total)
