# n! = n * n-1 * n-2 * n-3.....1
# n! = n * (n-1)!
def factorial_iterative(n):
    """
        :param n:
        :return:
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
"""
Working:
# 5 * factorial_recursive(4)
    # 5 * 4 * factorial_recursive(3)
    # 5 * 4 * 3 * factorial_recursive(2)
    # 5 * 4 * 3 * 2 * factorial_recursive(1)
    # 5 * 4 * 3 * 2 * 1 = 120
"""
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
num =  int(input("Enter the number."))
print("Factorial Using iterative method",factorial_iterative(num))
print("Factorial Using recurisve method",factorial_recursive(num))
print("Fibonacci Using recurisve method",fibonacci(num))


''' 
Recursions: Recursive Vs Iterative Approach:

"Recursion occurs when a function calls itself."

Mostly both recursion and iteration are used in association with loops, but both are very different from each other. 
In both recursion and iteration, the goal is to execute a statement again and again until a specific condition is 
fulfilled. An iterative loop ends when it has reached the end of its sequence; for example, if we are moving through 
a list, then the loop will stop executing when it reached the end of the list. But in the case of recursion, 
the function stops terminating when a base condition is satisfied. Let us understand both of them in detail. 

Recursion: 
    There are two essential and significant parts of a recursive function. The first one is the base case, 
and the second one is the recursive case. In the base case, a conditional statement is written, which the program 
executes at the end, just before returning values to the users. In the recursive case, the formula or logic the 
function is based upon is written. A recursive function terminates to get closer to its base case or base condition. 
As in case of loops, if the condition does not satisfy the loop could run endlessly, the same is in recursion that if 
the base case is not met in the call, the function will repeatedly run, causing the system to crash. 

In case of recursion, each recursive call is stored into a stack until it reaches the base condition, then the stack 
will one by one return the calls printing a series or sequence of numbers onto the screen. It is worth noting that 
stack is a LIFO data structure i.e., last in first out. This means that the call that is sent into the stack at the 
end will be executed first, and the first one that was inserted into the stack will be executed at last.

Iteration:
    We have a basic idea about iteration as we have already discussed, relating loops. 
Iteration runs a block of code again and again, depending on a user-defined condition. Many of the functions that 
recursion performs can also be achieved by using iterations but not all, and vice versa. 

Recursion vs. Iteration:
    1) Recursion can only be applied to a function, while iteration can be used for any number of lines of code, we want
    to repeat.
    2) Lesser coding has to be done in case of recursion than iteration.
    3) Back tracing or reverse engineering in case or recursion can be difficult.
    4) In the case of recursion, if the condition is not met, the system will repeat a few times and then crash while in
    case of iteration it will continue to run endlessly.
    5) Even though less coding has to be written in case of recursion, it is still slower in execution because the function has
    to be called, again, and again, storing data into the stack also increases the time of execution.
    
In my opinion for smaller programs where there are lessor lines of codes, we should use a recursive approach and in 
complex programs, we should go with iteration to reduce the risk of bugs. 

'''