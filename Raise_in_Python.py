a = input("What is your name")
b = input("How much do you earn")
if int(b)==0:
    raise ZeroDivisionError("b is 0 so stopping the program")
if a.isnumeric():
    raise Exception("Numbers are not allowed")

print(f"Hello {a}")
#1000 lines taking 1 hour.

c = input("Enter your name")
try:
    print(d)

except Exception as e:
    if c == "Rudraksh":

        raise ValueError("Rudraksh is blocked, He is not Allowed.")

    print("Exception Handled.")


'''Raise In Python: 
You all must remember that in try_except and else_and_finally_in_Try_Except, we learned a few ways to handle the 
exception. In try_except, we learned about try and catch. In the try block, we write the code in which an exception 
might occur, and in except block, we write the code as a result if an exception occurs. 

Moreover, in else_and_finally_in_Try_Except, we learned about else and finally. We use an else keyword to print 
something in cases where no exception occurs. It is also known as code cleaner because it will perform its action, 
either an exception occurs or not 

First, let us briefly go over the meaning of the word exception. The exception is an error that halts the program's 
normal functioning and displays an error onto the screen. While the try and except block are for handling exceptions, 
the raise keyword, on the contrary, is to raise an exception. 

Following is the syntax:

Syntax of raise keyword is:
    if test_condition:
    raise EXCEPTION_CLASS_NAME

Taking a simple usage example:
    raise ZeroDivisionError
    
Python has a range of built-in exceptions that we can use for our benefit. We can learn and read about the exceptions 
by visiting https://docs.python.org/3/library/exceptions.html Python documentation of python site. Few of these 
exceptions include: 

    KeyError: Raised when a mapping key is not found in the set of existing keys.
    ValueError: Raised when a function receives an argument with the right type but an inappropriate value.
    EOFError (End Of File Error): Raised when the input() function hits an end-of-file condition without reading any data.
    ImportError: Raised when the import statement has trouble trying to load a module.
    NameError: Raised when a local or global name is not found.
    ZeroDivisionError: Raised when the second argument of a division is zero.
    
These are only a few names. We will discuss few build-in exceptions in our code today, but you can search for more on 
the internet according to your requirement as nearly every possible exception is already out there. Covering so many 
of them in a single tutorial is not possible, so I will give you an idea about them with examples where I will use 
the most frequently used exceptions. We can also make a custom or user-defined exceptions that fulfills our purpose. 

Example:-
Before moving onto their detailed work, let us cover the reason for their use. Suppose we have made a program in 
which we want a number which is greater than 10. Now the user is giving the input (x),  5. So in such a case, 
we can raise ValueError, returning an error to the user that the input is wrong. By doing this, we can save the 
program running time and prevent the program from storing the wrong input. 

You can use the raise keyword to signal that the situation is exceptional to the normal flow. For example:
    x = 5
    if x < 10:
       raise ValueError('x should not be less than 10!')
       
Notice how you can write the error message with more information inside the parentheses. The example above gives the 
following output (by default, the interpreter will print a traceback and the error message): 

    >>>
    Traceback (most recent call last):
    File "C:/Python34/Scripts/raise1.py", line 3, in <module>
    raise ValueError('x should not be less than 10!')
    ValueError: x should not be less than 10!
    >>>
'''