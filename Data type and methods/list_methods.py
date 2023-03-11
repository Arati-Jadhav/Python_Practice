# List methods ---------------------------------------------------------------------------------------------------------
"""
list1 = [4, 6, 'a', 2.5, 'hello']
print(list1, type(list1))
# [4, 6, 'a', 2.5, 'hello'] <class 'list'>

var1 = list1[-1]
print(var1, type(var1))
# hello <class 'str'>

list2 = [4, 6, 'a', 2.5, 'hello', [5, 7, 8], (2, 5, 7), {'a' : 234, 'b' : 678}]
print(list2)
# [4, 6, 'a', 2.5, 'hello', [5, 7, 8], (2, 5, 7), {'a': 234, 'b': 678}]

print(list2[5][2])
# 8

# print reversed list
print(list2[ : : -1])
# [{'a': 234, 'b': 678}, (2, 5, 7), [5, 7, 8], 'hello', 2.5, 'a', 6, 4]

print(list2[1 : : ])
# [6, 'a', 2.5, 'hello', [5, 7, 8], (2, 5, 7), {'a': 234, 'b': 678}]

# apply loop on list
list3 = [4, 6, 23, 47, 2]

for var in list3 :
    print(var, var**2)
# 4 16
# 6 36
# 23 529
# 47 2209
# 2 4

for i in range(len(list3)) :
    print(i, list3[i], list3[i]**2)
# 0 4 16
# 1 6 36
# 2 23 529
# 3 47 2209
# 4 2 4

# get odd numbers from list
list4 = [4, 6, 23, 47, 2]
for var in list3 :
    if var % 2 != 0 :
        print(var)
    else :
        continue
# 23
# 47
-------------------------------------------------------------------------------------------------------------------------------------------------------------

print(dir(list))
append, clear, copy, count, extend, index, insert, pop, remove, reverse, reversed, sort


# append method (add one element at a time) -----------------------------------------------------------------------------------------------
list4 = [5, 7, 2, 9, 3]
print(list4)
# [5, 7, 2, 9, 3]

list4.append(40)
print(list4)
# [5, 7, 2, 9, 3, 40]

list4.append("hello")
print(list4)
# [5, 7, 2, 9, 3, 40, 'hello']

##### program to copy content of one list to another empty list
list1 = [5, 2, 7, 12, 30, 67, 89, 15]
# output1[] should contain all elements from list1
# output2[] should contain numbers divisible by 3
output1 = []
for var in list1 :
    output1.append(var)
print(output1)
# [5, 2, 7, 12, 30, 67, 89, 15]

output2 = []
for var in list1 :
    if var % 3 == 0 :
        output2.append(var)
    else :
        continue
print(output2)
# [12, 30, 15]

# Insert method (insert element at the specific place in the list) --------------------------------------------------------------------------------------------------------------------------------
list1 = [5, 2, 7, 12, 30, 67, 89, 15]
list1.insert(2, 'python')
print(list1)
# [5, 2, 'python', 7, 12, 30, 67, 89, 15]

list1.insert(4, (4, 5, 6, 8))
print(list1)
# [5, 2, 'python', 7, (4, 5, 6, 8), 12, 30, 67, 89, 15]

# extend method (extend data from one list to another) -----------------------------------------------------------------------------------------------------------------------------------------
list3 = [3, 5, 7]
list4 = [56, 76, 89]
list4.extend(list3)
print(list4)
# [56, 76, 89, 3, 5, 7]

# Concate 2 lists with + operator -->
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8, 9]
list3 = list1 + list2
print("list1 : ", list1)
print("list2 : ", list2)
print("list3 : ", list3)
# list1 :  [1, 2, 3, 4]
# list2 :  [5, 6, 7, 8, 9]
# list3 :  [1, 2, 3, 4, 5, 6, 7, 8, 9]

# remove (remove data from list) ---------------------------------------------------------------------------------------------------------------------------------
list2 :  [5, 6, 7, 8, 9]
list2.remove(5)
print(list2)
# [6, 7, 8, 9]


# Program to insert any element in the list after the target element (with insert method)
input = [6, 4, 3, 16, 12, 15, 23, 45]
var1 = 60
tar = 15
leng = len(input)

for i in range(leng) :
    if input[i] == tar :
        input.insert(i+1, var1)
        break
    else :
        continue
print("input list : ", input)
# input list :  [6, 4, 3, 16, 12, 15, 60, 23, 45]

# Program to insert any element in the list after the target element (with append method)
input = [6, 4, 3, 16, 12, 15, 23, 45]
var1 = 60
tar = 15
leng = len(input)
output = []
for i in range(leng) :
    if input[i] == tar :
        output .append(input[i])
        output.append(var1)
    else :
        output.append(input[i])
print("input list : ", output)
# input list :  [6, 4, 3, 16, 12, 15, 60, 23, 45]

# pop method ----------------------------------------------------------------------------------------------------------------------------
# remove data from list using index value, default index value is -1 (from last of the list)
# also returned removed data

list1 = [6, 4, 3, 16, 12]
var1  = list1.pop()
print(var1)
print(list1)
# 12
# [6, 4, 3, 16]

# pop element at index 2
list1 = [6, 4, 3, 16, 12]
var1 = list1.pop(2)
print(var1)
print(list1)
# 3
# [6, 4, 16, 12]

# program to move data from one list to another list which is empty
list1 = [5, 7, 82, 8, 9]
list2 = []
for i in range(len(list1)) :
    var1 = list1.pop(0)
    list2.append(var1)
print("list1 : ", list1)
print("list2 : ",list2)
# list1 :  []
# list2 :  [5, 7, 82, 8, 9]

# program to move data from list to dictionary (class work) ----------------------------------->
list1 = [5, 7, 82, 8, 9]
dict1 = {}
for i in range(len(list1)) :
    var1 = list1.pop(0)
    dict1[var1] = var1**2
print("list1 : ", list1)
print("dict1 : ", dict1)
# list1 :  []
# dict1 :  {5: 25, 7: 49, 82: 6724, 8: 64, 9: 81}

# delete entire list ----------------------------------------------------------------------------------------------------------------------------
# this will delete entire list from the memory, once it is deleted we cannot recover it.
list1 = [5, 7, 8, 9]
del list1
#print(list1)
# NameError: name 'list1' is not defined. Did you mean: 'list2'?

# count method (give count of any element of the list) --------------------------------------------------------------------------------------------
list2 = [5, 7, 82, 8, 9, 7, 2, 8, 12]
output = list2.count(8)
print("count of 8 : ", output)
# count of 8 :  2

# program to get count of each data without repetition----------------------->
list1 = [5, 7, 82, 8, 9, 7, 2, 8, 12]
list2 = []
i = 0
for i in range(len(list1)) :
    var1 = list1.pop(0)
    if var1 not in list2 :
        print("count of ", var1, " is : ", list1.count(var1)+1)
        list2.append(var1)
    else :
        continue
# count of  5  is :  1
# count of  7  is :  2
# count of  82  is :  1
# count of  8  is :  2
# count of  9  is :  1
# count of  2  is :  1
# count of  12  is :  1

# index method (get index of any element) ------------------------------------------------------------------------------------------------
list1 = [5, 7, 82, 8, 9, 7, 2, 8, 12]
# get index of 82
output = list1.index(82)
print("output 82 : ", output)
# output 82 :  2

# sorting of data methods -----------------------------------------------------------------------------------------------------------------------
# sort method  ---> sort all the data in the list in ascending order by default and modify list inplace (modify original list)

list1 = [5, 7, 82, 8, 9, 7, 2, 8, 12]
list1.sort()
print("list1 : ", list1)
# list1 :  [2, 5, 7, 7, 8, 8, 9, 12, 82]

list1.sort(reverse = True)
print("list1 : ", list1)
# list1 :  [82, 12, 9, 8, 8, 7, 7, 5, 2]

# sorted method : this method sort any sequential data type as per requierement  and does not modify list in place -->

list1 = [2, 5, 7, 7, 8, 8, 9, 12, 82]
output = sorted(list1)  # ascending order
print("list1 : ", list1)
print("output : ", output)
# list1 :  [2, 5, 7, 7, 8, 8, 9, 12, 82]
# output :  [2, 5, 7, 7, 8, 8, 9, 12, 82]

output2 = sorted(list1, reverse = True)
print("list1 : ", list1)
print("output2 : ", output2)
# list1 :  [2, 5, 7, 7, 8, 8, 9, 12, 82]
# output2 :  [82, 12, 9, 8, 8, 7, 7, 5, 2]

# Copy method -------------------------------------------------------------------------------------------------------------------------------------------
#  shallow copy --> when we assign one list to another list and modify second list
# changes will reflect in both
# basically both of them point to same list

list1 = [2, 5, 7, 7, 8, 8, 9, 12, 82]
list2 = list1
print("list1 : ", list1)
print("list2 : ", list2)
# list1 :  [2, 5, 7, 7, 8, 8, 9, 12, 82]
# list2 :  [2, 5, 7, 7, 8, 8, 9, 12, 82]

list2.append(45)    # we are adding element in list2
print("list1 : ", list1)
print("list2 : ", list2)
# list1 :  [2, 5, 7, 7, 8, 8, 9, 12, 82, 45]
# list2 :  [2, 5, 7, 7, 8, 8, 9, 12, 82, 45]


# Deep copy --> when we copy one list to another and modify second list then the changes will not reflect in first list
list1 = [2, 5, 7, 7, 8, 8, 9, 12, 82]
list2 = list1.copy()
print("list1 : ", list1)
print("list2 : ", list2)
# list1 :  [2, 5, 7, 7, 8, 8, 9, 12, 82]
# list2 :  [2, 5, 7, 7, 8, 8, 9, 12, 82]

list2.append(450)
print("list1 : ", list1)
print("list2 : ", list2)
# list1 :  [2, 5, 7, 7, 8, 8, 9, 12, 82]
# list2 :  [2, 5, 7, 7, 8, 8, 9, 12, 82, 450]

# Reverse method ------------------------------------------------------------------------------------------------------------------------------------------
1. reverse method
2. reversed method
3. slicing
4. for loop
5. while loop

# 1. reverse method -------------------------------------------------------------------------------------------------------------------------------------
list1 = [5, 7, 2, 8, 34]
list1.reverse()
print(list1)
# [34, 8, 2, 7, 5]

# 2. reversed method -----------------------------------------------------------------------------------------------------------------------------------
list1 = [5, 7, 2, 8, 34]
list2 = reversed(list1)
print("list1 : ", list1)
for var in list2 :
    print(var, end = " ")
# list1 :  [5, 7, 2, 8, 34]
# 34 8 2 7 5

# slicing method -----------------------------------------------------------------------------------------------------------------------
list1 = [5, 7, 2, 8, 34]
print(list1[ : : -1])
# [34, 8, 2, 7, 5]

# for loop (class work) --------------------------------------------------------------------------------------------------------------
list1 = [5, 7, 2, 8, 34]
for i in range(len(list1) -1, -1, -1) :
    print(list1[i], end = " ")
# 34 8 2 7 5

# while loop (class work) ------------------------------------------------------------------------------------------------------------------------------

list1 = [5, 7, 2, 8, 34]
i = len(list1) - 1
while i > -1 :
    print(list1[i], end = " ")
    i = i - 1
# 34 8 2 7 5

# list comprehension ------------------------------------------------------------------------------------------------------------------------------------
 # program to find squares of all numbers in the list
list1 = [2, 4, 3, 6, 4, 8]
result1 = [x**2    for x in list1]
print(result1)
# [4, 16, 9, 36, 16, 64]

# program to get all even numbers from list
list1 = [2, 4, 3, 6, 5, 9]
result = [x  for x in list1 if x % 2 == 0]
print(result)
# [2, 4, 6]

# program to get all even odd numbers based on condition
list1 = [2, 4, 3, 6, 5, 9]
result = [(x, 'even') if x % 2 == 0 else (x, 'odd') for x in list1]
print(result)
# [(2, 'even'), (4, 'even'), (3, 'odd'), (6, 'even'), (5, 'odd'), (9, 'odd')]

# program to check number is divisible by 7 or not
list1 = [5, 7, 21, 49, 22]
result = [(x, 'yes') if x % 7 == 0 else (x, 'no') for x in list1]
print(result)
# [(5, 'no'), (7, 'yes'), (21, 'yes'), (49, 'yes'), (22, 'no')]

# program to repeat number 3 times if divided by 3 else repeat 2 times
list1 = [5, 7, 21, 49, 22]
result = [((str(x) * 3)) if x % 3 == 0 else (str(x) * 2) for x in list1]
print(result)
# ['55', '77', '212121', '4949', '2222']
"""

a = [1,2,3,4]
a.extend('swanamit')
print(a)