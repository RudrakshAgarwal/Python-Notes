def function1():
    print("Subscribe Now.")

func2 = function1
del function1 #If we delete the function1 then also the value will print becoz we store the copy of function 1 in func2.
print(func2)

#------------Function inside function------------

def funcret(num):
    if num==0:
        return print #Hum ek function ke dwara ek function ko bhi return kr sakte hai.
    if num==1:
        return int
a = funcret(0)
print(a)

def f():
    def g():
        print("Hi, it's me 'g'")
        print("Thanks for calling me")

    print("This is the function 'f'")
    print("I am calling 'g' now:")
    g()
f()

# --------------------------------------

#-------------Function as Parameter------------

def executor(fun): #Hum function me as a argument ek aur function pass karva sakte hai.
    fun("this")
executor(print)


def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")

def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func()
f(g)

#-----------------------------------

#-----------DECORATORS-----------
def dec1(fun2):
    def dec_Exe():
        print("Executing now.")
        fun2()
        print("Executed.")
    return dec_Exe

@dec1 #This is short form to pass value in fun2.
def who_is_rudra():
    print("Rudra is good boy.")
# who_is_rudra = dec1(who_is_rudra)
who_is_rudra()




''' 
What is Python Decorator?
Decorator as can be noticed by the name is like a designer that helps to modify a function. The decorator can be said as a modification to 
the external layer of function, as it does not make any change in its structure. What a decorator does is, it takes a function and insert 
some new functionality in it without changing the function itself. A reference to a function is passed to a decorator and the decorator 
returns a modified function. The modified functions usually contain calls to the original function. This is also known as metaprogramming 
because a part of the program tries to modify and add functionality into another part of the program at compile time. Understanding the 
definition could be difficult but we can grasp the concept easily through the example in the video section. In terms of python, the other 
function is also called a wrapper.


A wrapper is a function that provides a wrap-around another function. While using decorator all the code that is executed before our 
function that we passed as a parameter and also the code after it is executed belongs to the wrapper function. The purpose of the wrapper 
function is to assist us. Like if we are dealing with a number of similar statements, the wrapper can provide us with some code that all the 
functions have in common and we can use a decorator to call our function along with wrapper. A function can be decorated many times. 

Note that a decorator is called before defining a function.

There are two ways to write a Python decorator:
1) We can pass our function to the decorator as an argument, thus define a function and pass it to our decorator.
2) We can simply use the @ symbol before the function we'd like to decorate.

def inner1(func): 
    def inner2():
        print("Before function execution"); 
        func() 
        print("After function execution")    
    return inner2 

@inner1
def function_to_be_used(): 
    print("This is inside the function") 

function_to_be_used()  


Advantages:
• Decorator function can make our work compact because we can pass all the functions to a decorator that requires the same sort of code that the wrapper provides.
• We can get our work done, without any alteration in the original code of our function.
• We can apply multiple decorators to a single function.
• We can use decorators in authorization in Python frameworks such as Flask and Django, Logging and measuring execution time.
'''