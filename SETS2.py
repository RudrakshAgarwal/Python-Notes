# s1 = {1, 2, 3, 4, 5}
# print(s1)

# s1 = {} #Empty Dictionary
# print(s1)
#
# s2 = set() #Empty Set
# print(s2)

# s1 ={1,2,3,4,5,1,2,3}
# print(s1)

# s1 = {1, 2, 3, 4, 5}
# s1.add(6)
# print(s1)

# s1 = {1, 2, 3, 4, 5}
# s1.update([6,7,8])
# print(s1)

# s1 = {1, 2, 3, 4, 5}
# s2 = {7,8,9}
# s1.update([6,7,8],s2)
# print(s1)

# s1 = {1, 2, 3, 4, 5}
# s1.discard(6)
# print(s1)

# s1 = {1,2,3}
# s2 = {2,3,4}
# s3 = {3,4,5}
# s4 = s1.intersection(s2,s3)
# print(s4)

# s1 = {1,2,3}
# s2 = {2,3,4}
# s3 = {3,4,5}
# s4 = s3.difference(s1,s2)
# print(s4)

# s1 = {1,2,3}
# s2 = {2,3,4}
# s3 = {3,4,5}
# s4 = s1.symmetric_difference(s2)
# print(s4)

# l1 = [1,2,3,1,2,3]
# l2 = list(set(l1))
# print(l2)

employees = ['Aman','Rahul','Abhishek','April','July','Rudraksh','Varun','Ranveer']
gym_members = ['April','Varun','Aman']
developers = ['Rudraksh','Aman','Abhishek','Ranveer','April']
# result = set(gym_members).intersection(developers)
result = set(employees).difference(gym_members,developers)
print(result)