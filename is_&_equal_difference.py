# == - value equality - Two objects have the same value
# is - reference equality - Two references refer to the same object


# Task:
a =[6, 4 , "34"]
b = [6, 4 , "34"]
print(b is a)
print(id(a))
print(id(b))

#False Becoz of their having a different memory location

''' 
Python 'is' vs '==': What's The Difference?
Our today's tutorial is related to a very basic yet very important concept. We are going to learn about the 
difference between 'is' and '=='. We have been using them both in our programs from the start. Sometimes one of them 
also works in place of the other. However, there is a huge difference in the working between the Python identity 
operator (is) and the equality operator (==) that we are going to cover in this tutorial. 


Equality operator (==) in Python:
'==' is used to represent value equality. Value equality means that two variables or objects or even data structures 
such as list composes of the same value. Suppose we have two variables a and b. We assign the value 2 to both of 
them. Now, as we know that they do not have any direct link with each other, the only similarity is that they have 
been given the same value. So, if we place an '==' sign between them, the output will be True. However, 
when we change the value of one of the variables, it will return false. 

For Example:-
    x = [1, 2, 3, 4]
    y= [1, 2, 3, 4]
    x == y
    #True
In this example, 'x == y' returns true because what x is referencing contains the same things that y is referencing.


Identity operator (is) in Python:
'is' is generally used to denote reference equality. The data structure or variables in the case has to be the same. 
In the case of the object, the objects must be referring to the same kind of data. In case we use a copy of our 
variable or data structure or even make a similar one with the same values, it will still return False as their 
reference is not the same. For example, if we assign a list to two different objects, then the 'is' keyword will 
return true as they are both referring to the same list. In case we change an entry in the list, it will also be 
changed for the other one, so no change in output. 

For Example:-
    c = [1, 2, 3]
    d = [1, 2, 3]
    c == d #True
    c is d #False

When we assign a list to a variable, Python allocates memory for that list, but the actual list is not stored in our 
variable. Instead, Python creates a list object and stores a reference to that object in the variable. However, 
in the above example, c = [1, 2, 3, 4] and d = [1, 2, 3, 4] 

This creates a list object and stores a reference to it in c; then, it creates a second list object and stores a 
reference to it in d.

‘c == d’ is still true. However, 'c is d' is now false. This is because of both c and d reference to different objects.
 
So, to recap the difference between "is" and "==" into short definitions: 
    1) An identity operator(is) expression evaluates to True if two variables point to the same object. 
    2) An equality operator ( == )expression evaluates to True if the objects referred to by the variables have the same 
    contents. 

The identity operator 'is' tracks the object back to its identity while the equality operator '==' only compares the 
values. 
'''