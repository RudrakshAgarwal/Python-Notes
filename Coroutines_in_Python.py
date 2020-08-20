def searcher(): #Coroutine
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on Rudraksh and code with Rudraksh and good"
    time.sleep(4) # Just imagine this time is for reading the file, or book or to read the machine learning module.

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")


search = searcher()
print("search started") # First this statement will execute.
next(search)
print("Next method run") # When this statement is execute it will take delay of 4 seconds for the first time,
# and for the rest of the time it will directly go to while loop and run fastly.
search.send("Rudraksh")

search.close()
search.send("Rudraksh")
# input("press any key")
# search.send("harry and")
# input("press any key")
# search.send("thi si")
# input("press any key")
# search.send("joker")
# input("press any key")
# search.send("like this video")


'''
Our today's topic for this course is Coroutines. Before learning the concept of coroutines, we must have some 
brief knowledge or understanding related to generators. A generator is a function that produces a sequence of results 
instead of returning a value. You generate a series of values (using the yield statement). 

Both generator and coroutine operate over the data; the main differences are: 

     1) Generators produce data
     2) Coroutines consume data


Coroutines are mostly used in cases of time-consuming programs, such as tasks related to machine learning or deep 
learning algorithms or in cases where the program has to read a file containing a large number of data. In such 
situations, we do not want the program to read the file or data, again and again, so we use coroutines to make the 
program more efficient and faster. Coroutines run endlessly in a program because they use a while loop with a true or 
1 condition so it may run until infinite time. Even after yielding the value to the caller, it still awaits further 
instruction or calls. We have to stop the execution of coroutine by calling coroutine.close() function. It is very 
crucial to close a coroutine because its continuous running can take up memory space related to function caching. We 
can define a coroutine using the following statements. 

def myfunc():
    while True:
        value = (yield)

The while block continues the execution of the coroutine for as long as it receives values. The value is collected 
through the yield statement. 


Coroutine Execution:- 
Execution is the same as of a generator. When you call a coroutine, nothing happens. They only 
run in response to the next() and send() methods. Coroutine requires the use of the next statement first so it may 
start its execution. Without a next() it will not start executing. We can search a coroutine by sending it the 
keywords as input using object name along with send(). The keywords to be searched are send inside the parenthesis. 

When we run the next() function the first time, the coroutine executes and waits for new input. After the input is 
sent to it using the send() function, it executes it and again waits for next input, and the process goes on like 
this because we have set the while loop as true, so it will never exit its execution. In order to make the execution 
stop, we have to close the coroutine using coroutine.close() function. 

    1) send() — used to send data to coroutine
    2) close() — to close the coroutine

Example:
def myfunc():
    print("Code With Harry")
    while True:
        value = (yield)
        print(value)

coroutine =myfunc()
next(coroutine)
coroutine.send("Python")
coroutine.send(" Tutorial ")
coroutine.close()

Output:-
Code With Harry
Python 
Tutorial
 
After closing coroutine, if we send values, it will raise StopIteration exception. Coroutines are used for data 
processing mechanisms. Coroutines are similar to generators, except they wait for information to be sent to it using 
send() function. 
'''
