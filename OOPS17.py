# Setters & Property Decorators:

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}11173@gmail.com"

    def explain(self):
        return f"This Employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set, Please set it using Setter."
        return f"{self.fname}.{self.lname}@codewithrudra.com"

    @email.setter
    def email(self, string):
        print("Setting Now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


rudraksh = Employee("Rudraksh", "Agarwal")
print(rudraksh.explain())
print(rudraksh.email)

rudraksh.fname = "Samraat"

print(
    rudraksh.email)  # The email will not change becoz during the creation of object i write "RUdraksh" "Agarwal" at
# that time constructor execute
# and it initilize email.

# Now if i dont want to use email as a function so i will declare @property decorator.

rudraksh.email = "this.that@codewithrudra.com"  # If i run this directly it will through eroor "Can't set this
# attribute" so to set this attribute
# we make setter.
print(rudraksh.fname)
print(rudraksh.lname)
print(rudraksh.email)

# Now if i want to delete the email then i have to declare deleter.

del rudraksh.email
print(rudraksh.email)

# Now mujhe nahu chahiye ki ye None.None@codewithrudra.com ese krke dikhayi de so me property me jaunga or usse set
# kr dunga.


'''In today’s tutorial, we are going over four of our main topics, i.e. Getter, Setter, Deleter and Property 
decorator. Let us start with property decorator. Before discussing property decorators, we must have an understanding 
of decorators themselves. Decorators are functions that take another function as an argument, and their purpose is to 
modify the other function without changing it. 

Note: For more information, visit the Decorators Tutorial, that is solely based on decorators. 

A property decorator is a built-in function in Python. Property decorator is a pythonic way to use getters and 
setters in object-oriented programming which comes from the Python property class. Theoretically speaking, 
Python property decorator is composed of four things, i.e. getter, setter, deleter and Doc. The first three are 
methods, and the fourth one is a docstring or comment. 

Ex-
@property
#def getter method
Use @property along with getter method to access the value of the attribute

Property decorator is used for setting the parameters. In Oop, the setter is a very important part of the program as 
we can change the values passed in parameters easily. Else without a setter, it is not possible to update the values 
passed as parameters during object creation. Setters are usually used in Oop to set the value of private attributes 
in a class. 

Setters are a great way of performing encapsulation that we discussed in Tutorial #59 of our Python Tutorials for 
beginners course. So by using setter, our interaction gets limited to the decorator, making the use of encapsulation 
concept, which is the basis of Oop. We can set new values for a newer object, or we can update values for an older one. 

Ex-
@function_name.setter
#def function
 @function_name.setter is a setter method with which we can set the value of the attribute

Deleter is used to delete the values passed as a parameter before. We can use a setter if we want to update or change 
the value, but we can not use it to delete the value. This is where deleter comes in; it removes the previous value 
and sets the variable equal to none. As in Oop we do not completely erase the existence of some variable but sets it 
equal to none. 

Ex-
# Deleter method 
@function_name.deleter
@function_name.deleter is a deleter method which can delete the assigned value by the setter method


Advantages of @property in Python:

Following are some advantages of using @property in Python: 
1) The syntax of defining @property is very concise and 
readable. 
2) We can access instance attributes while using the getters and setter to validate new values. This will 
avoid accessing or modifying the data directly. 
3) By using @property, we can reuse the name of a property. This will 
prevent us from creating new names for the getters, setters, and deleters. 



'''
