s= set()
print(type(s))
l= [1,2,3,4]
s_from_list = set(l)
print(s_from_list)
print(type(s_from_list))
s.add(1)
s.add(2)
s1=s.union({1,2,3})
print(s,s1)
s1=s.intersection({1,2,3})
print(s,s1)
s2 = {4,6} #set
print(s.isdisjoint(s2))
print(len(s))

'''
“A set is a data structure, having unordered, unique and unindexed elements.”

Elements in a set are also called entries and no two entries could be similar within a set.

If your curiosity isn’t satisfied with the basic definition than do not worry as we are approaching towards a more formal approach of understanding of the sets.

Well, you all have studied sets in basic mathematics.
A python set hold all the same properties and attributes of the basic mathematics set. The union, intersection, disjoint, etc.
All methods are exactly the same that we can now perform in python language too.

Furthermore:

Sets are iterable(iterations can be performed using loops)
They are mutable (can be updated by adding or removing entries)
Here is no duplication (two same entries do not occur)

Structure:

Elements of the sets are written in between two curly brackets and are separated with a comma, and by this simple way we can form a set in Python.
The other way for the forming a set is by using a built-in set constructor function.
Both of these approaches are defined in the tutorial above.

Sharing some basic knowledge about sets so you know why they are so important and why should you learn them:

Unlike dictionary (that we have learned in lecture 10 and 11) sets are not just restricted to Python language, 
but nearly all the commonly used languages have sets included in them as a data type. Examples of the languages include, C, C++, java, etc., 
even languages such as Swift and JavaScript also support sets. One of the earliest languages that supported sets was Pascal. 
So now you have a rough idea, how important the sets actually are because which ever language you choose to code in, 
you must have an understanding of sets because they are being used everywhere.

Restrictions:

Everything has a limit to its functionality, same as that there are some limitations on the working of sets too.

Once a set is created, you can not change any of its item, although you can add new items or remove previous but updating an already existing item is not possible.
There is no indexing in sets, so accessing an item in order or through a key is not possible, 
although we can ask the program if the specific keyword we are looking for is present in the set by using “in” keyword or 
by looping through the set by using a for loop(we will cover for loops in lecture # 16 and 17)


Methods:

There are already a lot of built-in methods that you can use for you ease and can be easily accessible through the internet. 
Some of the methods include union(), discard(), add(), isdisjoint(), etc. and their functionality is same as in 
basic mathematics and their functions can easily be understood by their names.
'''