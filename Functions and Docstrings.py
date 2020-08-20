def function1(a,b):
    print("Hello You are in function1.",a+b)

def funtion2(a,b):
    """This is a function which calculate average of two numbers
    this function doesn't work for three variables.""" #Docstrings.
    average = (a+b)/2
    #print(average)
    return average
v=funtion2(8,5)
print(v)
print(funtion2.__doc__) #Where there is a lot of functions in a program then we dus doctrings to describe the role of the fun.


''' 
Functions And Docstrings:
“Functions in Python can be defined as lines of codes that are built to create a specific task and can be used again and
again in a program when called.”

There are two types of functions in the Python language:
    1) Built-in functions
    2) User-defined functions

We have used a lot of built-in functions in our code till now, these functions include print(), or sum(), etc. So, 
we have a good idea about how to call a function. Built-in functions are already present in our python program, 
and we just have to call them whenever we need them to execute. Being familiar with built-in functions we will now 
look into User-defined function mostly in this tutorial. 

We must know how to define a function in Python in order to create one ourselves. We have to use the def keyword in 
order to define a function accompanied by the function's name with a pair of parentheses. The function of parenthesis 
is to send arguments or parameters to a function. In simple words, parameters can be defined as values that are sent 
in the parenthesis. For example, if a function is used to add two numbers then both the numbers will be passed as 
parameters in the parenthesis. After parenthesis, a colon is used to get in the body of the function. Some functions 
may return a value to the caller, so in order to get the value, a return statement is put at the end of the body of 
the function that gives the value that has been calculated by the function. 

Calling a function is very simple, we just have to write the name of the function along with the closing parenthesis. 
If the function requires some arguments then we write those in the parenthesis, but if it does not return anything, 
then we leave them empty. 

We have discussed a lot about what functions are and how to use them, now let us move to the advantages of using a 
function:

    1) If we are working on a big project then we will prefer to make as many functions as possible, so every other member 
    of our team could use that.
    2) By using functions, we can avoid the repetition of code to an extent. As we have discussed in the previous tutorial 
    more lines of code mean less efficiency. Also repeating the same code at different places will just make the code more 
    crowded than required.
    3) The reusability of code is ensured by using functions. We can even use a function inside another function or in any part
    of our code.
    4) By making a function of code that we are going to use again and again, we can save a lot of time.


Docstrings: 
Docstring is a short form of documentation string. Its purpose is to give the programmer a brief knowledge 
about the functionality of the function. It must be the first string in a function, and it is also an optional string 
but always good to have it while working on programs having multiple functions. The syntax for writing a docstring is 
very simple as it is just a string written in between three double quotes placed three times (""" """) on either side 
of the string. But it has to be the first line of code in the function’s body. To call a docstring we write the name 
of the function followed by ._doc_. 
'''