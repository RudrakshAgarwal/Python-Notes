i=0
while(True):
    if i+1<5:
        i=i+1
        continue
    print(i+1, end=" ")
    if(i==44):
        break #Stop the loop
    i=i+1
    print("\n")


#Table:
n=2
while(1):
    i=1
    while i<=10:
        print("%d X %d = %d\n"%(n,i,n*i))
        i=i+1
    choice=int(input("Do you want to continue printing the table, press 0 for no?"))
    if choice==0:
        break
    n=n+1


''' 
Break & Continue Statements:
“Break and continue statements are used to alter the flow or normal working of a loop, that could be either a “for loop”
or “while loop”.

You all know what break and continue means in basic English language. Break means interrupt and continue means 
resuming after an interrupt. As the meanings of the words can describe that both these functions are totally opposite 
to each other. Hence, both of these keywords are mostly defined together, like “if and else” or “try and except”, 
but unlike the others, their functionality is quite opposite to each other. They aren’t even used together in most of 
the cases like “except” couldn’t be used if there is no “try” or “else” couldn’t be if there isn’t an “if” statement 
present, but in cases of “break and continue”, they both do not have any such relation. They may be defined together 
but not mostly used together. 

Defining break statement, break statement alters the normal functionality of the loops by terminating or exiting the 
loop containing it. The compiler then moves on to the code that is placed after the body of the loop. The syntax of 
break is only a single word i.e. “break”. Break statement is rather easy and simple to understand than a continue 
statement as it just leaves the bunch of code written after it inside the loop and the control of the program is then 
shifted to the statement written after the loop. 

    Continue statement also alters the flow of a normal working loop but unlike the break statement, it takes the 
compiler to the start of the code that has already been executed before the statement but is inside the loop 
boundary. All the code written after the continue statement is skipped but it is worth noting that the continue 
statement works only for a single iteration. Unless in situations where it's written with decision statements such as 
if, else, etc., in those situations the continue statement will totally be dependent upon the condition of the 
decision statement. Its syntax is also plain and easy like a break statement as you only have to use the keyword 
“continue”. 

Where and when can these statements come in handy:

    When you are working with a big project, there might occur a situation where you only need to use the loop partially 
without adding new or removing already existing lines of codes. You can easily apply the break statement in your code 
so that you can partially run it without any sort of error. 

Or in another situation lets suppose you are working with while loop printing some lines on the screen and you want 
to skip an iteration in between others, then you can write the continue statement using an “if” statement that 
matches your need so that you can skip the specific iteration. '''
