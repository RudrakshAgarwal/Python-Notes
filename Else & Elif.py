var1 = 6
var2 = 56
var3 = int(input())
if(var3>var2):
    print("Greater")
elif var3==var2:
    print("Equal")
else:
    print("Lesser")
list1 = [5,7,8,9,10]
print(5 in list1) #This will return true or false.
print(15 not in list1)
if 5 in list1:
    print("Yes it's in the list")

#Quiz:
Legal_age =18
print("Enter your age.")
age = int(input())
if(Legal_age<age):
    print("Yess your are eligible for driving.")
elif Legal_age==age:
    print("Yess you are 18, Just come physically then we will decide you are eligible for driving or not.")
else:
     print("No you are not eligible for driving.")


''' 
If Else & Elif Conditionals In Python:
“If, else and elif statement can be defined as a multiway decision taken by our program due to the certain conditions in
our code.”

For few viewers, the term “elif” is new as they are not familiar with the word and it is also not like most of the 
other words such as list or loops, etc. that have the same meaning in the English language and in Python programming. 
In fact, in English “elif” means honest. But if you have ever done programming in any language, you must be familiar 
with “else-if” statement, well “elif” is just that. 

Now coming towards a more formal sort of description. “If and else” are known as decision-making statements for our 
program. They are very similar to the decision making we apply in our everyday life that depends on certain 
conditions. The everyday example is thoroughly explained in the tutorial so I will not waste your time on that, 
instead, I would now like to focus on more technical details. 

Let us focus a little on the working:

Our compiler will execute the if statement to check whether it is true or false now if it’s true the compiler will 
execute the code in the “if” section of the program and skip the bunch of code written in “elif” and “else”. But if 
the “if” condition is false then the compiler will move towards the elif section and keep on running the code until 
it finds a true statement(there could be multiple elif statements). If this does not happen then it will execute the 
code written in the “else” part of the program. 


An “if” statement is a must because without an if we cannot apply “else” or “else-if” statement. On the other hand 
else or else if statement are not necessary because if we have to check between only two conditions we use only “if 
and else” and even though if we require code to run only when the statement returns true and do nothing if it returns 
false then an else statement is not required at all. 

Now Let’s talk about some technical issues related to the working of decision statements:
    1) There is no limit to the number of conditions that we could use in our program. We can apply as many elif 
    statements as we want but we can only use one “else” and one “if” statement.
    2) We can use nested if statements i.e. if statement within an if statement. It is quite helpful in many cases.
    3) Decision statements can be written using logical conditions which are:
    4) Equal to
    5) Not equal to
    6) Less than
    7) Greater than
    8) Greater than equal to
    9) Less than equal to
We can also use Boolean or our custom-made conditions too.
'''