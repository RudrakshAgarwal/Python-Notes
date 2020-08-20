'''
Problem Statement:
The task you have to perform is” Oh Soldier Prettify my Folder.”

Suppose you have a folder, and its path is also given. You have to create a function which takes three input arguments,
which are:

def soldier("C://", "requirement.txt", "jpg")
    1) Full Path of the folder as input strings.
    2) Dictionary file
    3) File Format

The function will perform three tasks:
    1) First, it will check all the files present in the folder whose paths are given as an input argument.
    2) Then it will capitalize the first letter of each file. If the name of the file is present in a dictionary file
    then it will not capitalize the first letter. It will only capitalize the first letter of the files, which are not
    present in the dictionary file.
    3) The function renames the file names to number in range of 1 to100 whose format is the same as mentioned in the
    input parameter like 1.jpg.


After performing these tasks, your folder will prettify as all the first letters of the files in the folder will be
capitalize except for those files whose names are present in the dictionary file. And the files having the same format
as given in the input argument will rename to number in the range of 1-100.
'''


# Oh soldier Prettify my Folder

# path, dictionary file, format

# def soldier("C://", "harry.txt", "jpg")

import os
def soldier(path, file, format):
    os.chdir(path)
    i = 1 #Here we initialize 1 becoz we want to start numbering the files or folder from 1.
    files = os.listdir(path) #If we want to output the names of all the files at a certain location, we can use this function.
    with open(file) as f:
        filelist = f.read().split("\n")
#Mene .plit() fun isiliye use kiya hai becoz jo requirement.txt file hai jo mene banayi hai me usme change nahi krna
#chahata hu woh mujhe mill jayegi as a list.

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i +=1
#splitext() ye deta hai extention hamari file ki, or ye kya karta hai ki file or extention ko alag kr deta hai, or 1
#isiliye liya hai ki vo tuple return krta hai or jo tuple ka phele wala hota hai vo hota hai hamari extention.

soldier(r"D:\Personal Files\College Diaries",
        r"D:\Study Material\Python Notes\requirement.txt", ".jpg")

#.jpg vo extention hai jisme me 1 se lekar numbering krna chahata hu