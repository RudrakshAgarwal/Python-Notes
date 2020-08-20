'''
Exercise 5: Health Management System
The task is to create a "Health Management System." Suppose you are a fitness trainer and nutritionist. You have to deal
with three clients, i.e., (Rudraksh, Rahul, Soham, Rishi). For each client, you have to design their exercise and diet
plan.

Instructions:
1) Create a food log file for each client
2) Create an exercise log file for each client.
3) Ask the user whether they want to log or retrieve client data.
4) Write a function that takes the user input of the client's name. After the client's name is entered, A message should
display "What you want to log. Diet or Exercise"
5) Use function

'''


# Health Management System
# 3 clients - Rudraksh, Soham and Rahul.

def getdate():
    import datetime
    return datetime.datetime.now()


# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

import datetime


def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("enter 1 for exercise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("Rudraksh-exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Rudraksh-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("Soham-exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Soham-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("Rahul-exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Rahul-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(rudraksh),2(soham),3(rahul)1")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for exercise and 2 for food"))
        if (c == 1):
            with open("Rudraksh-exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Rudraksh-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 2):
        c = int(input("enter 1 for exercise and 2 for food"))
        if (c == 1):
            with open("Soham-exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Soham-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 3):
        c = int(input("enter 1 for exercise and 2 for food"))
        if (c == 1):
            with open("Rahul-exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Rahul-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (rudraksh,soham,rahul)")


print("Health Management System: ")
a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for Rudraksh 2 for Soham 3 for Rahul "))
    take(b)
else:
    b = int(input("Press 1 for Rudraksh 2 for Soham 3 for Rahul "))
    retrieve(b)

