def function_name_print(a,b,c,d,e): #This approach is not suitable when we add larges of name, numbers etc.
    print(a,b,c,d,e)
function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

def funargs(normal, *args, **kwargs): #The prototype is fixed: first normal, then args and then kwargs. and this will take arguments as a tuple.
    print(type(args))
    print(normal)
    for item in args:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

har = ["Harry", "Rohan", "Skillf", "Hammad", "Shivam", "Rudra is a programmer"] #If we pass argument as a list or tuple idoesn't matter.
#Args will take argument as a tuple only.
normal = "I am a normal argument and the students are:"
kw = {"Rohan":"Monitor", "Rudra":"Fitness Instructor",
      "The Programmer": "Coordinator", "Soham":"Cook"} #by this we can add multiple values and func will automatically handle the no. of value we entered.
funargs(normal, *har,**kw) #By this method we can multiple names, numbers, etc acc to our requirement. and the order if fixed



'''
*args and **kwargs In Python:
We have worked with functions lately and also have made our own functions. We have seen that a function can only pass a certain number of 
arguments. The number of arguments has to be decided while defining the function, and it can not be changed while calling it. 
In simple terms, the number of arguments passed should be the same as the ones that are defined. If we dislike this restriction and do not want 
ourselves to be bound by certain limits, then we are lucky to have *args and **kwargs with us.

Before discussing *args and **kwargs, we should have a basic knowledge about types of arguments. In Python programming, there are two types of 
arguments that can be passed in a function.

1) positional arguments
2) keyword arguments


Positional arguments: are the one in which an order has to be followed while passing arguments. We have been dealing with them until now.

We know how normal functions work with positional arguments, so now we will directly start exploring keyword arguments. But to understand them, 
we have to know about asterisk or more commonly known in Perl 6 and ruby as a splat operator.

Asterisk is used in python as a mathematical symbol for multiplication, but in case of arguments, it refers to unpacking. 
The unpacking could be for a list, tuple, or a dictionary. We will discover more about it by defining *args and **kwargs.


*args:
args is a short form used for arguments. It is used to unpack an argument. In the case of *args, the argument could be a list or tuple. 
Suppose that we have to enter the name of students who attended a particular lecture. Each day the number of students is different, 
so positional arguments would not be helpful because we can not leave an argument empty in that case. So the best way to deal with such 
programs is to define the function using the class name as formal positional argument and student names with parameter *args. 
In this way, we can pass student's names using a tuple.

Note that the name args does not make any difference, we can use any other name, such as *myargs. The only thing that makes a difference is the
Asterisk(*).


**kwargs:
The full form of **kwargs is keyword arguments. It passes the data to the argument in the form of a dictionary. Let's take the same example 
we used in the case of *args. The only difference now is that the student's registration, along with the student's name, has to be entered. 
So what **kwargs does is, it sends argument in the form of key and value pair. So the student's name and their registration both can be sent 
as a parameter using a single ** kwargs statement.

Same as we discussed for args*, the name kwargs does not matter. We can write any other name in its place, such as **attendance. 
The only mandatory thing is the double asterisks we placed before the name.   

One of the instances where there will be a need for these keyword arguments will be when we are modifying our code, and we have to make a 
change in the number of parameters or a specific function.

'''