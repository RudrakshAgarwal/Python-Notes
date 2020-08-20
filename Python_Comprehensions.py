ls = [] #List
for i in range(100):
     if i%3==0:
         ls.append(i)

ls = [i for i in range(100) if i%3==0]

print(type(ls))
print(ls)

dict1 = {i:f"item {i}" for i in range(1, 10001) if i%100==0} #Dictionary
dict1 = {i:f"Item {i}" for i in range(5)}

dict2 = {value:key for key,value in dict1.items()} #Reverse Dict.
print(type(dict1),"\n",type(dict2))
print(dict1,"\n",dict2)

dresses = [dress for dress in ["dress1", "dress2","dress1",
                               "dress2","dress1", "dress2"]] #List

dress = {dress for dress in ["dress1", "dress2","dress1",
                               "dress2","dress1", "dress2"]} #This is Set, It will not repeat the the values.
print(type(dresses))
print(type(dress))
print(dresses)
print(dress)


evens = (i for i in range(100) if i%2==0) #Generator
print(type(evens))
print(evens.__next__())

for item in evens:
    print(item)




''' 
Comprehensions in Python can be defined as the Pythonic way of writing code. Using comprehension, we compress the code so it takes less 
space. Comprehension in Python converts the four to five lines of code into a one-liner. In this tutorial, we will see the ways to write 
the code we used to write earlier in four to five lines, in just one line.

Comprehension’s importance comes in the scenarios when the project is too big, for example, Google is made up of 2 billion lines of code, 
Facebook is made from 62 million lines of code, Windows 10 has roughly 50 million lines of code. So in such scenarios, comprehension has to 
be implemented as much as we can so that the lines of code decreases and the efficiency increases. 

In Python 2.0, we only had the option of list comprehensions, but now after 3.0 version, we can also apply comprehension on dictionary and 
sets. We will discuss all three of them in this tutorial along with its implementation on generators. We have already discussed all of 
these topics before in our previous tutorials. I will provide you with a link to them so if you have somehow missed any of those, you may 
watch them or give the description a read. 

1) Sets
2) List
3) Dictionary
4) Generators

We will now learn ways to create a comprehensive way of implementing the functions. The concept is the same; the only difference comes in 
writing them i.e. in a more compact form.

1) List as ordinarily are written as such:

listA = []
for a in range(50):
    if a%5==0:
        listA.append(a)

While it can be written in a one liner format using comprehension as such:

listA = [a for a in range(50) if i%5==0]
The compressed code works exactly like the one above but with more precision.


2) Set comprehension works exactly the same way as List comprehension. The syntax is almost the same two, except for the brackets i.e. 
set uses curly brackets. The main difference arrives while priting the items as a set will only print the same items once. 

alpha = {alpha for alpha in ["a", "a", "b", "c", "d", "d"]}

The output will be: {'a', 'b', 'c', 'd'}

3) In the case of the dictionary, it has more benefits as we can alter the sequence of the dictionary by printing the values before the 
keys. We can also write conditional statements, that in the case of dictionary consumes 8-9 lines in just a single one. The syntax for a 
dictionary using ordinary syntax is:

Normaldict = {
  0 : "item0",
  1 : "item1",
  2 : "item2",
  3 : "item3",
  4 : "item4",
}

And the more compact one is:'

Compdict = {i:f"Item {i}" for i in range(5)}


4) We can implement comprehension on generators too. We discussed Generators in the previous tutorial. We will again see its syntax here:

def gener(n):
    for i in range(n):
        yield i

a = gener(5)
print(a.__next__())

We can also create a one liner for generators too by following the syntax below.

gener = (i for i in range(n))
a = gener(5)
print(a.__next__())
'''