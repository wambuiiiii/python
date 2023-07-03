marks=int(input("Enter students score:"))
if marks>80 and marks<=100:
    print("You scored an A")
elif marks>60 and marks<=80:
     print("You scored a B")
elif marks>40 and marks<=60:
    print("You scored a C")
elif marks>30 and marks<=40:
    print("You scored a D")
elif marks>0 and marks<=30:
    print("Sorry you failed")
else:
    print("Wrong input")
    # create a program to check if a given year is leap year
    # The year is divisible by 4 but not divisible by 100
    # except if it is also divisible by 400