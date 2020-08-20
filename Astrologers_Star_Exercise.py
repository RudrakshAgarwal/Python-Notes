print("Enter the no. of rows.")
row = int(input())
print("1 or 0")
bool = bool(int(input()))
if bool==True:
    for i in range(0,row+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif bool==False:
    for i in range(row,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()


#Another method
print("Enter the no. of rows.")
num = int(input())
print("1 or 0")
bool = input("1 for True Value and 0 for False Value.")
if bool == "1":
    for i in range(0,num+1):
        print("*"*i)
if bool == "0":
    for i in range(num,0,-1):
        print("*"*i)

