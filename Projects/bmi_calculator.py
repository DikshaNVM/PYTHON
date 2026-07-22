#BMI Calculator
print(input("Hello User! , Welcome to THE BMI Calculator . PRESS ENTER TO CONTINUE"))
heightfeet= float(input("Enter your height in feet: ")) #ask user for height in feet
heightinch =float(input("inches: ")) #in inches
weight = float(input("enter your weight in kilograms: ")) #weight in kg

ft_to_mtr1= heightfeet/3.281 #conversion of ft to mtr
ft_to_mtr2= heightinch/39.37 # conversion of inch to mtr

finalheight= ft_to_mtr1 + ft_to_mtr2 #final height

bmi = round(weight / finalheight**2 , 2)#formula

if bmi<18.5:
  print(f"your bmi is {bmi}. you're underweight!")
elif bmi<25:
  print(f"your bmi is {bmi}. you're healthy")
elif bmi <30:
  print(f"your bmi is {bmi}. you're overweight")
elif bmi<35:
  print(f"your bmi is {bmi}. you're obese")
else:
  print("your bmi is {bmi}. you're clinically obese")



