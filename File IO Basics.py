# IO Basics
"""
"r" - Open file for reading - default
"w" - Open fie for Writing
"x" - Create file if not exists
"t" - text mode
"b" - Binary mode
"+" - read and write
"""


'''
Python File IO Basics: 
In this tutorial we are not getting into files in detail, instead, we are discussing the 
basics of the file and its modes in a theoretical manner. In computer terms, “a file is a resource for saving data 
and information in computer hardware”. A file is stored in the form of bytes in hardware. A file is opened in the 
RAM, but it is stored in the hardware because the hardware is non-volatile i.e. it stores its data permanently. On 
the other hand, RAM is volatile, it loses its data when the system is shut down. 

Unlike C or C++, file handling in python is relatively easy and simple.  Python treats files differently as text or 
binary and this is important. There are two types of files that we normally encounter in our computer daily. The 
first one is a text file and the second one is a binary file. We can understand by the name of the text file that it 
must contain text in it. The extension for the text file is .txt. All other forms of files are mostly binary even a 
.doc file, that we open in Microsoft Word is a binary file because it requires special software for accessing it. 

The second sort of files are binary files. They are almost all the other files that we come in contact with while 
using our computer. These files include images, PDFs, Excel files, etc. 

Modes of opening file in Python: 
There are many modes of opening a file in Python, unlike other languages Python has 
provided its users a variety of options. We will discuss seven of them in this tutorial. 

    1) r : r mode opens a file for read-only. We do not have permission to update or change any data in this mode.
    2) w : w mode does not concern itself with what is present in the file. It just opens a file for writing and if there is 
    already some data present in the file, it overwrites it.
    3) x : x is used to create a new file. It does not work for an already existing file, as in such cases the operation fails.
    4) a : a stands for append, which means to add something to the end of the file. It does exactly the same. It just adds the
    data we like in write(w) mode but instead of overwriting it just adds it to the end of the file. It also does not have 
    the permission of reading the file.
    5) t : t mode is used to open our file in text mode and only proper text files can be opened by it. It deals with the file 
    data as a string.
    6) b : b stands for binary and this mode can only open the binary files, that are read in bytes. The binary files include 
    images, documents, or all other files that require specific software to be read.
    7) + : In plus mode, we can read and write a file simultaneously. The mode is mostly used in cases where we want to update
    our file.
'''