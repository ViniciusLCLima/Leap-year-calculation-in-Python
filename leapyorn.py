print("Let's find out if a year is leap or not?")
calculate="Y"
while calculate=="Y":
  ano=int(input("Type the year:"))
  if ano%400==0 or ano%4==0 and ano%100!=0:
    print("It's Leap")
  else:
    print("Not leap.")
  calculate=input("Want use again?(Y/N)")
print("End")
