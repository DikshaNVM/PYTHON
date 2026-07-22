#day 3.3 check if a particular year is a leap year
year= int(input("enter a year:"))
if year%4==0:
  if year%100==0:
    if year%400 ==0:
      print("leap year")
    else:
      print(f"{year} is not a leap year")
  else:
    print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")