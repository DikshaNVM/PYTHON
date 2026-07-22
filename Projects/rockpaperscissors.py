import random
rock='''
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)'''
paper='''
      _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________)'''
scissors='''
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)'''
images=[rock,paper,scissors]
user=int(input("What do you choose? Type 0 for Rock , 1 for Paper and 2 for Scissors: \n"))
if user>2:
    print("please enter a number between 0 and 2")
else:
    print(f"YOU CHOSE:\n{images[user]}\n")
computer=random.randint(0,2)
print(f"COMPUTER CHOSE:\n{images[computer]}\n ")

if user==0 and computer==2:
  print("YOU WIN")
elif user==1 and computer==0:
  print("YOU WIN")
elif user==2 and computer==1:
  print("YOU WIN")
elif user == computer:
  print("OOPS, IT'S A DRAW")
else:
  print("YOU LOSE")