f = open("Rudra.txt")
print(f.tell()) #the tell() function. f.tell() returns an integer giving the file pointer current position in the file represented as a number of bytes.
print(f.readline())
print(f.tell())
f.seek(10) # seek() function returns the current position of the file pointer within the file.
print(f.readline())
print(f.tell())
f.close()


'''
Seek(), tell() & More On Python Files: 
Python file objects give us many methods and attribute that we can use to 
analyze a file, including tools to figure out the name of the file associated with the file object, whether it is 
closed or opened, writable, readable and how it handles errors. 

We have already discussed the file, its access modes, how to open, close, read, and write files.

we are going to study why there is a need for tell() and seek() functions and how we can use them? 
tell():
    When we are working with python files, there are several ways to present the output of a program, it could be in human-
    readable form or binary form, or we use read() function with specified sie to read some data.
    

What if we want to know the position of the file(read/write) pointer:
For this purpose, we use the tell() function. f.tell() returns an integer giving the file pointer current position in 
the file represented as a number of bytes. File Pointer/File Handler is like a cursor, which defines from where the data 
has to be read or written in the file. Sometimes it becomes important for us to know the position of the File Pointer. 
With the help of tell(), this task can be performed easily 


Description:
    Syntax:  seek()
    Parameters Required: No parameters are required.
    Return Value:  seek() function returns the current position of the file pointer within the file.
    
Example:
     f = open("myfile.txt", "r")
    print(f.readline() )
    print(f.tell())
    
Here the question arises, what if we want to change the position of the file pointer.

Here the concept of seek() function comes.
seek():
    When we open a file, the system points to the beginning of the file. Any read or write will happen from the 
    start. To change the file object’s position, use seek(offset, whence) function. The position will compute by 
    adding offset to a reference point, and the whence argument selects the reference point. It is useful when 
    operating over an open file. If we want to read the file but skip the first 5 bytes, open the file, use function 
    seek(5) to move to where you want to start reading, and then continue reading the file. 
    
Description:
    Syntax:  file_pointer .seek(offset, whence).
    Offset:   In seek() function, offset is required. Offset is the position of the read/write pointer within the file.
    Whence: This is optional. It defines the point of reference. The default is 0, which means absolute file positioning.

Value & Meaning:
    1) 0: Absolute file positioning. The position is relative to the start of the file. The first argument cannot be negative.
    2) 1: Seek relative to the current position. The first argument can be negative to move backward or positive to move forward
    3) 2: Seek relative to the file’s end. The first argument must be negative.

Example:
This code will change the current file position to 5, and print the rest of the line.
    f = open("myfile.txt", "r")
    f.seek(5)
    print( f.readline() )
    
Note: not all file objects are seekable.
'''