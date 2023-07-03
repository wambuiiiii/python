# write a program to calculate ticket price for a movie theather based on the age of the customer
# 0-5 free
# 6-12 500
# 13-17 1000
# 18+yrs 1500
age=int(input("Enter your age:"))
if age>0 and age<=5:
    print("tickets are free")
if age>6 and age<=12:
 print("tickets-500")
if age>13 and age<=17:
     print("Tickets-1000")
if age>18:
    print("tickets-1500")