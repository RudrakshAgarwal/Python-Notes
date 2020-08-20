l = 10 #Global Variable(Goverment Property)

def function1(n):
    # l=5 #Local Variable(Private property)
    m = 8
    global l #the global keyword allows us to modify the global variable.
    # It is used to create a global variable and make changes to the variable in a local scope.
    l = l+45
    print(l,m)
    print(n,"I have Printed")
function1("This is me Rudra.")
# print(m)

#Quiz:
x=89
def rudra():
    x = 20
    def aman():
       global x
       x = 88
    print("Before calling aman()",x)
    aman()
    print("After calling Rudra()", x)
rudra()
print(x)

"""
Scope, Global Variables and Global Keyword:
Scope refers to the coding area where a particular Python variable is accessible. Hence one cannot access any 
particular variable from anywhere from the code. We have studied about variables in previous lectures. Recall that a 
variable is a label for a location in memory. It holds a value. Not all variables are accessible, and not all 
variables exist for the same amount of time. 

Where the variables defined determines that is it accessible or not, and how long it will exist.

Local vs. Global Variables

Local Variable:-
A variable that is declared inside a function or loop is called a local variable. 
In case of functions, when we define a variable within a function, its scope lies within the function only. 
It is accessible from the point where it is defined until the end of the function. 
It will exist for as long as the function is executing. Local variables cannot be accessed outside the function. 
The parameter names in the function, they behave like a local variable.

For Example,
def sum():

      a=10 #local variable cannot be accessed outside the function
      b=20
      sum=a+b
      print( sum)

print(a) #this gives an error

When you try to access variable “a” outside the function, it will give an error. It is accessible within the function 
only.

Global Variable:- 
On the other hand, a global variable is easier to understand; it is not declared inside the 
function and can be accessed anywhere within a program. It can also be defined as a variable defined in the main body 
of the program. Any function or loop can access it. Its scope is anywhere within the program.
 
For Example,
a=1  #global variable

def print_Number():

            a=a+1;
            print(a)

print_number() 

This is because we can only access the global variable, but we cannot modify it from inside of the function.


What if we want to modify the global variable inside the function?
For this purpose, we use the global keyword. In Python, the global keyword allows us to modify the global variable. 
It is used to create a global variable and make changes to the variable in a local scope. 

Rules of global keyword:
    1) If we assigned a value to a variable within the function body, it would be local unless explicitly declared as global.
    2) Those variables that are referenced only inside a function are implicitly global.
    3) There is no need to use the global keyword outside a function.
    
    
What if we have a nested function. How does the scope change?
When we define a function inside another function, it becomes a nested function. We already know how to access a 
global variable from a function by using a global keyword. When we declare a local variable in a function, 
its scope is usually restricted to that function alone. This is because each function and sub function stores its 
variables in its separate workspace. 

A nested function also has its own workspace. But it can be access to the workspaces of all functions in which it is 
nested. A variable whose value is assigned by the primary function can be read or overwritten by a function nested at 
any level within the primary. 
"""