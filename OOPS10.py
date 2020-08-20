#Multilevel Inheritance

class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    def isdance(self):
        return f"Yes i can dance {self.dance} no. of times"

class Grandson(Son):
    dance = 6
    def isdance(self): #Overriding
        return f"Jackson Yeah!!" \
        f"Yes i can dance {self.dance} no. of times"

dadaji  = Dad()
beta = Son()
rudra = Grandson()

print(rudra.isdance())
print(rudra.basketball)


'''
In multilevel inheritance, a class that is already derived from another class is derived by a third class. 
So in this way, the third class has all the other two former classes' features and functionalities. 

Now let us dive into the priority brought by the ordering of the class. Suppose that we are looking for a constructor or 
a value for any variable. Our program will first check our current class i.e., Derived2, for it. 
If nothing found, then it will move towards Derived1 and in order at last towards Parent1 until it finds the constructor 
or variable in the way.

If we have the same method or variable in the base and derived class, then the order we discussed above will be followed, 
and the method will be overridden. Else, if the child class does not contain the same method, then the derived1 class method 
will be followed by the sequence defined in the paragraph above. 

Rules for Method overriding:-
There are few rules for Method overriding that should be followed:

The name of the child method should be the same as parents.
Inheritanceshould be there, and we need to derive a child class from a parent class
Both of their parameters should be the same.

Multiple inheritance VS. Multilevel inheritance:                                                                                            

Multiple inheritance:

1) Multiple Inheritance is where a class inherits from more than one base class.
2) Sometimes,multiple Inheritance makes the system more complex,that’s why it is not widely used.
3) Multiple Inheritance has two class levels; these are base class and derived class.

Multilevel inheritance:

1) In multilevel inheritance, we inherits from a derived class, making that derived class a base class for a new class.
2) Multilevel Inheritance is widely used. It is easier to handle code when using multilevel inheritance.
3) Multilevel Inheritance has three class levels, which are base class, intermediate class, and derived class.

Advantages of Inheritance   
1) It reduces code redundancy.
2) Multilevel inheritance provides code reusability.
3) Using multilevel inheritance, code is easy to manage, and it supports code extensibility by overriding the base class
   functionality within child classes

'''