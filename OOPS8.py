#Single Inheritance:

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

    @staticmethod
    def print_good(string):
        print("This is Good " + string)

class Programmer(Employee):

    def __init__(self,aname,asalary,arole,alanguage):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = alanguage


    def printprog(self):
        return f"The Programmer's name is {self.name}. Salary is {self.salary}. and the Role is {self.role} and the Languages programmer know {self.language}"

rudra = Employee("Rudraksh Agarwal",45000,"Website Designer")
rohan = Employee("Rohan Mehda",41000,"Graphic Designer")

shubham = Programmer("Shubham",47000,"Programmer",["Python","Java:Core"])
karan = Programmer("Karan",48000,"Programmer",["Python","CPP","Django"])
print(karan.printprog())

print(shubham.printprog())

#We can also call employee class methods as we inherit the properties of employee class.
print(karan.printDetails())


''' 
"Inheritance is the ability to define a new class(child class) that is a modified version of an existing class(parent class)"

Syntax:
class Parent_class_Name:
#Parent_class code block
class Child_class_Name(Parent_class_name):
#Child_class code block

The above syntax consists of two classes declared. One is the parent class or by other means, the base class, and the other one is the 
child class which acts as the derived class.

Two common terms related to inheritance are as follows:
1) Parent: As can be observed by the name. The parent class is the one that is giving access to its methods or properties to the child class 
or derived class.
2) Child: Child class is the one that is inheriting methods and properties from the parent class.


The class that is inheriting i.e. the child class can not only inherit all the functionality of the parent class but can also add its 
functionalities too. As we have already discussed that each class can have its constructors and methods, so in case of inheritance the child 
class can make and use its constructor and also can use the constructor of the parent class. We can simply construct it as we did for the 
parent class but OOP has provided us with a simple and more useful solution known as Super().

We will be discussing super() and overriding in our Super() and Overriding In Classes tutorial of the course.

Single inheritance exists when a class is only derived from a single base class. Or in other words when a child class is using the methods 
and properties of only a single parent class then single inheritance exists. Single inheritance and Multiple inheritance are very similar 
concepts, the only major difference is the number of classes. We will see Multiple Inheritance in our next tutorial.   

Different forms of Inheritance:

1) Single inheritance: When a child class inherits from only one parent class then it is called single inheritance.

2) Multiple inheritance: When a child class inherits from multiple parent classes then it is called multiple inheritance
Below is an example of single inheritance in python.

class Parent():
    def first(self):
        print('Parent function')
        
class Child(Parent):
    def second(self):
        print('Child function')

object1 = Child()
object1.first()
object1.second()

Output: 
Parent function
Child function


Advantages of inheritance:
1) It promotes code’s reusability as we do not have to copy the same code again to our new class.
2) It makes the program more efficient.
3) We can add more features to our already built class without modifying it or changing its functionality.
4) It provides a representation of real-world relationships.


In this tutorial, we have discussed the Inheritance concept. Inheritance is among the most significant concepts in object-oriented 
programming technique which provide code reusability, readability and helps in building optimized and efficient code.
'''