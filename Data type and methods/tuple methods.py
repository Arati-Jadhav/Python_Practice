# Tuple
"""
--> Tuple is immutable datatype
--> any type of data can be tuple
--> follows positive and negative index

tup1 = (2, 4, 5, [5, 7, 8], {'a' : 4, 'b' : 5})
print(tup1)
# (2, 4, 5, [5, 7, 8], {'a': 4, 'b': 5})

# positive index
output = tup1[2]
print(output)
# 5

# negative indexing
output2 = tup1[-2]
print(output2)
# [5, 7, 8]

tup11 = (4, 7, 8, [4, 7, 3], (2, 4, 5), {'a' : 123, 'b' : 345}, 'programming')
print(tup11)
# (4, 7, 8, [4, 7, 3], (2, 4, 5), {'a': 123, 'b': 345}, 'programming')

# loop without indexing :
for var in tup11 :
    print(var, end = " ")
# 4 7 8 [4, 7, 3] (2, 4, 5) {'a': 123, 'b': 345} programming

# loop with indexing :
for i in range(0, len(tup11), 1) :
    print(tup11[i], end  = " ")
# 4 7 8 [4, 7, 3] (2, 4, 5) {'a': 123, 'b': 345} programming

# check if any data is available in tuple or not :
tup11 = (4, 7, 8, [4, 7, 3], (2, 4, 5), {'a' : 123, 'b' : 345}, 'programming')
val = (2, 4, 5)
output = True if val in tup11 else False
print(output)
# True

print(dir(tuple))
# count, index

# count, index methods
tup11 = (4, 7, 8, [4, 7, 3], (2, 4, 5), {'a' : 123, 'b' : 345}, 'programming')
output = tup11.count(4)
print(output)
# 1

# program to get all the datat and avoid duplication--------------------------------------------------------------------------------------------
tup11 = (4, 7, 8, [4, 7, 3], (2, 4, 5), {'a' : 123, 'b' : 345}, 'programming', (2, 4, 5), 7, 8, [4, 7, 3])
list1 = []
for val in tup11 :
    if val in list1 :
        continue
    else :
        print(val, ' : ', tup11.count(val))
        list1.append(val)
# 4  :  1
# 7  :  2
# 8  :  2
# [4, 7, 3]  :  2
# (2, 4, 5)  :  2
# {'a': 123, 'b': 345}  :  1
# programming  :  1

# index method --> get index of any element-------------------------------------------------------------------------------------------
tup11 = (4, 7, 8, [4, 7, 3], (2, 4, 5), {'a' : 123, 'b' : 345}, 'programming')
output = tup11.index([4, 7, 3])
print('index of [4, 7, 3] : ', output)
# index of [4, 7, 3] :  3

# modify data in tuple---------------------------------------------------------------------------------------------------------------------------

tup2 = (5, 7, 8, 9)
list1 = list(tup2)
list1.append(12)
print('new tuple : ', tuple(list1))
print('Original tuple : ', tup2)
# new tuple :  (5, 7, 8, 9, 12)
# Original tuple :  (5, 7, 8, 9)

# modify data in tuple in place
list1= [4, 6, 8]
tup1 = (1, 3, 5, list1)
print(tup1)
# (1, 3, 5, [4, 6, 8])

list1.append(45)
print(tup1)
# (1, 3, 5, [4, 6, 8, 45])

# reverse the tuple ------------------------------------------------------------------------------------------------------------------------
tup2 = (2, 4, 6, 8)
print(tup2[ : : -1])
# (8, 6, 4, 2)

# with reversed method -----------------------------------------------------------------------------------------------------
tup2 = (2, 4, 6, 8)
output = reversed(tup2)
for var in output :
    print(var, end = " ")
# 8 6 4 2

# reverse with loop --------------------------------------------------------------------------------------------------------------
tup2 = (2, 4, 6, 8)
for i in range(-1, -len(tup2)-1, -1) :
    print(tup2[i], end = " ")
# 8 6 4 2

# sorting methods -------------------------------------------------------------------

# sort method ----------------------------------------------------------------------------------------->
tup3 = (4, 2, 6, 1, 8)
print(tuple(sorted(tup3)))
# (1, 2, 4, 6, 8)

# Fine minimum, maximum, sum numbers in the tuple -----------------------------------------------------------
# find sum ----------->
tup3 = (4, 2, 6, 1, 8)
sum = 0
for val in tup2 :
    sum = sum + val
print(sum)
# 20

# inbuilt method for sum-----------------------------------------------------------
#print(sum(tup3))
# 20

list11  = [6, 8, 3, 8, 2, 6, 8, 9]
print('sum of list values : ', sum(list11))
# sum of list values :  50

# program to get max value from tuple --------------------------->
tup11 = (16, 8, 3, 18, 22, 66, 8, 9)
max = 0
for data in tup11 :
    if data > max :
        max = data
print('maximum number from tuple is : ', max)
# maximum number from tuple is :  66

# by inbuilt method------------------------------------------------------------------------------------------------------------------------------------
tup11 = (16, 8, 3, 18, 22, 66, 8, 9)
print('maximum number from tuple is : ', max(tup11))
# maximum number from tuple is :  66

# by inbuilt method
tup11 = (16, 8, 3, 18, 22, 66, 8, 9)
print('minimum number from tuple is : ', min(tup11))
# minimum number from tuple is :  3

# program to find second largest number from the tuple ---------------------------------------------------------------------
tup1 = (11, 5, 12, 8, 1, 9, 0)
output = sorted(tup1)
print('Second largest number from tuple : ', output[-2])
# Second largest number from tuple :  11

# program to find all prime numbers from the tuple -----------------------------------------------------------------------------
tup1 = (5, 12, 11, 23, 29, 31, 50, 49, 33)
list1 = []
for val in tup1:
        prime = True
        for i in range(2, val):
                if val % i == 0:
                        prime = False
                        break
        if prime:
                list1.append(val)
print(tuple(list1))
# (5, 11, 23, 29, 31)

# Program to check palindrome from tuple elements ------------------------------------------------------------------------------------------------
# tup1 = (5, 7,  8, 23, 131, 243, 545, 787)
# output = (131, 545, 787)

tup1 = (5, 7,  8, 23, 131, 243, 545, 787)
output = []
for val in tup1 :
    temp = str(val)
    if str(val) == temp[ : : -1] :
        output.append(val)
print(tuple(output))
# (5, 7, 8, 131, 545, 787)

# Program to find largest prime numbers from the tuple -----------------------------------------------------------------------------
tup1 = (5, 7, 8, 12, 21, 61, 97, 101, 78)
output = 101

tup1 = (5, 7, 8, 12, 21, 61, 97, 101, 78)
list1 = []
for val in tup1:
        prime = True
        for i in range(2, val//2):
                if val % i == 0:
                        prime = False
                        break
        if prime:
                list1.append(val)

output = sorted(list1)[-1]
print("Largest prime number from the tuple is : ", output)
# Largest prime number from the tuple is :  101
"""