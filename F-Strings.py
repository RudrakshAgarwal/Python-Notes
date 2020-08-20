# F strings
import math

me = "Harry"
a1 =3
# a = "this is %s %s"%(me, a1)
# a = "This is {1} {0}"
# b = a.format(me, a1)
# print(b)
a = f"this is {me} {a1} {math.cos(65)}"
# time
print(a)

str1 = "Python"

str2 = "Programming"

print(f"Welcome to our {str1} {str2} tutorial")


'''
F-Strings & String Formatting In Python:
String formatting is used to design the string using formatting techniques provided by the particular programming 
language. From the % formatting to the format() method, to format string literals, there is no limit as to the 
potential of string crafting. There are four significant ways to do string formatting in Python. In this tutorial, 
we will learn about the four main approaches to string formatting in Python. 

1) String Formatting (% Operator)
    Python has a built-in operation that we can access with the % operator. This will help us do simple positional 
formatting. If anyone knows a little bit about C programming, then they have worked with printf statement, 
which is used to print the output. This statement uses the % operator. Similarly, in Python, we can perform string 
formatting using the % operator. For Example: 

name="Jack”

 n="%s My name is %s” %name

print(n)

 Output: "My name is Jack."
 
The problem with this method is when we have to deal with large strings. If we specify the wrong type of input type 
operator, then it will throw an error. For Example, %d will throw a TypeError if the input is not an integer. 

2) Using Tuple ()
    The string formatting syntax, which uses % operator changes slightly if we want to make multiple substitutions in a 
single string. The % operator takes only one argument, to mention more than one argument, use tuples. Tuples are 
better than using the old formatting string method. However, it is not an ideal way to deal with large strings. For 
Example: 

name=”Jack”
class=5
s=”%s is in class %d”%(name,class)
print(s)

Output: Jack is in class 5.

3) String Formatting (str.format)
    Python 3 introduced a new way to do string formatting. format() string formatting method eliminates the %-operator 
special syntax and makes the syntax for string formatting more regular. str.format() allows multiple substitutions 
and value formatting. We can use format() to do simple positional formatting, just like you could with old-style 
formatting: 

In str.format(), we put one or more replacement fields and placeholders defined by a pair of curly braces { } into a 
string. 

Syntax: {}.format(values)

For Example,

str = "This article is written in {} "

print (str.format("Python"))

Output: This article is written in Python.

This string formatting method is preferred over %-style formatting. Using the format() method, we can deal with large 
strings, and the code will become more readable. 


4) Using f-Strings ( f ):
    Python added a new string formatting approach called formatted string literals or "f-strings." This is a new way of 
formatting strings. A much more simple and intuitive solution is the use of Formatted string literals.f-string has an 
easy syntax as compared to previous string formatting techniques of Python. They are indicated by an "f" before the 
first quotation mark of a string. Put the expression inside { } to evaluate the result. Here is a simple example 

## declaring variables

 str1="Python”

 str2="Programming”

print(f"Welcome to our {str1}{str2} tutorial”)

Output: Welcome to our Python Programming tutorial.


Time Module:-

The time module provides time-related functions. It handles the time-related tasks. To use functions that are defined 
in this module, we need to import the module first. 

import time

It is mostly used in measuring the time elapsed during program execution.
'''