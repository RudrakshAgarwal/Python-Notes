f1 = open("Rudra.txt")
try:
    f=open("does.txt")

except EOFError as e:
    print("EOF Error Occur",e)

except IOError as e:
    print("IO error Occur",e)
else:
    print("This will run only if except is not running")
finally:
    print("This finally statement will run in any way weather try or except block run or not...")
    f1.close()
print("Important Stuff")

'''
try and except block: In the try block, we write the code in which an exception might occur, and in except block, 
we write the code as a resultant if an exception occurs. This could either be a print statement or the error itself. 
If no exception occurs, the except block will not execute. The purpose of try and except is to keep the program 
running either an error or exception occurs. In simple programs, if an error occurs, the program stops its execution 
and displays the error onto the screen. By using try an except we can show the error as a string onto the screen and 
the program could continue its execution after that. For further explanation, you can give Tutorial #24 a watch or 
read the description given below. 

else keyword:- Now moving onto the else keyword. We use an else keyword to print something in cases where no 
exception occurs. Suppose that an exception occurred, and the except block is printing the error, likewise if the 
exception does not occur, we can print a statement that no error occurred, using an else keyword. Syntax of using 
else with try and except block is: 

try:
    #Run this code
except Exception as error:
    #Execute this code when there is an exception
else:
    #No Exception. Run this code

Note: An else will only run in case where no exception occurs.

For Example:-
def divide(a, b):
    try:
        print(f'{a}/{b} is {a / b}')
    except ZeroDivisionError as e:
        print(e)
    else:
        print("No Exception")
divide(1, 2)

Output:-
1/2 is 0.5
No Exception


finally:- Now the last keyword for this tutorial i.e., finally, will run in either case. It is also known as code 
cleaner because it will perform its action, either an exception occurs or not. We write such commands in the finally 
part of code that we want to execute even an exception occurs or not. It is mostly used to clean resources or close 
files. 

try:
    #Run this code
except Exception as error:
    #Execute this code when there is an exception
else:
   #No Exception. Run this code
finally:
   #Always run this code
   
   
Summing Up
After seeing the difference between these four keywords, we learned about various ways to handle exceptions in Python. 
In this tutorial, so studied that:

1) In the try block, all the statements are executed until an exception occurs.
2) Except block is used to catch and handle the exception(s) that occurs during the execution of the try block.
3) Else block runs only when no exceptions occur in the execution of the try block.
4) Finally block always run, either an exception occurs or not.   

'''
