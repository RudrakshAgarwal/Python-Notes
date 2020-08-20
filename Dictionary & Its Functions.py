#Dictionary is nothing but a key value pairs.
d1 = {} #Black dictionary
#print(type(d1))

d2 = {"Rudra":"Sandwish", "Soham":"Maggie","Rishi":"Burger","Aayush":{"B":"Pizza","L":"Roti","D":"Dahi"}}
print(d2["Aayush"]["B"])
d2 ["Ankit"] = "Junk Food" #By this we can add new key value pairs in dictionary.
d2 [420] = "Kebabs"
print(d2)
del d2[420] #By this we can delete the key value pairs in dictionary.
print(d2)
d3 = d2.copy() #This func will copy the string to the variable d3, so we can apply changes in d3 without any change in actual dictionary.
del d3["Rudra"]
print(d3)
print(d2)
d2.update({"Leena":"Toffee"}) #By this also we can update value in a dictionary.
print(d2)
print(d2.keys()) #This fun will return the keys of the dictionary.
print(d2.items()) #This fun return the key, value items.

'''
Theory:

“Python dictionary is an unordered collection of items. Each item of the dictionary has a key/value pair.”

Every programming language has its own distinct features, commonly known as its key features. 
That said, Python’s one out of box feature is “dictionaries”. Dictionaries may look very similar to a “List”, 
but dictionaries have some distinct key features that a list do not hold, and those features are what makes it special. 

Moving on to the features:

It is unordered (no sequence is required - data or entries have no order)
It is mutable (values can be changed even after its formation or new data/information can be added to the already existing dictionary, 
we can also pop/remove an entry completely)

 
It is indexed (Dictionary cointains key-value pairs and indexing is done with keys. 
Also after the 3.7th update the compiler stores the entries in the order they are created)

 
No duplication of data (each key is unique; no two keys can have the same name so there is no chance for a data override)
If we talk little about how it works, its syntax comprises of key and values separated by colons in between curly brackets, 
where the key is used as a keyword, as we see in real life dictionaries, and the values are like the explanation of the key, 
or what the key holds. And for the successful retrieval of the data, we must know the key, so we can access its value. 
Like in the regular oxford dictionary, if we do not know the word or its spelling, we cannot obtain its definition. 

With the help of dictionaries, we do not have to do most of our work manually through code like in C or C#. 
Python along with dictionary provides us with a long list of already defined methods that can help us do our work in a shorter span of time with only a little bit of code. 
Some of these methods include, clear(), copy(), popitem(), etc.
No extra effort must be put in order to learn these methods functionality as their names explain their functions (in most of the cases), such as clear() will clear all the data from the dictionary, making it empty, copy() will make a copy, etc.

Some distinct features that a dictionary provides are:

We can store heterogeneous data into our dictionary i.e. numbers, strings, tuples, and other objects.
Different data types can be used in a single list.

'''

