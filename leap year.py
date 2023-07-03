# create a program to check if a given year is leap year
# The year is divisible by 4 but not divisible by 100
# except if it is also divisible by 400
year = int(input("Enter the year:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:3
.year

    print("year is a leap year")
else:
    print("year is not a leap year")
