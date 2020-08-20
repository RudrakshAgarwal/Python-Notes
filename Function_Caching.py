import time
from functools import lru_cache

@lru_cache(maxsize=32)
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(2)
    print("Done... Calling again")
    input()
    some_work(3)
    print("Called again")



''' 
In today's tutorial, we are going to learn about function caching. If you have some background related to computer science, you must have 
came across this term in relation to the operating system. Or you may have seen the caching term in your browser history settings. Before 
discussing function caching, we must know what caching is.

What is the term caching means?
Caching means to store the data in a place from where it can be served faster. In case of data that has been frequently used, the computer 
assigns a cache memory, so it does not have to load it again and again from the main memory. The purpose of the cache is to make the tasks 
more efficient and quicker. The same is true for web browsers, the pages we load again and again are stored in the cache for faster retrieval. 
In Python, however, we have to do it all manually, as the program will not store anything in the cache itself.

How to use function caching in Python?
Function caching is a way to improve the performance of code by storing the return values of the function. Before the 3.2 updates of 
Python, we had to create a cache ourselves by storing the value in a variable or by other such means. But in Python 3.2, there is a new 
update in the functools module of Python. To use this module, we have to import it first.

Ex-
import functools

We have been facilitated with the help of a decorator known as lru_cache. Decorators are an essential part of Python. Decorators in Python 
can be used for a variety of different purposes.

If you are not familiar with the concept of a decorator.

We have to pass maxsize as parameter with the decorator. maxsize is defined to tell the program how many values we want to store in the 
cache. It automatically stores the values for the latest number of calls. 

For example
@functools.lru_cache(maxsize=4)
def myfunc(x):
    time.sleep(2)
    return x

myfunc(1) 
# myfunc(1) takes 2 seconds and results for myfunc(1) are now cached
myfunc(1)
myfunc(2)
myfunc(3)
myfunc(4)
myfunc(5)

We set the maxsize equal to 4, and the program uses the same call five times, then the program will only be able to retrieve the data faster 
for the last five calls because caching is only storing data for them. It is important to define the maxsize as per our requirements 
because it takes up memory accordingly, so for a better program, it should be precisely according to our needs. 

We are using the time module as an example in this tutorial to understand the working of function caching better. We are using its function 
known as time.sleep(), which delays the execution of further commands for given specific seconds of time. The number of seconds is sent as a 
parameter within parenthesis. If you are not familiar with Python's time module, visit the tutorial #42 i.e., Time Module In Python, for a 
better understanding.
'''