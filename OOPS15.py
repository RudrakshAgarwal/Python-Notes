#Operator Overloading & Dunder Methods

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

    def __add__(self, other): #It is a special method which is called dunder method and that's help to achieve operator overloading.
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp1 = Employee("Harry", 345, "Programmer")
# emp2 =Employee("Rohan", 55, "Cleaner")
print(str(emp1)) #This will run __str__ method first not --repr-- method. but if we want to call __repr__ method the we have to call it like this
#print(repr(emp1))


''' 
Operator Overloading In Python:
Operator overloading means to give new meanings to an operator. In simple words, it means to assign new functionality to an operator beyond 
its normal functioning. We will go with the most common and easiest that we could find related to the concept i.e., the + sign. For numbers, 
it is used for addition between them, but in case of a string, it is used to join or combine two strings, working differently in two 
different scenarios. The operators are methods defined in respective classes. Defining methods for operators is known as operator overloading.


Python Dunder Methods Or Special Functions:
Dunder methods in Python are special methods. In Python, we sometimes see method names with double undescore (__), such as __init__ method 
that every Class has. These methods are called “dunder” methods. In Python, Dunder methods are used for operator overloading and for 
customizing the behaviour of some other function.

Python usually calls dunder methods under the hood. Suppose we want to join a string with a number using the + sign. Now joining between two 
different data types is not possible in Python, and the resultant in such a case will be an error. So for this purpose, we can use a function 
provided to us by Python, named as dunder function. We will write such code in it that it may first convert the number to a string and then 
join them or any other logic will be fine too until it does what we require. We can even return 85, regardless of what string or number is 
given to us, it is all up to us. 

Methods starting with a double underscore ( __ ) and ending with a double underscore ( __ ) represents dunder methods.

Check https://docs.python.org/3/library/operator.html to explore more about operator overloading.


_str__ and __repr__ functions
Both of these built-in methods are used to return a presentable description about any object rather than the default one. The difference in 
them is the way of writing them. The __str__ method is mainly written for the end-user, while __repr__ is written for a developer. It is 
overridden to return a printable string representation of any user-defined class. An interesting thing to note here is that the priority 
of __str__ is greater than __repr__. This means that if we pass an object into a print statement, it will return us the __str__ string even 
if __repr__ is also present there. In such cases, if we want to print __repr__, we have to call it exclusively with the object name in the 
print statement.


Difference between __str__ and __repr__ functions:
1) If the implementation of __str__ is missing, then __repr__ function is used as a fallback. If the implementation of __repr__ is missing, then there will be no fallback.
2) If __repr__ function is returning the String representation of the object, we can skip the implementation of __str__ function. 
3) The priority of __str__ is higher than __repr__.
'''
