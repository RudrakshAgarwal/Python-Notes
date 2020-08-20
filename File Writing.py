f = open("Rudra2.txt", "a") # "w" is for write and "a" is for append
a = f.write("Mein ek bhut hi smart or handsome ladka hu \n")
print(a) #This will print no. of characters which has written in the file.
f.close()

#Handle Read and Write both

file = open("Rudra2.txt", "r+") #"r+" this means read and write both
print(file.read())
file.write("Thank You.")
file.close()


''' 
Writing And Appending To A File:
We have already discussed how to open and read a file in Python, Now we will discuss how to write or insert text to a 
file and also how we can simultaneously read and write a file. Now, as we know, there are different modes of opening a 
file.

Note: f is an object for the file. It is not a method or a special character. You will notice me using f.write() or 
f.read() or f.close(), in further description or tutorial, but you can use character or word of your own choice 
instead. 

    1) “w” mode: Here “w” stands for write. After opening or creating a file, a function, f.write() is used to insert text 
    into the file. The text is written inside closed parenthesis surrounded by double quotations. There is a certain 
    limitation to the write mode of the opening file that it overrides the existing data into the file. For a newly 
    created file, it does no harm, but in case of already existing files, the previous data is lost as f.write() 
    overrides it. 

    2) “a” mode: “a” symbolizes append mode here. In English, appends mean adding something at the end of an already 
    written document, and the same is the function the mode performs here. Unlike write mode, when we use "a" 
    keyword, it adds more content at the end of the existing content. The same function i.e., f.write() is used to 
    add text to the file in append mode. It is worth noting that append mode will also create a new file if the file 
    with the same name does not exist and can also be used to write in an empty file. 
    
    3) “r+” mode: At the beginning of the description, I told you that we would learn reading and writing a file 
    simultaneously. Well, r+ mode is more of a combination of reading and append than read and write. By opening a 
    file in this mode, we can print the existing content on to the screen by printing f.read() function and adding or 
    appending text to it using f.write() function. 

A very helpful tip for beginners: 
If you are writing in append mode, start your text by putting a blank space or 
newline character (\n) else the compiler will start the line from the last word or full stop without any blank space 
because the curser in case of append mode is placed right after the last character. So, it is always considered a 
good practice to adopt certain habits that could help you in the future, even though they are not much helpful now. 

f.close(): 
f.close() is used to close a file when we are done with it. It is a good practice to close a file after 
use because whichever mode you opened it for, the file will be locked in for that specific purpose and could not be 
accessed outside the program, even though the file browser. 
'''
