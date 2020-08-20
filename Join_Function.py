lis = ["John", "cena", "Randy", "orton",
       "Sheamus", "khali", "jinder mahal"]

for item in lis:
    print(item, "and", end=" ")

#Instead of using loop we can use join function to print this stuff:

a = ", ".join(lis) # We can simply use join func instead of running loop to pirnt such statements.                   
print("\n",a, "Others WWE Superstars")

'''
What is the join method in Python?
"Join is a function in Python, that returns a string by joining the elements of an iterable, using a string or character of our choice."

In the case of join function, the iterable can be a list, dictionary, set, tuple, or even a string itself. 
The string that separates the iterations could be anything. It could just be a comma or a full-length string. 
We can even use a blank space or newline character (/n ) instead of a string.

The syntax of the join() method is:
string.join(iterable)

the string is the name of string in which joined elements of iterable will be stored.

Note: If the iterable contains any non-string values, join() will raise a TypeError exception.

The implementation over the list iterable example is explained below. Here we join the elements of a list using a delimiter. 
A delimiter can be any character or nothing.

For Example:
#join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))


How will the join function work in case of a "dictionary"? Are there any limitations to join() function?
The join function has certain limitations. We must have a question in our mind that how will join function will work in case of a "dictionary" 
where there are values along with the keys. In the case of the dictionary, the join function will only return the key part, separated by the 
string in between, leaving the value side behind.

For Example:
myDictionary = {"name": "Jack", "country": "America"}
separator = "_separator_"
print(separator.join(myDictionary))

Output:
name_separator_country

As we are on the subject, let us discuss another limitation associated with the join method. In situations where the iterable consists of a 
multi-data type, such as a list or tuple consisting of all integer variables and one single, double variable, the join function will not work. 
Instead, it will display an error. For join to function properly, all the variables should have the same sort of data type, either it is an 
integer, string, or any other.

For Example:
inputlist = ["Test1",13,"Test2",24,"Test3",100,"Test4"]
sep = '_'
out = sep.join(inputlist)
print(out)

Output:
Traceback (most recent call last): File "./prog.py", line 3, in TypeError: sequence item 1: expected str instance, int found
'''