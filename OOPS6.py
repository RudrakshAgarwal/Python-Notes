#Static Method:
class Employee:
    no_of_leaves = 8

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

    @staticmethod #We just simply want to run this func independently without taking self argument or class argument.
    #just run the func whatever we have written.
    def print_good(string):
        print("This is Good " + string)


rudra = Employee("Rudraksh Agarwal",45000,"Website Designer")
rohan = Employee("Rohan Mehda",41000,"Graphic Designer")
karan = Employee.from_dash("Karan-480-Student")

print(karan.salary)
rudra.print_good("Rudraksh")
Employee.print_good("Samraat.")


''' 
Static Method in Python:
We know that a static method in Python is treated differently than in other languages. Static methods in Python are extremely similar to 
python class methods, but the difference is that a static method is bound to a class rather than the objects for that class.

To define a static method, we use @staticmethod decorator, which is a built-in decorator. Also, there is no need to import any module to use 
decorators. Using a static method in a class, we permit it to be accessed only by the class objects or inside the class.

There are few limitations related to static methods, such as:
1) Unlike, class method a static method cannot alter or change any variable value or state of the class.
2) Static methods do not have any knowledge related to class


Static methods do not require any knowledge related to the class that they are built-in. They are only formed in a class so that only the 
class instances can access them. We can use a static method for simple functionality that is mostly not related to the class. For example, 
we want to add two numbers together, but we do not want our method to be used elsewhere, other than the class, or through its instances, 
so we will create a static method. It will not require any information related to class as it only requires the numbers it has to add, but 
it will still fulfill its purpose as it is like a personal method that only the class has access to.

Most of the functionalities of the static methods can be performed using a class method. However, we prefer the static method, at places 
where it could work to make our program more efficient and faster as we do not have to pass self as a parameter, so the efficiency of the 
program increases.
In Python static methods can be created using @staticmethod.   

class Student:
@staticmethod
    def myfunc():
        //Code to be executed


Alternatively, we can follow the below syntax as well:

staticmethod(class_name.method())

Using @staticmethod annotation is actually a better way to create a static method in Python as the intention of keeping the method static is 
clear.

Advantages of Python static method
Static methods have a very clear use-case. When we need some functionality not for an Object but with the complete class, we make a method 
static. This is advantageous when we need to create utility methods.

Finally, note that in a static method, we do not need the self or cls to be passed as the first argument.
'''