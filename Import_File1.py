import sys
print(sys.path)

from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())

import Import_File2
print(Import_File2.a)
Import_File2.printjoke("This is Me.")


''' 
How Import Works In Python?
In this tutorial we aim to understand the working of the import statement, so we can have a better grasp of the 
concept and resolve common importing issues. In Python, we give access to a module by using a keyword import. To use 
any package in our code, we must make it accessible by importing it first. There are many ways we can import a module 
in python, but what can be easier than using a single keyword, so it is also the most common way for importing. 

How does the import keyword work?
When we write a certain module name along with the import keyword, it will start searching for a file with that name 
having an extension .py. After finding the file, it will import it into our program, which means that it will permit 
our program to use the functions of the certain module we imported. We can import a module named “sys” to see the 
path that our import statement takes while searching for a module. 

import sys
print( sys.path)

sys.path prints out a list of directories. When we tell Python to import something, then it looks in each of the 
listed locations in order. 

A common mistake that most of the beginners make and is also the primary reason for making this tutorial is, 
why can’t we name our file, the same as the name of a module. The reason is associated with the path. When we give 
our file a name same as the name of a module, then instead of importing the original module, the system will import 
our created file because it starts its search for the file from the directory where the file we are working on 
exists. So, we will not be able to use the functions of the original file. 


There are two methods to use functions or variables after importing:
1) The first one is to import using an object. For this, we usually import the whole module by using a simple import 
statement. When we use only the import keyword, we will import the resource directly, like this: 
    import sklearn
    
2) When we use the second syntax, we will import the resource from another package or module. Here is an example:
    from flask import Flask
    
3) We can also choose to rename an imported resource, like this:
    import pandas as pd

This renames the imported resource pandas to pd. 

We can not access it using pandas keyword; instead, we have to use pd or the compiler will show an error. This case 
comes in handy when the module name is difficult or lengthy, and we have to use a module again and again to call its 
functions. 

Note: import module as module_name does not rename the module originally but only for a specific program where it is 
imported using this sort of keyword. 

Disadvantages: One of the major disadvantages of the flexibility provided by a python in the case of modules is that 
they can be easily modified and overridden. Along with disrupting the functionality of the program, it also poses a 
major security risk. 
'''
