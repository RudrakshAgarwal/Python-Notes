f = open("Rudra.txt", "rt") #f is a pointer & default is rt & binary is rb.
#content = f.read(3)
print(f.readlines()) #This will print the List and list will contain lines.
print(f.readline())

# print(content)
# for line in content: - This will print file character by character.
#     print(line)
# for line in f:
#     print(line,end="") - This will print the statement line by line.
# content = f.read(34484)
# print("1",content)
#       
# content = f.read(344)
# print(content)
#
# content = f.read(34484)
# print("2",content)
f.close()


'''
Open(), Read() & Readline() For Reading File: 
As we now have an idea of what files(text or binary) are and their 
access modes, we are now ready to dive into the discussion of file handling methods. When we want to read or write a 
file (say on our hard drive), we must first open the file. When we open a file, we are asking the operating system to 
find the file by name, making sure the file exists. 

How to open a file?
Python has a built-in open() function to open a file.

The syntax of the function is:
open("filename" ,"mode")

To open a file, we must specify two things,

    1) Name of the file and its extension 
    2) Access mode where we can specify in which mode file has to be opened, 
    it could either be read (r), write (w) or append(a), etc. For more information regarding access modes, 
    refer to the previous tutorial. 

For Example, 
open("myfile.txt")

The file “myfile.txt” will open in "rt" mode as it is the default mode. But the best practice is to follow the syntax to
avoid errors.

The open function returns a file object. We store this file object into a variable which is generally called as a 
file pointer/file handler. Here is a code snippet to open the file using file handing in Python, 

f=open("myfile.txt," "w")

You can use this file pointer to further add modifications in the file. An error could also be raised if the 
operation fails while opening the file. It could be due to various reasons like trying to access a file that is 
already closed or trying to read a file open in write mode. 


How to read a file? 
To read a file in Python, there are various methods available:
    1) We can read a whole file line 
    by line using a for loop in combination with an iterator. This will be a fast and efficient way of reading data. 
    2) When opening a file for reading, Python needs to know exactly how the file should be opened. Two access modes are 
    available reading (r), and reading in binary mode (rb). They have to be specified when opening a file with the 
    built-in open() method. 

f = open("myfile.txt", "r")

    3)The read() method reads the whole file by default. We can also use the read(size) method where you can specify how 
    many characters you want to return i.e. 

f.read(2); #Here, you will get the first two characters of the file.

    4) You can use the readline() method to read individual lines of a file. By calling readline() a second time, 
    you will get the next line.
    5) readlines() method reads until the end of the file and returns a list of lines of the 
    entire file. It does not read more than one line. 
    
f=open("myfile.txt","r");
f.readlines() #Returns a list object
    

Note: The default mode to read data is text mode. If you want to read data in binary format, use ''rb".

Is it necessary to close a file?
The answer is yes, it is always the best practice to close a file after you are done performing operations on it. 
However, Python runs a garbage collector to clean up the unused objects, but as good programmers, we must not rely on 
it to close the file. Python has a build-in close() function to close a file i.e; 
f.close()
    
'''