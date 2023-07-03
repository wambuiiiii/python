def Majina(fname, lname, age):
    print("My name is ", fname, "", lname, " and i am ", age, " years old")


Majina("Joy ", "Githinji", "19")
Majina("Anne ", "Nyambura", "49")
Majina("James ", "Muigai", "79")
Majina("James", "Muigai", 50)


def avaerage_num(numbers):

    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average
dataset=[10,29,20,20,80]
answer=avaerage_num(dataset)
print("average is",answer)

