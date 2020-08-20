#Class Method as alternative Constructor

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
        # para = string.split("-")
        # print(para)
        # return cls(para[0], para[1], para[2])
        return cls(*string.split("-"))


rudra = Employee("Rudraksh Agarwal",45000,"Website Designer")
rohan = Employee("Rohan Mehda",41000,"Graphic Designer")
karan = Employee.from_dash("Karan-480-Student")

# rudra.change_leaves(34)
#
# print(rudra.no_of_leaves)

print(karan.name)


''' 
Now we will learn how to use a method as a constructor. It has its own advantages. By using a method as a constructor, we would be able to 
pass the values to it using a string.

Note that we are talking about a class method, not a static method.

The parameters that we have to pass to our constructor would be the class i.e., cls and the string containing the parameters. 
Moving on towards the working, we have to use a function "split()," that will divide the string into parts. And the parts as results will be 
stored in a list. We can now pass the parameters to the constructor using the index numbers of the list or by the concept of *args.

split():
Let us have a brief overview of the split() function. What split() does is, it takes a separator as a parameter. If we do not provide any, 
then the default separator is any whitespace it encounters. Else we can provide any separator to it such as full stop, hash, dash, colon, etc.
After separating the string into parts, the split() function, stores it into a list in a sequence. For example:

text = "Python tutorial for absolute beginners."
 t = text.split()
 print(t)
 
Here, we are not providing it any separator as a parameter, so it will automatically divide, taking whitespace as a separator. 

The output will be a list, such as:
['Python', 'tutorial', 'for', 'absolute', 'beginners.']

Example of Class methods - alternative constructor:
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

@classmethod 
    def from_dash(cls,string):
          return cls(*string.split("-"))

date1=Date.from_dash("2008-12-5")
print(date1.year)
#Output: 2008


If we want multiple and independent "constructors", we can use class methods. They are usually called factory methods. It does not invoke 
the default constructor __init__.In the above example, we split the string based on the "-" operator. We first create a class method as a 
constructor that takes the string and split it based on the specified operator. For this purpose, we use a split() function, which takes the 
separator as a parameter. This alternative constructor approach is useful when we have to deal with files containing string data separated 
by a separator.
'''