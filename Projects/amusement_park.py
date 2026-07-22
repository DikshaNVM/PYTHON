height= int(input("enter your height in cm:"))
if height >=120:
    print("you can ride the rollercoaster")
    age= int(input("enter your age:"))
    bill=0
    if age <12:
        print("your ticket is for $5")
        bill=5
    elif age <=18:
        print("your ticket is for $7")
        bill=7
    else:
        print("your ticket is for $10")
        bill=10
    #ask user if they want photos
    photo= input("do you want photos for $3? type Y for YES and N for NO: ")
    if photo=="Y" or"y":
        bill+=3
        print(f"your final bill incl. of photos is {bill}")
    else:
        print(f"your final bill is {bill}")
else:
    print("You can't ride!")

    

    