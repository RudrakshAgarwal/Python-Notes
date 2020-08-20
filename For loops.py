list1 = [["Rudraksh",5],["Soham",4],["Rishi",7],["Rahul",8],["Lekhraj",9 ]]
for item,lollipop in list1:
    print(item,"and lollipop is",lollipop)

dict1=dict(list1)
print(dict1)
for item,lollipop in dict1.items(): #dict.item() by this we can print items in the dictionary
    print(item,"and lollipop is",lollipop)

for item in dict1: #This will print all the keys in the dictionary.
    print(item)


#Quiz:
list2 = [int,float,"Rudraksh",2,8,7,4,10,14,18,20,6]
for item in list2:
    if str(item).isnumeric() and item>=6:
        print(item)


'''
Like all the other functions we have seen so far in the video tutorials, for loop is also just a programming function 
that iterates a statement or a number of statements based on specific boundaries under certain defined conditions, 
that are the basis of the loop.

Note that the statement that the loop iterates must be present inside the body of the loop.

Regarding loops, iteration means to go through some chunk of code again and again. In programing it has the same meaning, 
the only difference is that the iteration depends upon certain conditions and upon its fulfilment the iteration stops, 
and the compiler moves forward.

For a beginner or layman, the concept of loop could be easily understood using an example of songs playlist. 
When we like a song, we set it on repeat and then it automatically starts playing again and again. 
Same concept is used in programming, we set a part of code for looping and the same part of the code executes until the 
certain condition that we provided it is fulfilled. 
You must be thinking that in song playlist the song keeps on playing until we stop it, 
same scenario can be made in case of loops by we put a certain condition that the loop could not fulfill, 
then it will continue to iterate endlessly until stopped by force.

An example of where loop could be helpful to us could be in areas where a lot of data has to be printed on the screen and 
physically writing that many printing statements could be difficult or in some cases impossible. 
Loops are also helpful in searching data from lists, dictionary and tuple.

Why do we use loops?

Complex problems can be simplified using loops
Less amount of code required for our program
Lesser code so lesser chance or error
Saves a lot of time
Can write code that is practically impossible to be written
Programs that requires too many iterations such as searching and sorting algorithms can be simplified using loops.

How to write a for loop?

For loop basically depends upon the elements it has to iterate instead of the statement being true or false. 
The later one is for the While loop which is topic for the next tutorial i.e. tutorial# 17. 
In different programming languages the way to write a loop is different, in java and C it could be a little technical and 
difficult to grasp for a beginner but in Python, its simple and easy. We just have to declare a variable so we can print 
the output through it during different iterations and just have to use the keyword “for” and “in”, more explanation could 
be easily obtained about working and syntax through the video tutorial.

Advantages of loops:

The reusability of code is ensured
We do not have to repeat the code again and again, just have to write it one time
We can transverse through data structures like list, dictionary and tuple
We apply most of the finding algorithms through loops
'''