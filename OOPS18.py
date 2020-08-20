#Object Introspection:

class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}11173@gmail.com"

    def explain(self):
        return f"This Employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set, Please set it using Setter."
        return f"{self.fname}.{self.lname}@codewithrudra.com"

    @email.setter
    def email(self,string):
        print("Setting Now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf =Employee("Skill", "F")
# print(skillf.email)
o = "this is a string"
# print(dir(skillf))
# print(id("that that"))

import inspect
print(inspect.getmembers(skillf))



''' 
In today’s tutorial, we are going to learn about object introspection. We have used it a bit in our previous tutorial but never discussed 
it in depth. As we have discussed earlier that everything in Python is an object. All the functions we use regularly are predefined in some 
built-in class. For example, while printing any string, we are using the object of an str class that is predefined for the usage of string.

Object Introspection in Python
Introspection can be said as the ability to recognize the object along with all its details, such as id or location at runtime. One of the 
most basic introspect we came across many times earlier is type(). 

Ex-
type(object)

We used it to see the type of our object, that whether it is int, float or string. We have to pass the object in the parenthesis, and the 
compiler will return the type. Introspection gives us useful information about the program’s objects. Python provides tremendous 
introspection support. Introspection is an ability to determine the type of an object at runtime. Henceforth, by using introspection, 
we can inspect the Python objects dynamically. 

There are many types of introspects. In this tutorial, we will focus on three of them so you may get a brief idea about their working. 
You may search the internet for more, but for conceptual learning, we will be focusing on three. We have already discussed type( ), now 
let’s ,move onto id( ). Id provides us with the id allocated to the particular object. The id of each object is unique, meaning it is 
different, and no two objects can have the same id. 

Ex-
id(object)

Now the most important introspection function is dir(). It returns us a list of attributes and methods associated with an object. By using dir(), we can check the attributes that our object is composed of. It is mostly executed before and after updating our object by inserting more attributes or methods. 

Ex-
o = MyClass()
print(dir(o))


Types of introspects:-

Some of the other common Introspects:
1) hasattr(): It checks if an object has an attribute.
2) getattr(): 	It returns the contents of an attribute if there are some.
3) repr(): It returns the string representation of an object
4) vars(): It checks all the instance variables of an object
5) issubclass(): This function checks that if a specific class is a derived class of another class.
6) isinstance(): It checks if an object is an instance of a specific class. 
7) __doc__: This attribute gives some documentation about an object 
8) __name__: This attribute holds the name of the object.
9) callable(): This function checks if an object is a function.
10) help(): It checks what other functions do
    


'''