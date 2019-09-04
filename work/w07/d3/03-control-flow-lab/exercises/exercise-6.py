# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.


month = input("Enter the month of the season (Jan - Dec): ")
day = int(input("Enter the day of the month: "))

if month in ('Dec'):
  if day > 20:
    print(f"{month} {day} is in winter")
if month in ('Jan', 'Feb'):
    print(f"{month} {day} is in winter")
if month in ('Mar'):
  if day < 20:
    print(f"{month} {day} is in winter")

if month in ('Mar'):
  if day >= 20:
    print(f"{month} {day} is in Spring")
if month in ('Apr','May'):
    print(f"{month} {day} is in Spring")
if month in ('jun'):
  if day < 21:
    print(f"{month} {day} is in Spring")

if month in ('Sep'):
  if day >= 22:
    print(f"{month} {day} is in Fall")
if month in ('Oct','Nov'):
    print(f"{month} {day} is in Fall")
if month in ('Dec'):
  if day <= 20:
    print(f"{month} {day} is in Fall")

if month in ('Sep'):
  if day >= 21:
    print(f"{month} {day} is in Summer")
if month in ('Jul','Aug'):
    print(f"{month} {day} is in Summer")
if month in ('Sep'):
  if day < 22:
    print(f"{month} {day} is in Summer")