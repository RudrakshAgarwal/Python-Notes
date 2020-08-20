'''
Design a Faulty calculator which will correctly solve all the problems except the following ones:*
45*3 =555,56+9= 77, 56/6=4
Your program should take operator and two no. as input from the user and then return the result.
'''

print("Enter which operator you want to use.\n"
      "Addition.\n"
      "Multiplication.\n"
      "Divide.\n"
      "Subtraction.")
operator = input()

print("Enter the two no. for a operations")
num1 = int(input())
num2 = int(input())
if "Addition"==operator:
    if num1==56 and num2==9:
        print("Result is 77")
    else:
        print("Result is:",num1+num2)
elif "Multiplication"==operator:
    if num1==45 and num2==3:
        print("Result is: 555")
    else:
        print("Result is:",num1*num2)
elif "Divide"==operator:
    if num1==56 and num2==4:
        print("Result is: 4")
    else:
        print("Result is:",num1//num2)
elif "Subtraction"==operator:
    print("Result is:",num1-num2)
