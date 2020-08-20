#Super  and Overriding in classes:
class A:
    classvar1 = "I am a Class Variable in class A" #Class Variable
    def __init__(self):
        self.var1="I am inside Class A's Constructor "
        self.classvar1="Instance Var in Class A" #Instance Variable
        self.special="Special,"

class B(A):
    classvar1="I am a CLass Variable in Class B"
    def __init__(self):
        super().__init__() #Ye phele call hoga fir class ke speical,var1 or classvar1 ko access karega fir niche aayega or class A ke members
        # ko override karega and then fir class B ke var1 or classvar1 ko karega print.
        self.var1 = "I am inside Class B's Constructor"
        self.classvar1 = "Instance Var in Class B"
        # super().__init__()
        # print(super().classvar1)

a = A()
b = B()
print(b.special,b.var1,b.classvar1)

#Agar print(b.classvar1) se me print karau toh vo sabse phele class B me jake search karega ki koi instance variable hai, if hota hai toh
# print kare dega and if nahi hota hai toh class A me jake search karega, if waha bhi nahi hota toh fir class variable ko search karega Class B
# and Class B me agar class variable bhi na mile toh vo fir class A me jake class variable ko search karega or print kar dega.


'''
As you people might have noticed that we came across super and overriding keywords, a lot of time in a few of our previous tutorials, 
but did not get into its detailed working. The reason for that was to give you an idea of concepts leading to the use of super() and 
overriding first. In this tutorial, we are going to discuss it in detail, using the single inheritance as an example.

Yet being different concepts, they are often used together. The need for superclass arises when overriding is being done at a certain point 
in our code. Overriding is an essential part of object-oriented programming since it makes the inheritance utilize its full power. 
Overriding avoids duplication of code, and at the same time enhance or customize the part of it. It is a part of the inheritance mechanism. 
Let us get a description of overriding first so that we can dive into the concept of super() later. 


How to override class methods in Python?
Overriding occurs when a derived class or child class has the same method that has already been defined in the base or parent class. 
Being the same methods with the same name and number of parameters, when called checks for the method first in a child class, and runs it 
ignoring the method in the parent class because it is already overridden. In the case of Instance variables, the case is a little different. 
When the method is called, the program will look for any instance variable having the same name as the one that is called in the child, 
then in the parent, and after that, it comes again into child class if not found.


Where does super() fit in all this?

When we want to call an already overridden method, then the use of super function comes in. It is a built-in function, so no requirement 
of any module import statement. What super does is, it allows us the use of the method of our superclass, that in the case of inheritance 
is the parent class. Syntax of using super() is:

class Parent_Class(object):
      def __init__(self):
            pass

class Child_Class(Parent_Class):
     def __init__(self):
           super().__init__()
           
super() returns a temporary object of the superclass that then allows you to call that superclass’s methods. The primary use case of super() 
is to extend the functionality of the inherited method.

We have discussed earlier that in case of method overriding, the previous method could not be called, but super makes an exception, and 
thus we can partially or completely use the method of the parent class too. We can even use super() to call only a specific variable we used 
in our overridden method. Calling the superclass built methods with super() saves us from rewriting those methods in our subclass, and 
allows us to swap out superclasses with minimal code changes.

'''
