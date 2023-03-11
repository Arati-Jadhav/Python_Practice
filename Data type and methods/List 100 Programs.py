"""
# 1). Print the square of each number from the list.
list1 = [1, 2, 3, 4, 5, 6]
result = [x**2 for x in list1]
print(result)
# [1, 4, 9, 16, 25, 36]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2). Add elements from list1 to list2.
list1 = [1, 2, 3, 4, 5, 6]
list2 = []
for i in range(len(list1)) :
    var = list1.pop(0)
    list2.append(var)
print("list1 : ", list1)
print("list2 : ", list2)
# list1 :  []
# list2 :  [1, 2, 3, 4, 5, 6]
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3). Write a program to print the sum of all the elements of a list
list1 = [1, 2, 3, 4, 5, 6]
sum = 0
for var in list1 :
    sum = sum + var
print("sum is : ", sum)
# sum is :  21
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4). Write a program to print products of all the elements of a list.
list1 = [1, 2, 3, 4, 5, 6]
pro = 1
for var in list1 :
    pro = pro * var
print("product is : ", pro)
# product is :  720
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5). Find the largest and smallest elements of a list.
list1 = [3, 5, 2, 7, 1]
small = list1[0]
large = 0
for var in list1 :
    if var > large :
        large = var
    if var < small :
        small = var
print("largest element : ", large)
print("smallest element : ", small)
# largest element :  7
# smallest element :  1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6). Write a program to separate odd and even elements from a list.
list1 = [3, 45, 66, 13, 98, 55, 34, 67]
list2 = []
for var in list1 :
    if var % 2 == 0 :
        list2.append(var)
        list1.remove(var)
print("even numbers : ", list2)
print("odd numbers : ", list1)
# even numbers :  [66, 98, 34]
# odd numbers :  [3, 45, 13, 55, 67]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 7). Write a program to remove all duplicate elements from the list.
list1 = [34, 45, 13, 13, 98, 67, 34, 67]
list2 = []
for var in list1 :
    if var in list2 :
        list1.remove(var)
    else :
        list2.append(var)
print("list without duplicates : ", list1)
# list without duplicates :  [45, 13, 98, 67, 34, 67]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 8). Write a program to print a combination of 2 elements from the list which has sum is 10.
list1 = [2, 4, 6, 5, 1, 9, 8, 7]
list2 = []
for i in range(len(list1)) :
    for j in range(i+1, len(list1), 1) :
        if list1[i] + list1[j] == 10 :
            list2.append((list1[i] , list1[j]))
print(list2)
# [(2, 8), (4, 6), (1, 9)]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 9). Program to print squares of all even numbers using list comprehension.
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
result = [x**2 for x in list1 if x % 2 == 0 ]
print("Even number square : ", result)
# Even number square : [4, 16, 36, 64]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 10). Write a python program to split the list two-part, left side all odd values and the right side all even values.
# Input list = [5, 7, 2, 8, 11, 12, 17, 19, 22]
# Output = [5, 7, 11, 17, 19, 2, 8, 12, 22]

list1 = [5, 7, 2, 8, 11, 12, 17, 19, 22]
listodd =[]
listeven = []
for var in list1 :
    if var % 2 == 0 :
        listeven.append(var)
    else :
        listodd.append(var)
output = listodd + listeven
print("output list : ", output)
# output list :  [5, 7, 11, 17, 19, 2, 8, 12, 22]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 11).  Write a python program to get common elements from two lists.
# list1 = [4, 5, 7, 9, 2, 1]
# list2 = [2, 5, 8, 3, 4, 7]
# common_element = [4, 5, 7, 2]

list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
list3 = []
for var  in list1 :
    if var in list2 :
        list3.append(var)
print(list3)
# [4, 5, 7, 2]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 12). Write a python program to reverse a list with for loop.
list1 = [5, 7, 2, 8, 34]
for i in range(len(list1) -1, -1, -1) :
    print(list1[i], end = " ")
# 34 8 2 7 5
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 13). Write a python program to reverse a list with a while loop.
list1 = [5, 7, 2, 8, 34]
i = len(list1) - 1
while i > -1 :
    print(list1[i], end = " ")
    i = i - 1
# 34 8 2 7 5
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 14). Write a python program to reverse a list using index slicing.
list1 = [5, 7, 2, 8, 34]
print(list1[ : : -1])
# [34, 8, 2, 7, 5]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 15). Write a python program to reverse a list with reversed and reverse methods.
# 1. reverse method --------------------------------------------------->
list1 = [5, 7, 2, 8, 34]
list1.reverse()
print(list1)
# [34, 8, 2, 7, 5]

# 2. reversed method --------------------------------------------------->
list1 = [5, 7, 2, 8, 34]
list2 = reversed(list1)
print("list1 : ", list1)
for var in list2 :
    print(var, end = " ")
# list1 :  [5, 7, 2, 8, 34]
# 34 8 2 7 5
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 16). Write a python program to copy or clone one list to another list.
list1 = [2, 5, 7, 7, 8, 8, 9, 12, 82]
list2 = list1.copy()
print("list1 : ", list1)
print("list2 : ", list2)
# list1 :  [2, 5, 7, 7, 8, 8, 9, 12, 82]
# list2 :  [2, 5, 7, 7, 8, 8, 9, 12, 82]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 17). Write a python program to return True if two lists have any common member.
list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
for var in list1 :
    if var in list2 :
        print("True")
        break
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 18). Write a python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = []
for i in range(len(list1)) :
    if i == 0 or i == 2 or i == 5 :
        continue
    else :
        list2.append(list1[i])
print(list2)
# [2, 4, 5, 7]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 20). Write a python program to remove all negative values from the list.
list1 = [0, 4, -4, 6, -2, 1, -6, 8]
for var in list1 :
    if var < 0 :
        list1.remove(var)
print(list1)
# [0, 4, 6, 1, 8]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 21). write a python program to get a list of all elements which are divided by 3 and 7.
list1 = [21, 23, 56, 49,  63]
list2 = []
for var in list1 :
    if var % 3 == 0 and var % 7 == 0 :
        list2.append(var)
print("List of elements which are divisible by 3 and 7 both : ", list2)
# List of elements which are divisible by 3 and 7 both :  [21, 63]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 22). Write a python program to check the given list following palindrome (should be equal from both the side)
list1 = ['amit', 'jahaj', 'swanand', 'madam']
list2 = []
for word in list1 :
    temp = word[ : : -1]
    if temp == word :
        list2.append(word)
print('Palindrome list : ', list2)
# Palindrome list :  ['jahaj', 'madam']
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 23). Write a Python Program to get a list of words which has vowels in the given string.
# Input: “www Student ppp are qqqq learning Python vvv”
# Output : [‘Student’, ‘are’, ‘learning’, ‘Python’]

list2 = []
vow = 'aeiou'
input = 'www Student ppp are qqqq learning Python vvv'
list1 = input.split()
for word in list1 :
    for i in range(len(word)) :
        if word[i] in vow :
            list2.append(word)
            break
print('List of words contains vowels : ', list2)
# List of words contains vowels :  ['Student', 'are', 'learning', 'Python']
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  24). Write a python program to add 2 lists with extend method.
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list1.extend(list2)
print('Extended list : ', list1)
# Extended list :  [1, 2, 3, 4, 5, 6, 7, 8]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 25). Write a python program to sort list data, with the sort and sorted method.

# sort method --------->
list1 = [5, 7, 82, 8, 9, 7, 2, 8, 12]
list1.sort()
print("list1 : ", list1)
# list1 :  [2, 5, 7, 7, 8, 8, 9, 12, 82]

# sorted method ----------->
list1 = [2, 5, 7, 7, 8, 8, 9, 12, 82]
output = sorted(list1)
print("list1 : ", list1)
print("output : ", output)
# list1 :  [2, 5, 7, 7, 8, 8, 9, 12, 82]
# output :  [2, 5, 7, 7, 8, 8, 9, 12, 82]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 26). Write a python program to remove data from the list from a specific index using the pop method.
list1 = [1, 3, 5, 7, 9]
list1.pop(3) # 7
print(list1)
# [1, 3, 5, 9]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 27). Write a python program to get the max, min, and sum of the list using inbuilt method.
list1 = [34, 56, 32, 1, 45, 9]
print("Sum of list elements is : ", sum(list1))
print("largest element of list elements is : ", max(list1))
print("smallest element of list elements is : ", min(list1))
# Sum of list elements is :  177
# largest element of list elements is :  56
# smallest element of list elements is :  1
 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 28). Write a python program to check whether a list contains a sublist.
list1 = [5, 6, 3, 8, 2, 1, 7, 1]
print("The original list : " + str(list1))
sublist = [8, 2, 1]
res = False
for i in range(len(list1) - len(sublist) + 1) :
        if list1[i : i + len(sublist)] == sublist :
            res = True
            break
print("Is sublist present in list ? : " + str(res))
# Is sublist present in list ? : True
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 29). Write a python program to generate all sublists with 5 lengths from the given list.
list1 = [5, 6, 3, 8, 2, 1, 7, 1]
lists = [[]]
for i in range(len(list1) + 1) :
    for j in range(i):
        lists.append(list1[j: i])
for val in lists :
    if len(val) == 5 :
        print(val)
# [5, 6, 3, 8, 2]
# [6, 3, 8, 2, 1]
# [3, 8, 2, 1, 7]
# [8, 2, 1, 7, 1]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 30). Write a python program to find the second smallest number from the list.
list1 = [5, 6, 3, 8, 2, 1, 7]
output = sorted(list1)[1]
print(output)
# 2
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 31). Write a python program to find the second largest number from the list.
list1 = [5, 6, 3, 8, 2, 1, 7]
output = sorted(list1)[-2]
print(output)
# 7
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 32). Write a python program to merge all elements of the list in a single entity using a special character.
list1 = ['5', '6', '3', '8', '2', '1', '7']
output = '&'.join(list1)
print(output)
# 5&6&3&8&2&1&7
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 33). Write a python program to get the difference between two lists.
list1 = [5, 6, 3, 8, 2, 1, 7]
list2 = [5, 32, 78, 6, 65, 3]
for val in list1 :
    if val in list2 :
        continue
    else :
        print(val, end = " ")
# 8 2 1 7
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 34). Write a python program to reverse all the elements of the list.
# Input = [‘Sqa’, ‘Tools’, ‘Online’, ‘Learning’, ‘Platform’]
# output = [‘aqS’, ‘slooT’, ‘enilno’, ‘gninraeL’, ‘mroftalP’]

input = ['Sqa', 'Tools', 'Online', 'Learning', 'Platform']
output = []
for val in input :
    output.append(val[ : : -1])
print(output)
# ['aqS', 'slooT', 'enilnO', 'gninraeL', 'mroftalP']
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 35). Write a python program to combine two list elements in the sublist.
# list1 = [3, 5, 7, 8, 9]
# list2 = [1, 4, 3, 6, 2]
# Output = [[3, 1], [5, 4], [7, 3], [8, 6], [9, 2]]

list1 = [3, 5, 7, 8, 9]
list2 = [1, 4, 3, 6, 2]
output = []
for i in range(len(list1)) :
    temp = [list1[i], list2[i]]
    output.append(temp)
print(output)
# [[3, 1], [5, 4], [7, 3], [8, 6], [9, 2]]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 36). Write a python program to get keys and values from the list of dictionaries.
# Input : [{‘a’:12}, {‘b’: 34}, {‘c’: 23}, {‘d’: 11}, {‘e’: 15}]
# Output :  [‘a’, ‘b’, ‘c’, ‘d’, ‘c’]    [12, 34, 23, 11, 15]

input = [{'a' :12}, {'b' : 34}, {'c' : 23}, {'d' : 11}, {'e' : 15}]
output1 = []
output2 = []
for val in input :
    k, v = zip(*val.items())
    output1.append(k)
    output2.append(v)
print(str(output1))
print(str(output2))
# [('a',), ('b',), ('c',), ('d',), ('e',)]
# [(12,), (34,), (23,), (11,), (15,)]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 37). Write a python program to get all the unique numbers in the list.

list1 = [1,3,5,3,2,7,8,1,4]
list2 = []
for val in list1 :
    if val in list2 :
        continue
    else :
        list2.append(val)
print(list2)
# [1, 3, 5, 2, 7, 8, 4]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 38). write a python program to convert a string into a list.
str1 = "1234567"
output = list(str1)
print(output)
# ['1', '2', '3', '4', '5', '6', '7']
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 39). Write a python program to replace the last number and the first number of the list with the word.
# Input: [12, 32, 33, 5, 4, 7]
# output : [‘SQA’, 32, 33, 5, 4, ‘Tools’]

input = [12, 32, 33, 5, 4, 7]
output = []
for i in range(len(input)) :
    if i == 0 :
        output.append('SQA')
    elif i == len(input) - 1 :
        output.append('Tools')
    else :
        output.append(input[i])
print(output)
# ['SQA', 32, 33, 5, 4, 'Tools']
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 40). Write a python program to check whether the given element is exist in the list or not.

input = [12, 32, 33, 5, 4, 7]
ele = 33
for val in input :
    if val == ele :
        print("Element is exist")
        break
# Element is exist
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 41). Write a python program to replace all odd index elements with words.
# Input: [12, 32, 33, 5, 4, 7, 33]
# Output: [12, ‘SQA’, 33, ‘Tools’, 4, ‘Python’, 33]

input = [12, 32, 33, 5, 4, 7, 33]
output = []
for i in range(len(input)) :
    if i == 1 :
        output.append('SQA')
    elif i == 3 :
        output.append('Tools')
    elif i == 5 :
        output.append('Python')
    else :
        output.append(input[i])
print(output)
# [12, 'SQA', 33, 'Tools', 4, 'Python', 33]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 42). Write a python program to take two lists and return true if then at least one common member.

list1 = [3, 5, 7, 8, 9]
list2 = [1, 4, 3, 6, 2]
for val in list1 :
    if val in list2 :
        print('True')
        break
# True
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 43). Write a python program to convert multiple numbers from a list into a single number.
# Input: [12, 45, 56]
# Output:124556

input = [12, 45, 56]
for val in input :
    print(val, end = "")
# 124556
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 44). Write a python program to convert words of a list into a single string.
# Input: [‘Sqa’, ‘Tools’,’Best’, ‘Learning’, ‘Platform’]
# Output: Sqa Tools Best Learning Platform

input = ['Sqa', 'Tools','Best', 'Learning', 'Platform']
for val in input :
    print(val, end = " ")
# Sqa Tools Best Learning Platform
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 45). Write a python program to split a list into different variables.
# Input: [(‘Black’, ‘Yellow’, ‘Blue’), (50, 55, 60), (30.0, 50.5, 55.66)]
# Output:
# (‘Black’, ‘Yellow’, ‘Blue’)
# (50, 55, 60)
# (30.0, 50.5, 55.66)

input = [('Black', 'Yellow', 'Blue'), (50, 55, 60), (30.0, 50.5, 55.66)]
for val in input :
    print(val)
# ('Black', 'Yellow', 'Blue')
# (50, 55, 60)
# (30.0, 50.5, 55.66)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 46). Write a python program to create a sublist of numbers and their squares from 1 to 10.
# Output : [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81], [10, 100]]

list1 = []
for i in range(1, 11, 1) :
    temp = [i, i**2]
    list1.append(temp)
print(list1)
# [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81], [10, 100]]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 47). Write a python program to create a list of five consecutive numbers in the list.
# Output : [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]

list1 = [ [5*i + j for j in range(1,6)] for i in range(4) ]
print(list1)
# [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 48). Write a python program to insert a given string at the beginning of all items in a list.
# Input: [1, 2, 3, 4, 5], Sqa
# Output: [‘Sqa1’, ‘Sqa2’, ‘Sqa3’, ‘Sqa4’, ‘Sqa5’]

output = []
input = [1, 2, 3, 4, 5]
for val in input :
    output.append('Sqa' + str(val))
print(output)
# ['Sqa1', 'Sqa2', 'Sqa3', 'Sqa4', 'Sqa5']
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 49). Write a python program to iterate over two lists simultaneously and create a list of sublists.
# list1 = [1, 3, 5, 7, 9]
# list2 = [8, 6, 4, 2, 10]
# output = [[1, 8], [3, 6], [5, 4], [7, 2], [9, 10]]

list1 = [1, 3, 5, 7, 9]
list2 = [8, 6, 4, 2, 10]
output = []
for i in range(len(list1)) :
    temp = [list1[i], list2[i]]
    output.append(temp)
print(output)
# [[1, 8], [3, 6], [5, 4], [7, 2], [9, 10]]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 50). Write a python program to move all positive numbers on the left side and negative numbers on the right side.
# Input: [2, -4, 6, 44, -7, 8, -1, -10]
# Output: [2, 6, 44, 8, -4, -7, -1, -10]

input = [2, -4, 6, 44, -7, 8, -1, -10]
output = []
for val in input :
    if val > 0 :
        output.append(val)
        input.remove(val)
output.extend(input)
print(output)
# [2, 6, 8, -4, 44, -7, -1, -10]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 51). Write a python program to move all zero digits to the end of a given list of numbers.
# Input: [3, 4, 0, 0, 0, 0, 6, 0, 4, 0, 22, 0, 0, 3, 21, 0]
# Output: [3, 4, 6, 4, 22, 3, 21, 0, 0, 0, 0, 0, 0, 0, 0]
input = [3, 4, 0, 0, 0, 0, 6, 0, 4, 0, 22, 0, 0, 3, 21, 0]
output = []
for val in input :
    if val == 0 :
        output.append(val)
    else :
        output.insert(0, val)
print("Output : ", output)
# Output :  [21, 3, 22, 4, 6, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 52). Write a python program to find the list in a list of lists whose sum of elements is the highest.
# Input: [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7 8, 9]]
# Output: [10, 11, 12]

input = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
output = input[1]
for i in input :
    if sum(i) > sum(output) :
        output = i
print("List with elements with highest sum : ", output)
# List with elements with highest sum :  [10, 11, 12]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 53). Write a python program to find the items that start with a specific character from a given list.
# Input: [‘abbcd’, ‘ppq, ‘abdd’, ‘agr’, ‘bhr’, ‘sqqa’, tools, ‘bgr’]
------------------------------------------
# item starts with a from the given list.
# [‘abbcd’, ‘abdd’, ‘agr’]
------------------------------------------
# item starts with b from the given list.
# [‘bhr’, ‘bgr’]
------------------------------------------
# item starts with c from the given list.
# []

input = ['abbcd', 'ppq', 'abdd', 'agr', 'bhr', 'sqqa', 'tools', 'bgr']
lista = []
listb = []
listc = []
list1 = []
for val in input :
    if val[0] == 'a' :
        lista.append(val)
    elif val[0] == 'b' :
        listb.append(val)
    elif val[0] == 'c' :
        listc. append(val)
    else :
        list1.append(val)
print("Starts with 'a' : ", lista)
print("Starts with 'b' : ", listb)
print("Starts with 'c' : ", listc)
print("Starts with other than a, b, c : ", list1)
# Starts with 'a' :  ['abbcd', 'abdd', 'agr']
# Starts with 'b' :  ['bhr', 'bgr']
# Starts with 'c' :  []
# Starts with other than a, b, c :  ['ppq', 'sqqa', 'tools']
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 54). Write a python program to count empty dictionaries from the given list.
# Input: [{}, {‘a’: ‘sqatools’}, {}, {‘a’: 123}, {}]
# empty_count: 3

input = [{}, {'a': 'sqatools'}, {}, {'a': 123}, {}]
output = input.count({})
print("empty items : ", output)
# empty items :  3
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 55). Write a python program to remove consecutive duplicates of given lists:
# Input: [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 4]
input =  [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
output = []
for i in range(len(input)) :
    if input[i] == input[i - 1] :
        continue
    else :
        output.append(input[i])
print("List of distinct elements : ", output)
# List of distinct elements :  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 56). Write a python program to pack consecutive duplicates of given list elements into sublists.
# Input: [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
# Output: [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6], [7], [8, 8], [9]]

input = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
output = []
for val in input :
    if [val] not in output :
        output.append([val])
    else :
        i = output.index([val])
        output[i].append(val)
print("Output :", output)
# Output : [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6], [7], [8, 8], [9]]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 57). Write a python program to split a given list into two parts where the length of the first part of the list is given.
# Input: [4, 6, 7, 3, 2, 5, 6, 7, 6, 4]
# length of the first part is 4
# Output: [[4, 6, 7, 3], [2, 5, 6, 7, 6, 4]]
leng = 3
input = [4, 6, 7, 3, 2, 5, 6, 7, 6, 4]
output = [[], []]
for i in range(len(input)) :
    if i <= leng :
        output[0].append(input[i])
    else :
        output[1].append(input[i])
print("Output :", output)
# Output : [[4, 6, 7, 3], [2, 5, 6, 7, 6, 4]]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 58). Write a python program to insert items at a specific position in the list.
# Input: [2, 4, 6, 8, 3, 22]
# Index: 3
# Item: 55
# Output: [2, 4, 6, 55, 8, 3, 22]

input = [2, 4, 6, 8, 3, 22]
index = 3
item = 55
input.insert(index, item)
print("output :", input)
# output : [2, 4, 6, 55, 8, 3, 22]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 59). Write a python program to select random numbers from the list.
# Input: [1, 4, 5, 7, 3, 2, 9]
# Selected 4 random numbers from the list.
# Output : [4, 5, 2, 1]

# Select 4 random numbers from the list.
import random
input = [1, 4, 5, 7, 3, 2, 9]
output = []
for i in range(4) :
    output.append(random.randint(0, len(input) - 1))
print("output :", output)
# output : [4, 6, 3, 6]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 60). Write a python program to create a 3*3 grid with numbers.        ---------------------> understand it correctly
# Output: [[4, 5, 6], [5, 6, 7], [7, 8, 9]]
output = [[]]
ind = 0
for i in range(1,10):
    if len(output[ind]) <=2:
        print(len(output[ind]))
        output[ind].append(i)
    else:
        ind += 1
        output.append([i])
print(output)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 61). Write a python program to zip two given lists of lists.
# list1: [[1, 3], [5, 7], [9, 11]]
# list2: [[2, 4], [6, 8], [10, 12, 14]]

list1 = [[1, 3], [5, 7], [9, 11]]
list2 = [[2, 4], [6, 8], [10, 12, 14]]

output = zip(list1, list2)
print("Zipped output :", output)
for val in output :
    print(val)
# ([1, 3], [2, 4])
# ([5, 7], [6, 8])
# ([9, 11], [10, 12, 14])
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 62). Write a python program to convert the first and last letter of each item from Upper case to lowercase
#     and lowercase to uppercase.
# Input: [‘Learn’, ‘python’, ‘From’, ‘Sqa’, tools]
# Output: [‘learN’, ‘PythoN’, ‘froM’,  sqA, ‘ToolS’]

input = ['Learn', 'python', 'From', 'Sqa', 'tools']
output = []
for val in input :
    temp = val[0].swapcase() + val[1: -1] + val[-1].swapcase()
    output.append(temp)
print("Output : ", output)
# Output :  ['learN', 'PythoN', 'froM', 'sqA', 'ToolS']
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 63). Write a python to find maximum and minimum values in the given heterogeneous list.
# Input: [‘Sqa’, 6, 5, 2, ‘Tools’]
# Output: [6,2]

input = ['Sqa', 6, 5, 2, 'Tools']
mid = []
for val in input :
    if str(val).isdigit() == True :
        mid.append(val)
output = []
output.append(max(mid))
output.append(min(mid))
print("Maximum and minimum numbers from the list :", output)
# Maximum and minimum numbers from the list : [6, 2]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 64). Write a python program to sort a given list in ascending order according to the sum of its sublist.
# Input: [[3, 5, 6], [2, 1, 3], [5, 1, 1], [1, 2, 1], [0, 4, 1]]
#                14          6             7             4          5
# Output = [[1, 2, 1], [0, 4, 1], [2, 1, 3], [5, 1, 1], [3, 5, 6]]

input  =  [[3, 5, 6], [2, 1, 3], [5, 1, 1], [1, 2, 1], [0, 4, 1]]
output = []
mid = []
for i in input :
    mid.append(sum(i))
mid.sort()
for i in mid :
    for j in range(len(input)) :
        if i == sum(input[j]) :
            output.append(input[j])
print("Output :", output)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 65). Write a python program to extract the specified sizes of strings from a given list of string values.
# Input: [‘Python’, ‘Sqatools’, ‘Practice’, ‘Program’, ‘test’, ‘list’]
# size = 8
# Output: [‘Sqatools’, ‘Practice’]

input = ['Python', 'Sqatools', 'Practice', 'Program', 'test', 'list']
output = []
for val in input :
    if len(val) == 8 :
        output.append(val)
print("Elements of length 8 are :", output)
# Elements of length 8 are : ['Sqatools', 'Practice']
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 66). Write a python program to find the difference between consecutive numbers in a given list.
# Input list: [1, 1, 3, 4, 4, 5, 6, 7]
# Output list: [0, 2, 1, 0, 1, 1, 1]

input = [1, 1, 3, 4, 4, 5, 6, 7]
output = []
for i in range(len(input) - 1) :
    output.append(input[i+1] - input[i])
print("Difference list :", output)
# Difference list : [0, 2, 1, 0, 1, 1, 1]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 67). Write a python program to calculate the average of the given list.
# Input : [3, 5, 7, 2, 6, 12, 3]
# Output: 5.428571428571429

input = [3, 5, 7, 2, 6, 12, 3]
avg = sum(input) / len(input)
print("Average of the list elements :", avg)
# Average of the list elements : 5.428571428571429
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 68). Write a python program to count integers in a given mixed list.
# Input list: [‘Hello’, 45, ‘sqa’,  23, 5, ‘Tools’, 20]
# Output: 4

input = ['Hello', 45, 'sqa',  23, 5, 'Tools', 20]
cnt = 0
for val in input :
    if str(val).isnumeric() == True :
        cnt += 1
print("Count of numbers : ", cnt)
# Count of numbers :  4
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 69). Write a python program to access multiple elements of the specified index from a given list.
# Input list: [2, 3, 4, 7, 8, 1, 5, 6, 2, 1, 8, 2]
# Index list: [0, 3, 5, 6]
# Output: [2, 7, 1, 5]
input = [2, 3, 4, 7, 8, 1, 5, 6, 2, 1, 8, 2]
output = []
for i in [0, 3, 5, 6] :
    output.append(input[i])
print("Output : ", output)
# Output :  [2, 7, 1, 5]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 70). Write a python program to check whether a specified list is sorted or not.
# Input list : [1, 2, 3, 5, 7, 8, 9]
# Output: True

# Input list: [3, 5, 1, 6, 8, 2, 4]
# Output: False

input = [1, 2, 3, 5, 7, 8, 9]
output = sorted(input)
print("Check if list is sorted or not : ", input == output)
# Check if list is sorted or not :  True

input =  [3, 5, 1, 6, 8, 2, 4]
output = sorted(input)
print("Check if list is sorted or not : ", input == output)
# Check if list is sorted or not :  False
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 71). Write a python program to remove duplicate dictionaries from a given list.
# Input : [{‘name’: ‘john’}, {‘city’: ‘mumbai’}, {‘Python’: ‘laguage’}, {‘name’: ‘john’}]
# Output: [{‘city’: ‘mumbai’}, {‘Python’: ‘laguage’}]

input = [{'name': 'john'}, {'city': 'mumbai'}, {'Python': 'laguage'}, {'name': 'john'}]
output = []
for val in input :
    if val not in output :
        output.append(val)
print("List after removing duplicates : ", output)
# List after removing duplicates :  [{'name': 'john'}, {'city': 'mumbai'}, {'Python': 'laguage'}]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 72). Write a python program to check if the elements of a given list are unique or not.
# Input: [2, 5, 6, 7, 4, 11, 2, 4, 66, 21, 22, 3]
# Output: False

# Input: [2, 5, 8, 3, 6, 21]
# Output: True

input =  [2, 5, 6, 7, 4, 11, 2, 4, 66, 21, 22, 3]
output = []
for val in input :
    if val in output :
        print("No unique elements")
        break
    else :
        output.append(val)
# No unique elements

input = [2, 5, 8, 3, 6, 21]
output = []
for val in input :
    if val in output :
        print("No unique elements")
        break
    else :
        output.append(val)
print("Unique elements")
# Unique elements
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 73). Write a python program to remove duplicate sublists from the list.
# Input: [[1, 2], [3, 5], [1, 2], [6, 7]]
# Output: [[3, 5],[6, 7]]

input = [[1, 2], [3, 5], [1, 2], [6, 7]]
output = []
for i in input:
    if i not in output:
        output.append(i)
    else:
        output.remove(i)
print("List after removing duplicate sublists :", output)
# List after removing duplicate sublists : [[3, 5], [6, 7]]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 74). Write a python program to create a list by taking an alternative item from the list.
# Input: [3, 5, 7, 8, 2, 9, 3, 5, 11]
# Output: [3, 7, 2, 3, 11]

input =  [3, 5, 7, 8, 2, 9, 3, 5, 11]
i = 0
output = []
while i < len(input) :
    output.append(input[i])
    i += 2
print("list by taking an alternative item from the list :", output)
# list by taking an alternative item from the list : [3, 7, 2, 3, 11]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 75). Write a python program to remove duplicate tuples from the list.
# Input: [(2, 3), (4, 6), (5, 1), (2, 3), (7, 9), (5, 1)]
# Output: [(4, 6), (7, 9)]

input =  [(2, 3), (4, 6), (5, 1), (2, 3), (7, 9), (5, 1)]
output = []
for i in input:
    if i not in output:
        output.append(i)
    else:
        output.remove(i)
print("List after removing duplicate tuples :", output)
# List after removing duplicate tuples : [(4, 6), (7, 9)]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 76). Write a python program to insert an element before each element of a list.
# Input :[3, 5, 7, 8]
# element = ‘a’
# Output: [‘a’, 3, ‘a’, 5, ‘a’, 7, ‘a’, 8]
input = [3, 5, 7, 8]
i = 0
leng = len(input)
while i < leng * 2 :
    input.insert(i, 'a')
    i += 2
print("List after inserting elemnts :", input)
# List after inserting elemnts : ['a', 3, 'a', 5, 'a', 7, 'a', 8]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 77). Write a python program to remove the duplicate string from the list.
# Input: [‘python’, ‘is’, ‘a’, ‘best’, ‘language’, ‘python’, ‘best’]
# Output: [‘is’, ‘a’, ‘language’]

input = ['python', 'is', 'a', 'best', 'language', 'python', 'best']
output = []
for i in input:
    if i not in output:
        output.append(i)
    else:
        output.remove(i)
print("List after removing duplicates :", output)
# List after removing duplicates : ['is', 'a', 'language']
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 78). Write a python program to get the factorial of each item in the list.

input = [4, 7, 5, 9]
output = []
for val in input :
    temp = 1
    for i in range(1, val+1, 1) :
        temp *= i
    output.append(temp)
print("factorial list :", output)
# factorial list : [24, 5040, 120, 362880]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 79). Write a python program to get a list of Fibonacci numbers from 1 to 20.
num1 = 0
num2 = 1
output =[]
sum = 0
while(num1 + num2 < 20) :
    sum = num1 + num2
    output.append(sum)
    num1 = num2
    num2 = sum
print("Fibonacci numbers :", output)
# Fibonacci numbers : [1, 2, 3, 5, 8, 13, 21]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 80). Write a python program to reverse all the numbers in a given list.
# Input : [123, 145, 633, 654, 254]
# Output: [321, 541, 336, 456, 452]

input = [123, 145, 633, 654, 254]
output = []
for val in input :
    temp = str(val)[ : : -1]
    output.append(int(temp))
print("Output with reversed elements: ", output)
# Output with reversed elements:  [321, 541, 336, 456, 452]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 81). Write a python program to get palindrome numbers from a given list.
# Input : [121, 134, 354, 383, 892, 232]
# Output : [121, 282, 232]

input  = [121, 134, 354, 383, 892, 232]
output = []
for val in input :
    temp = str(val)[ : : -1]
    if int(temp) == val :
        output.append(val)
print("Palindrome elements: ", output)
# Palindrome elements:  [121, 383, 232]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 82). Write a python program to get a count of vowels in each word in a given list.
# Input : [‘Learning’, ‘Python’, ‘From’, ‘SqaTool’]
# Output : [{‘a’: 1, ‘e’: 1, ‘i’ : 1}, {‘o’: 1}, {‘a’:1, ‘o’: 2}]

input = ['Learning', 'Python', 'From', 'SqaTool']
vow = "aeiou"
output = []
for vo in input:
    dict1 = {}
    for vi in vo:
        if vi not in dict1 and vi.lower() in vow:
            dict1[vi] = 1
        elif vi in dict1:
            dict1[vi] += 1
    output.append(dict1)
print("Output :", output)
# Output : [{'e': 1, 'a': 1, 'i': 1}, {'o': 1}, {'o': 1}, {'a': 1, 'o': 2}]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 83). Write a python program to get the list of prime numbers in a given list:
# Input : [11, 8, 7, 19, 6, 29]
# Output : [11,  7,  19, 29]

input  = [11, 8, 7, 19, 6, 29]
list1 = []
for val in input:
        prime = True
        for i in range(2, val//2):
                if val % i == 0:
                        prime = False
                        break
        if prime:
                list1.append(val)
print("List of prime numbers from the list : ", list1)
# List of prime numbers from the list :  [11, 7, 19, 29]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 84). Write a python program to get a list with n elements removed from the left and right.
# Input : [2, 5, 7, 9, 3, 4]
# Remove 1 element from left
# [5, 7, 9, 3, 4]

input  = [2, 5, 7, 9, 3, 4]
input.pop(0)
print("Output : ", input)
# Output :  [5, 7, 9, 3, 4]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 85). Write a python program to create a dictionary with two lists.
# Input :
# list1 : [‘a’, ‘b’, ‘c’, ‘d’, ‘e’]
# list2 : [234, 123, 456, 343, 223]
# Output: {‘a’: 234, ‘b’: 123, ‘c’: 456, ‘d’: 343, ‘e’: 223}

list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [234, 123, 456, 343, 223]
output = {}
for i in range(len(list1)) :
    output[list1[i]] = list2[i]
print("Dictionary after combining 2 lists is :", output)
# Dictionary after combining 2 lists is : {'a': 234, 'b': 123, 'c': 456, 'd': 343, 'e': 223}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 86). Write a python program to remove the duplicate item from list using set.
# Input : [2, 5, 7, 8, 2, 3, 4, 12, 5, 6]
# Output : [2, 5, 7, 8, 3, 4, 12, 6]

input = [2, 5, 7, 8, 2, 3, 4, 12, 5, 6]
output = set(input)
print("Removing duplicates by using set :", list(output))
# Removing duplicates by using set : [2, 3, 4, 5, 6, 7, 8, 12]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 87). Write a python program to insert a sublist into the list at a specific index.
# Input : [4, 6, 8, 2, 3, 5]
# sublist, index
# [5, 2, 6], 3
# Output: [4, 6, 8, [5, 2, 6], 2, 3, 5]

# sublist, index
# [5, 2, 6], 3
input = [4, 6, 8, 2, 3, 5]
input.insert(3, [5, 2, 6])
print("Output :", input)
# Output : [4, 6, 8, [5, 2, 6], 2, 3, 5]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 88). Write a python program to calculate bills per fruit purchased from a given fruits list.
# Fruit list with Price: [[‘apple’, 30], [‘mango’, 50], [‘banana’, 20], [‘lichi’, 50]]
# Fruit with quantity: [[‘apple’, 2]]

# Bill :
# Fruit: Apple
# Bill: 60

input1 = [['apple', 30], ['mango', 50], ['banana', 20], ['lichi', 50]]
fruit = input("Enter fruit name : ")
quantity = int(input("Enter quantity : "))
for i in input1 :
    if i[0] == fruit :
        bill = quantity * i[1]
        print("Bill is: ", bill)
    else :
        continue
# Enter fruit name : apple
# Enter quantity : 6
# Bill is:  180
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 89). Write a python program to calculate marks percentage from a given mark list, the max mark for each item is 100.
# Marks_list : [80, 50, 70, 90, 95]
# Output: 77%

list1 = [80, 50, 70, 90, 95]
leng = len(list1)
total = leng * 100
sum1 = sum(list1)
per = (sum1 / total) * 100
print("Percentage is : ", per
# Percentage is :  77.0
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 90). Write a python program to get the list of all palindrome strings from the given list.
# Input: [‘data’, ‘python’, ‘oko’, ‘test’, ‘ete’]
# Output: [‘oko’, ‘ete’]

input = ['data', 'python', 'oko', 'test', 'ete']
output = []
for val in input :
    temp = val[ :  : -1]
    if val == temp :
        output.append(val)
print("Palindromes from the list are : ", output)
# Palindromes from the list are :  ['oko', 'ete']
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 91). Write a python program to flatten a given nested list structure.
# Input: [0, 12, [22, 32], 42, 52, [62, 72, 82], [92, 102, 112, 122]]
# Output: [0, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122]

input = [0, 12, [22, 32], 42, 52, [62, 72, 82], [92, 102, 112, 122]]
output = []
for i in input:
    if isinstance(i,list):
        for j in i:
            output.append(j)
    else:
        output.append(i)
print("Flatten List : ", output)
# Flatten List :  [0, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 92). Write a python program to convert tuples in the list into a sublist.
# Input: [(3, 5), (6, 8), (8, 11), (12, 14), (17, 23)]
# Output: [[3, 5], [6, 8], [8, 11], [12, 14], [17, 23]]

input = [(3, 5), (6, 8), (8, 11), (12, 14), (17, 23)]
output = []
for val in input :
    output.append(list(val))
print("Tuples converted into list : ", output)
# Tuples converted into list :  [[3, 5], [6, 8], [8, 11], [12, 14], [17, 23]]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 93). Write a python program to create dict from a sublist in a given sublist.
# Input: [[‘a’, 5], [‘b’, 8], [‘c’, 11], [‘d’, 14], [‘e’, 23]]
# Output: [{‘a’: 5}, {‘b’: 8}, {‘c’: 11}, {‘d’: 14}, {‘e’: 23}]

input = [['a', 5], ['b', 8], ['c', 11], ['d', 14], ['e', 23]]
output = []
for val in input :
    temp = {}
    temp[val[0]] = val[1]
    output.append(temp)
print("List converted into dictionary : ", output)
# List converted into dictionary :  [{'a': 5}, {'b': 8}, {'c': 11}, {'d': 14}, {'e': 23}]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 94). Write a python program to replace ‘Python’ with ‘Java' from the given list.
# Input: [‘Hello’, ‘student’, ‘are’, ‘learning’, ‘Python’, ‘Its’, ‘Python’, ‘Language’]
# Output: [‘Hello’, ‘student’, ‘are’, ‘learning’, ‘Java’, ‘Its’, ‘Java’, ‘Language’]

input = ['Hello', 'student', 'are', 'learning', 'Python', 'Its', 'Python', 'Language']
for i in range(len(input)) :
    if input[i] == 'Python' :
        input.insert(i, 'Java')
        input.pop(i+1)
print("Updated list : ", input)
# Updated list :  ['Hello', 'student', 'are', 'learning', 'Java', 'Its', 'Java', 'Language']
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 95). Write a python program to convert the 3rd character of each word to a capital case from the given list.
# Input: [‘Hello’, ‘student’, ‘are’, ‘learning’, ‘Python’, ‘Its’, ‘Python’, ‘Language’]
# Updated list :  ['HeLlo', 'stUdent', 'arE', 'leArning', 'PyThon', 'ItS', 'PyThon', 'LaNguage']

input = ['Hello', 'student', 'are', 'learning', 'Python', 'Its', 'Python', 'Language']
output = []
for i in input:
    res = ''
    for j in range(len(i)):
        if j == 2:
            res += i[j].upper()
        else:
            res += i[j]
    output.append(res)
print("Updated list : ", output)
# Updated list :  ['HeLlo', 'stUdent', 'arE', 'leArning', 'PyThon', 'ItS', 'PyThon', 'LaNguage']
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 96). Write a python program to remove the 2nd character of each word from a given list.
# Input: [‘Hello’, ‘student’, ‘are’, ‘learning’, ‘Python’, ‘Its’, ‘Python’, ‘Language’]
# Updated list :  ['Hllo', 'sudent', 'ae', 'larning', 'Pthon', 'Is', 'Pthon', 'Lnguage']

input = ['Hello', 'student', 'are', 'learning', 'Python', 'Its', 'Python', 'Language']
output = []
for i in input:
    res = ''
    for j in range(len(i)):
        if j == 1:
            continue
        else:
            res += i[j]
    output.append(res)
print("Updated list : ", output)
# Updated list :  ['Hllo', 'sudent', 'ae', 'larning', 'Pthon', 'Is', 'Pthon', 'Lnguage']
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 97). Write a python program to get a count of each word and add as a dictionary from the given list.
# Input: [‘Hello’, ‘student’, ‘are’, ‘learning’, ‘Python’, ‘Its’, ‘Language’]
# Output: [{‘Hello’:5}, {‘student’: 7}, {‘are’: 3}, {‘learning’: 8}, {‘Python’: 6}, {‘Its’: 3}, {‘Language’: 8}]

input = ['Hello', 'student', 'are', 'learning', 'Python', 'Its', 'Language']
output = []
for val in input :
    temp = {}
    temp[val] = len(val)
    output.append(temp)
print("Output : ", output)
# Output :  [{'Hello': 5}, {'student': 7}, {'are': 3}, {'learning': 8}, {'Python': 6}, {'Its': 3}, {'Language': 8}]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 98). Write a python program to remove duplicate dictionaries from the given list.
# Input: [{‘Hello’:5}, {‘student’: 7}, {‘are’: 3}, {‘learning’: 8}, {‘Hello’:5}, ,{‘Language’: 8}, {‘are’: 3}]
# Output: [{‘Hello’:5}, {‘student’: 7}, {‘learning’: 8}, {‘Language’: 8}, {‘are’: 3}]

input = [{'Hello':5}, {'student': 7}, {'are': 3}, {'learning': 8}, {'Hello':5} ,{'Language': 8}, {'are': 3}]
output = []
for val in input :
    if val not in output :
        output.append(val)
print("After removing duplicates : ", output)
# After removing duplicates :  [{'Hello': 5}, {'student': 7}, {'are': 3}, {'learning': 8}, {'Language': 8}]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 99). Write a python program to decode a run-length encoded given list.
# Original encoded list: [[2, 1], 2, 3, [2, 4], 5, 1]
# Decode a run-length encoded said list: [1, 1, 2, 3, 4, 4, 5, 1]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 100). Write a Python program to round every number of a given list of numbers and print the total sum multiplied by the
# length of the list.
# Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# Result: 243

input = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
output = []
for val in input :
    output.append(round(val))
sum1 = sum(output) * len(output)
print("Output : ", sum1)
# Output :  243
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""