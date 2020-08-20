#Class Methods:

class Employee:
    no_of_leaves = 8

    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printDetails(self):
        return f"My Name is {self.name}. Salary is {self.salary}. and Role is {self.role}"

    @classmethod #This method will only access class ke instance variable
    #We make this class method so that we can access class through instance.
    def change_leaves(cls,newLeaves):
        cls.no_of_leaves = newLeaves


rudra = Employee("Rudraksh Agarwal",45000,"Website Designer")
rohan = Employee("Rohan Mehda",41000,"Graphic Designer")

rudra.change_leaves(34) #Now we can access class through instance also.
Employee.change_leaves(34)
print(rudra.no_of_leaves)
print(Employee.no_of_leaves)


''' 
We have been dealing with static methods until now. In Object-Oriented programming, there is a new concept of a class method, which we will 
see today in this lecture. They are very different from static methods as they are limited in their functionality to the class they are 
built-in. They can be called by using the class name and also can be accessed by using the object.

As we have observed in the previous tutorials, we cannot change the value of a variable defined in the class from outside, using an object. 
Instead, if we try that, a new instance variable will be created for the class having the value we assigned. But no change will occur in the 
original value of the variable.

We saw the use of self keyword in the previous tutorial. In this tutorial, we are going to know the working of a new keyword i.e., cls. 
Class methods take cls parameter that points to the class and not the object instance when the method is called.

Syntax:

class myClass:
    @classmethod
    def myfunc (cls, arg1, arg2, ...):

myfunc defines the function that needs to be converted into a class method

returns: @classmethod returns a class method for function.

Because the class method only has access to cls argument, it cannot modify object instance state. However, class methods can still modify 
class state that applies to all instances of the class. So a class method automatically recognizes a class, so the only parameter that 
remained to be passed is the function that needs conversion.

@classmethod Decorator:
We have covered decorators in detail in Tutorial #51, so here we are just doing to define the functionality of decorator instead of its 
working. A @classmethod Decorator is a built-in function in Python. It can be applied to any method of the class. We can change the value of 
variables using this method too.

Differences between Class Method and Static Method:

Class method:

1) Taking a class or, in short, form cls as an argument is a must for a class method.
2) With the help of class methods, we can change and alter the variables of the class.
3) Class methods are restricted to OOPs, so we can only use them if a class exists
4) We generally use class methods to create factory methods. Factory methods return a class object which is similar to a 
constructor for different use cases.

Static Method:

1) There is no such restriction of any specific parameter related to class in the Static method.
2) With a static method, we can not change or alter the class state.
3) The static method is not restricted to a class
4) Static methods are used to create utility functions.
'''
