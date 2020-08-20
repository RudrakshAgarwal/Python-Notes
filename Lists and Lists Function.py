'''List (List is mutable i.e can change)
Python lists are container that is used to store a list of values of any data type.
In simple words we can say that list is a collection of any data type items or elements.

E.g. list1 [‘harry’, ‘ram’, ‘Aakash’, ‘shyam’, 5, 4.85]

The above list contains strings, integer and even float type data.
It means above list contains any kind of data means it’s not mandatory to form list of only one data type.
List can contain any kind of data in it.
'''
grocery = ["Deodrant", "Oil", "Perfume", "Comb", 56]

print(grocery[4])

numbers = [2, 7, 9, 11, 3]
print(numbers[:])  # In this by default the value will take automatically 0 and length of the list i.e 5.
print(numbers[1:4])
print(numbers[::2])
print(numbers[1:5:2])  # 1 is index no., 5 is length, and 2 is skip value. numbers[Start:Stop:step]

'''List Functions
numbers.append(7)
numbers.insert(3,8)
numbers.pop(2)
numbers.remove(1)
numbers.sort()
numbers.reverse()
'''

'''
Tuple (Tuple is immutable i.e cannot change)

Tuple is an immutable data type in Python. Tuple is a collection of elements enclosed in () (parentheses). 
Tuple once defined can’t be changed i.e. its elements or values can’t be altered or manipulated.

To create tuple of one element it is necessary to put ‘,’ after that one element i.e. like this tup=(1,) because 
if we write only 1 then interpreter will understand it as a simple number or integer that’s why it’s important to use ‘,’ after single element.
'''

tp = (1, 5, 8)
print(tp)

a = ()  # it's an example of empty typle
x = (1,)  # tuple with single value i.e 1.
# SWAP
a = 1
b = 3
a, b = b, a  # By this we can swap two numbers.
