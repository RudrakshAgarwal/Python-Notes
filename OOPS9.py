#Multiple Inheritance

class Employee:
    var = 8
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

class Player:
    var = 9
    no_of_games = 4
    def __init__(self, name,game):
        self.name = name
        self.game = game
    def printDetails(self):
        return f"The name is {self.name} and the Game is {self.game}"

class CoolProgrammer(Player,Employee): #Order is important becoz agar me koi esa method use kr raha hu jo dono class me likha ho,
    #toh vo sabse phele us class ke method ko access karega jo sabse phele likhi ho.
    var = 10 #agar me is class ka var hata du toh vo Player class ke var ko print karega.
    Language = "Python"
    def printLanguage(self):
        print(self.Language)


rudra = Employee("Rudraksh Agarwal",45000,"Website Designer")
rohan = Employee("Rohan Mehda",41000,"Graphic Designer")

shubham = Player("Karan",["Cricket"])
karan = CoolProgrammer("karan",["Cricket"])

details = karan.printDetails()
print(details)
karan.printLanguage()
print(karan.var)


''' 
"In multiple inheritance a class is derived from more than one class i.e. multiple base classes. The child class in this case has features of 
both the parent classes."

As the name implies, python's multiple inheritance is when a class inherits from more than one class.This concept is very similar to 
multilevel inheritance, which also is our next topic of this course. It is also nearly the same as a single level inheritance because it 
contains all of the same functionality, except for the number of base classes. 

While using the concept of multiple inheritance, the order of placing the base classes is very important. Let us clear the concept using an 
example. Suppose we have a child class named Child1, and it has two base classes, named Base1 and Base2.

Example:
class Base1:
      def func1(self):
            print("this is Base1 class")
class Base2:
      def func2(self):
            print("this is Base2 class")

class Child(Base1 , Base2):
      def func3(self):
            print("this is Base3 class")

obj = Child()
obj.func1()
obj.func2()
obj.func3()

Output:
this is Base1 class

this is Base2 class

this is Base3 class

Now, when we are looking for some attribute, let it be a constructor. Then the program will search the current class i.e., the Child1 class 
first. If it does not find it in the Child1, it will look in the base class that is present at the leftmost side, which is Base1. After that, 
the program will start moving from left to right in a sequential manner, hence searching the Base2 class at the end. We should always give 
attention to the ordering of the base classes because it helps us a lot when multiple classes contain the same methods and also in method 
overriding. 

Method Overriding:
Override means having two methods that have the same name. They may perform same tasks or different tasks. In python, when the same method 
defined in the parent class is also defined in the child class, the process is known as Method overriding. This is also true when multiple 
classes have the same method and are linked together somehow.  


There are few rules for Method overriding that should be followed:

1) The name of the child method should be the same as parents.
2) Inheritance should be there, and we need to derive a child class from a parent class
3) Both of their parameters should be the same. 


In this case, the child method will run, and the reason for which, we have discussed in the paragraph above, related to ordering. 
Multiple inheritance is based on the same concept on which the single inheritance is based on i.e., DRY (do not repeat yourself). 
Multiple inheritance makes it easier to inherit methods and attributes from base classes that implement the functionality. When done right, 
we can reuse the code without having to copy-and-paste a similar code to implement interfaces.   
'''