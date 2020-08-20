#Self & __init__() (Constructor)

class Employee:
    no_of_leaves = 8

    def __init__(self,aname,asalary,arole): #Constructor. It takes argument.
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printDetails(self): #Self means vo object jis pr ye function lagega. i.e rudra.printDetails so self is rudra.
        #It will print the details of the particular instance.
        return f"My Name is {self.name}. Salary is {self.salary}. and Role is {self.role}"

rudra = Employee("Rudraksh Agarwal",45000,"Website Designer")
rohan = Employee("Rohan Mehda",41000,"Graphic Designer")

print(rudra.name,"\n",rudra.salary,"\n",rudra.role)
print(rudra.printDetails()) #rudra is automatically passes as aargument to printDetails fun and it will catch by slef parameter.
print(rohan.printDetails())


''' 
Method:
A method is just like a function, with a def keyword and a single parameter in which the name of the object has to be passed. 
The purpose of the method is to show all the details related to the object in a single go. We choose variables that we want the method to 
take but do not have to pass all of them as parameters. Instead, we have to set the parameters we want to include in the method during 
its creation. Using methods make the process simpler and a lot faster. 

Self keyword:
The self keyword is used in the method to refer to the instance of the current class we are using. The self keyword is passed as a 
parameter explicitly every time we define a method.

def read_number(self):
        print(self.num)

__init__ method:-
"__init__" is also called as a constructor in object-oriented terminology. Whereas a constructor is defined as:

"Constructor in Python is used to assign values to the variables or data members of a class when an object is created."

Python treats the constructor differently as compared to C++ and Java. The constructor is a method with a def keyword and parameters, 
but the purpose of a constructor is to assign values to the instance variables of different objects. We can give the values by accessing 
each of the variables one by one, but in the case of the constructor, we pass all the values directly as parameters. Self keyword is used 
to assign value to a constructor too.  

As there can be only one constructor for a specific class, so the name of the constructor is a constant, i.e., __init__.

We declare a constructor in Python using def keyword,

def __init__(self):
    # body of the constructor

Here,
1) The def keyword is used to define the function.
2) The first argument refers to the current object which binds the instance to the init() method.
3) In init() method ,arguments are optional. Constructors can be defined with any number of arguments or with no arguments.

For Example:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1.name) 
#Output: John

Types of constructors in Python:
We have two types of constructors in Python.

1) The default constructor is the one that does not take any arguments.
2) Constructor with parameters is known as parameterized constructor.

Method vs. Function:
Methods and functions are very similar, yet there are some differences:

1) Methods are explicitly for Object-Oriented programming.
2) The method can only be used by the object that it is called for. In simple terms, for a method, the parameter must be an object.
3) The method can only access the data that is initialized in the class the method is formed in. 
'''
