import pickle

# Pickling a python object
# cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
# file = "MyCar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

file = "MyCar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))

'''Pickle Module: 
In this tutorial, we are going to learn about the pickle module in python. Pickle means to 
preserve, and in Python, we use it for the same purpose. Pickle comes handy while saving complicated data. They are 
easy to use, lighter, and does not require several lines of code. The pickled file generated is not easily readable 
and thus provide some level of security. We will divide this tutorial into two parts i.e. 

    1) Pickling
    2) Unpickling

First, we will learn about the basics of Pickling and how to achieve it.

What is pickling? 
Pickling is a process of serializing an object. Serializing means to store the object in the form 
of binary representation so it can be saved in our main memory. The object could be of any type. It could be a 
string, tuple, or any other sort of object that Python supports. The data is stored in the main memory in a file. 
While writing the code for pickling, we open the file in "wb" mode, also known as writing binary mode. So, 
to use the pickle module, we have to make a file with .pkl extension and send it in a dump() function along with the 
object. dump() is a built-in function in the Pickle module, made for pickling. 

Pickling files:-
To use pickle, we have to import it in Python.

Ex-
import pickle

In this example, we will pickle a dictionary. We will save it to a file and then load again.

py_dict = { 'name': 'Rudraksh', 'salary':9000, 'language': 'Hindi' }
myfile = open('filename','wb')
pickle.dump(py_dict,myfile)
myfile.close()


What is unpickling? 
The file format is binary, so we cannot directly open and read it; instead, we have to open it 
using a python program, and the process is known as unpickling. For unpickling, we have to open the file in "rb" 
mode, also known as a read binary mode. The function we use this time is also a built-in function, named load(). 
Unlike dump(), we have to send the file name as a parameter, and it automatically retrieves the data in the object 
type it was inserted in. For example, if we send a list while pickling, the return result will also be a list. 

myfile = open(filename,'rb')
py_dict = pickle.load(myfile)
myfile.close()
    
To make sure that you successfully unpickled it, you can print the dictionary, compare it to the previous dictionary 
and check its type with type().d") 

We can face some of the common pickle exceptions raised while dealing with pickle module.

    1) Pickle.PicklingError: If the pickle object does not support pickling, then Pickle.PicklingError exception is raised.
    2) Pickle.UnpicklingError: This exception will raise if the file contains bad or corrupted data.
    3) EOF Error: This exception will raise if the end of the file is detected.
    
Disadvantages:
    1) There are some situations in which pickling is discouraged. For example, when we are working with multiple 
    programming languages, pickle is discouraged.
    2) Pickle has been found slower than its alternatives.
    3) In some cases, it has also shown a few security vulnerabilities.
    4) When we update our program to a newer version, pickled data through the previous version can cause issues.
'''
