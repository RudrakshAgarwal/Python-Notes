import os
# print(dir(os))
# print(os.getcwd())
# os.chdir("C://")
# print(os.getcwd())
# f = open("Rudra.txt")
# print(os.listdir("C://"))
# os.makedirs("This/that")
# os.rename("Rudra.txt", "Rudraksh Agarwal.txt")
# print(os.environ.get('Path'))
# print(os.path.join("C:/", "/Rudra.txt"))

# print(os.path.exists("C://Program Files2"))
print(os.path.isfile("C://Program Files"))


'''What is OS Module? 
OS module provides our code with a direct connection to the operating system. We can use its 
different functions to interact and do activities on our operating system. For example, if we want to create such 
software that needs to store or access files from a directory or folder, we can use the OS module to perform the task 
for us. To use OS Module in Python, we have to import it. 

Ex- import os 


Build-in Function in OS Module:- 
OS modules have a lot of built-in functions. You can see the list of 
built-in functions we can run through it by running the following code, also known as object introspection: 

1) print(dir(os)): It gives us a list of all the functions the OS module is composed of. 
2) os.getcwd( ): Here cwd is a short form for the current working directory. The function returns us the path of the 
directory we are currently in. 
It is important to know about our directory because when we are trying to import a file in python, the compiler 
searches for it in our current directory. 
3) os.chdir( ): it is used in case we want to change our directory. The new path is sent inside the parenthesis. If we 
want to access some files or folder from some other directory, we can use it.
4) os.listdir( ): If we want to output the names of all the directories at a certain location, we can use this function.
5) os.mkdir( ): To create a new directory or folder. The name is sent as a parameter inside the parenthesis.
6) os.makedirs( ): To make more than on directory simultaneously.
7) os.rename( ): To rename an already existing directory, we use this. We send the current name and new name of our 
directory as parameters
8) os.rmdir( ): It deletes an empty directory.
9) os.removedirs( ): We can remove all directories within a directory by using removedirs(). 
10) os.environ.get( ): It will return us the environment variable. The environment variable must be set, or the function
will return null.
11) os.path.join( ): It joins one or more path components. We can join the paths by simply using a + sign, but the 
benefit of using this function is that we do not have to worry about extra slashes between the components. So less 
accuracy still provides us with the same result.
12) os.path.exists( ): It returns us a Boolean value i.e., either true or false. It is used to check whether a path 
exists or not. If it does, then the output will be true, otherwise false.
13) os.path.isfile( ): It returns true if the path is an existing regular file.
14) os.path.isdir( ): It returns true if the path is an existingdirectory.
'''