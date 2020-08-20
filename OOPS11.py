#Access Specifiers:

class Employee:
    no_of_leaves = 8 #public
    _protect = 9 #Protected
    __private = 98 #Private

    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printDetails(self):
        return f"My Name is {self.name}. Salary is {self.salary}. and Role is {self.role}"

    @classmethod
    def change_leaves(cls,newLeaves):
        cls.no_of_leaves = newLeaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def print_good(string):
        print("This is Good " + string)

emp = Employee("Rudra",78000,"Programmer")
print(emp._protect)

print(emp._Employee__private) #Name Mambling


'''
Public Access Modifier:

In public, all the functions, variables, methods can be used publicly. Meaning, every other class can access them easily 
without any restriction. Public members are generally methods declared in a class that is accessible from outside the class. 
Any ordinary class is by default, a public class. So, all the classes we had made till now in the previous tutorials were all public by default.

Protected Access Modifier:

In case of a protected class, its members and functions can only be accessed by the classes derived from it, i.e. its child class or classes. 
No other environment is permitted to access it. To declare a class as protected, we use a single underscore “_” sign before the data members 
of the class.

Private Access Modifier:

In the case of private access modifiers, the variables and functions can only be accessed within the class. 
The private restriction level is the highest for any class. To declare a class as private, we use a double underscore “_­_” sign before 
the data members of the class. Here is a suggestion to not try to access private variables from outside the class, 
because it will result in an AttributeError. 

Name mangling in Python:

Python does not have any strict rules when it comes to public, protected or private, like java. So, to protect us from using the 
private attribute in any other class, Python does name mangling, which means that every member with a double underscore will be changed 
to _object._class__variable when trying to call using an object. The purpose of this is to warn a user, so he does not use any private class 
variable or function by mistake without realizing it's states.

The use of single underscore and double underscore is just a way of name mangling because Python does not take the public, 
private and protected terms much seriously so we have to use our naming conventions by putting single or double underscore to let the 
fellow programmers know which class they can access or which they can't.


'''