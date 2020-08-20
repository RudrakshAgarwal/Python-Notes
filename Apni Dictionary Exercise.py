# Problem:
# Using a Python dictionary, write a program capable of taking dictionary words as input from the user. Your
# program should be able to return the meaning of the word from the dictionary



print("Your Keys are Name, Age, Mobile no, City, Postal code")
print("Select two Keys.")
Key1 = input()
Key2 = input()
dic1 = {"Name":"Rudraksh Agarwal","Age":"21","Mobile no":"48654926448","City":"Indore","Postal code0":"445645"}
print("You Entered",Key1,"and",Key2)
print(dic1[Key1])
print(dic1[Key2])

