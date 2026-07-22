print("Welcome to la pino's pizza!")

size = input("what size of pizza do you want? S,M,L?: ").upper()
mushrooms = input("do you want to add mushrooms? Y or N? ").upper()
extra_cheese = input("do you want extra cheese? Y or N: ").upper()

bill = 0

# Base price
if size == "S":
    bill += 3
elif size == "M":
    bill += 6
elif size == "L":
    bill += 10

# Mushrooms
if mushrooms == "Y":
    bill += 1

# Extra cheese
if extra_cheese == "Y":
    bill += 1

print(f"your total bill is ${bill}, We accept all kinds of payment menthods")
print("THANK YOU FOR YOUR ORDER! SEE YOU SOON!")