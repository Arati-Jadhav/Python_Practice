'''
# 1). Write a Python program to add elements to the dictionary.
dict1 = {}
dict1['a'] = 1234
print("dictionary after adding elements : ", dict1)
# dictionary after adding elements :  {'a': 1234}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2). Write a Python program to print the square of all values in a dictionary.
# Input : {'a': 5, 'b':4, 'c': 6, 'd' : 7}
# Output :
# a : 25
# b : 16
# c : 36
# d : 49

input = {'a' : 5, 'b' : 4, 'c' : 6, 'd' : 7}
for key, value in input.items() :
    print(key, ' : ', value ** 2)
# a  :  25
# b  :  16
# c  :  36
# d  :  49
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3). Write a Python program to move items from dict1 to dict2.
# Input :
# dict1 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}
# dict2 = {}
# Output :
# dict1 ={}
# dict2 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}

dict1 = {'name' : 'john', 'city' : 'Landon', 'country' : 'UK'}
dict2 = {}
dict3 = dict1.copy()
for val in dict3 :
    temp = dict1.pop(val)
    dict2[val] = temp
print("dict1 :", dict1)
print("dict2 :", dict2)
# dict1 : {}
# dict2 : {'name': 'john', 'city': 'Landon', 'country': 'UK'}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4). Write a Python program to concatenate two dictionaries
# Input :
# dict1 = {'Name': 'Harry', 'Rollno':345, 'Address': 'Jordan'}
# dict2 = {'Age' : 25, 'salary': '$25k'}
# Output :
# dict1 :{'Name': 'Harry', 'Rollno':345, 'Address': 'Jordan', 'Age' : 25, 'salary': '$25k'}

dict1 = {'Name' : 'Harry', 'Rollno' : 345, 'Address' : 'Jordan'}
dict2 = {'Age' : 25, 'salary' : '$25k'}
dict1.update(dict2)
print("Dictionaries after concat :", dict1)
# Dictionaries after concat : {'Name': 'Harry', 'Rollno': 345, 'Address': 'Jordan', 'Age': 25, 'salary': '$25k'}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5). Write a Python program to get a list of odd and even keys from dict.
# Input :
# {1: 25, 5:'abc', 8:'pqr', 21:'xyz', 12:'def', 2:'utv'}
# Output :
# Even Key : [[8, 'pqr'], [12, 'def'], [2, 'utv']]
# Odd Key : [[1, 25], [5, 'abc'], [21, 'xyz']]
dict1 = {1 : 25, 5 : 'abc', 8 : 'pqr', 21 : 'xyz', 12 : 'def', 2 : 'utv'}
even = []
odd = []
for key, value in dict1.items() :
    if key % 2 == 0 :
        even.append([key, value])
    else :
        odd.append([key, value])
print("Even list : ", even)
print("Odd list : ", odd)
# Even list :  [[8, 'pqr'], [12, 'def'], [2, 'utv']]
# Odd list :  [[1, 25], [5, 'abc'], [21, 'xyz']]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6). Write a Python Program to create a dictionary from two lists
# Input :
# list1 = ['a', 'b', 'c', 'd', 'e']
# list2 = [12, 23, 24, 25, 15, 16]
# Output :
# {'a': 12, 'b': 23, 'c': 24, 'd': 25, 'e': 15}

list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [12, 23, 24, 25, 15, 16]
output = {}
for i in range(len(list1)) :
    output[list1[i]] = list2[i]
print("Dictionary : ", output)
# Dictionary :  {'a': 12, 'b': 23, 'c': 24, 'd': 25, 'e': 15}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 7). Write a Python program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
# Input : [4, 5, 6, 2, 1, 7, 11]
# Output : {4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}

input = [4, 5, 6, 2, 1, 7, 11]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 8). Write a Python program to clear all items from the dictionary.
dict1 = {1 : 25, 5 : 'abc', 8 : 'pqr', 21 : 'xyz', 12 : 'def', 2 : 'utv'}
dict1.clear()
print("dictionary after clear : ", dict1)
# dictionary after clear :  {}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 9). Write a Python program to remove duplicates values from Dictionary.
# Input : {'a': 12, 'b': 2, 'c': 12, 'd': 5, 'e': 35, 'f': 5}
# Output : {'a': 12, 'b': 2, 'd': 5, 'e': 35}

input = {'a': 12, 'b': 2, 'c': 12, 'd': 5, 'e': 35, 'f': 5}
output = {}
temp = []
for key, val in input.items() :
    if val not in temp :
        temp.append(val)
        output[key] = val
print("After removing duplicates :", output)
# After removing duplicates : {'a': 12, 'b': 2, 'd': 5, 'e': 35}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 10). Write a Python program to create a dictionary from the string.
# Input : 'SQATools'
# Output : {'S': 1, 'Q': 1, 'A': 1, 'T': 1, 'o': 2, 'l': 1, 's': 1}

input = 'SQATools'
output = {}
mid = ''
for val in input :
    if val not in mid :
        temp = input.count(val)
        mid = mid + val
        output[val] = temp
print('Output :', output)
# Output : {'S': 1, 'Q': 1, 'A': 1, 'T': 1, 'o': 2, 'l': 1, 's': 1}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 11). Write a python program to sort a dictionary in python using keys.
# Input = {'d' : 21, 'b' : 53,  'a': 13, 'c': 41}
# Output =
# ('a', 13)
# ('b', 53)
# ('c', 41)
# ('d', 21)

input = {'d' : 21,'b' : 53,'a': 13,'c': 41}
keylist = []
output = {}
for key in input :
    keylist.append(key)
keylist.sort()
print('After sorting dictionary according to keys : ')
for key in keylist :
    temp = input[key]
    print((key, temp))
# After sorting dictionary according to keys :
# ('a', 13)
# ('b', 53)
# ('c', 41)
# ('d', 21)
----------------------------------------------------------------------------------------------------
12). Write a python program to sort a dictionary in python using values.
Input = {'d' : 14, 'b' : 52,  'a': 13, 'c': 1 }
Output= (c, 1) (a,13) (d, 14) (b, 52)

input = {'d' : 21,'b' : 53,'a': 13,'c': 41}
sortval = sorted(input.values())
output = {}
for i in sortval :
    for k in input.keys() :
        if input[k] == i :
            output[k] = input[k]
            break
print('After sorting dictionary according to values : ', output)
# After sorting dictionary according to values :  {'a': 13, 'd': 21, 'c': 41, 'b': 53}
----------------------------------------------------------------------------------------------------
13). Write a python program to add a key in a dictionary.
Input= {1:'a', 2:'b'}
Output= (1:'a', 2:'b', 3:'c'}

input = {1:'a', 2:'b'}
input[3] = 'c'
print('After adding key :', input)
# After adding key : {1: 'a', 2: 'b', 3: 'c'}
-----------------------------------------------------------------------------------------------------
14). Write a program to concatenate two dictionaries
Input:
D1 = {'name' : 'yash', 'city' :  'pune'}
D1 = {'course' : 'python', 'institute' : 'sqatools'}
Output = { 'name' : 'yash', city: 'pune', 'course' : 'python', 'institute' : 'sqatools' }

d1 = {'name':'yash','city':'pune'}
d2 = {'course':'python','institute':'sqatools'}
d1.update(d2)
print('After concatenating 2 dictionaries :', d1)
# After concatenating 2 dictionaries : {'name': 'yash', 'city': 'pune', 'course': 'python', 'institute': 'sqatools'}
-------------------------------------------------------------------------------------------------------
15). Write a program to swap the values of the keys in the dictionary.
Input = {name:'yash', city: 'pune'}
Output={name:'pune', city: 'yash'}

input = {'name':'yash','city':'pune'}
list1 = []
list2 = []
for key, values in input.items() :
    list1.append(key)
    list2.append(values)

output = {}
output[list1[0]] = list2[1]
output[list1[1]] = list1[0]
print('After swapping values :', output)
# After swapping values : {'name': 'pune', 'city': 'name'}
------------------------------------------------------------------------------------------------------
16). Write a program to get the sum of all the items in a dictionary.
Input = {'x' : 23, 'y' : 10 , 'z' : 7}
Output = 40

input = {'x':23,'y':10,'z':7}
list1 = []
for value in input.values() :
    list1.append(value)
suma = sum(list1)
print('sum of values of items of dictionary :', suma)
# sum of values of items of dictionary : 40
----------------------------------------------------------------------------------------------------
17). Write a program to get the size of a dictionary in python.
Hint : use sys.getsizeof(var) method.
Input = {'name' : 'virat', 'sport' : 'cricket'}
Output = 216bytes
-----------------------------------------------------------------------------------------------------
18). Write a program to check whether a key exists in the dictionary or not.
Input:
Dict1 = {city:'pune', state='maharashtra'}
Dict1[country]
Output= 'key does not exist in dictionary'

dict1 = {'city':'pune','state':'maharashtra'}
key = 'country'
if key in dict1 :
    print('Key exist in dictionary')
else :
    print('Key does not exist in dictionary')
# Key does not exist in dictionary
----------------------------------------------------------------------------------------------------
19). Write a program to iterate over a dictionary.
Input :
Dict1 = {food:'burger', type:'fast food'}
Output :
food : burger
type : fast food

dict1 = {'food':'burger','type':'fast food'}
for key in dict1 :
    print(key, ':', dict1[key])
# food : burger
# type : fast food
----------------------------------------------------------------------------------------------------
20). Write a program to create a dictionary in the form of (n^3) i.e. if key=2 value=8
Input: n=4
Output ={1 : 1, 2 : 8, 3 : 27, 4 : 64}

input = 4
dict1 = {}
for i in range(1,input+1,1) :
    dict1[i] = i ** 3
print('Dictionary :', dict1)
# Dictionary : {1: 1, 2: 8, 3: 27, 4: 64}
-----------------------------------------------------------------------------------------------------
21). Write a program to give a class based on marks by using a dictionary.
Input = {'marks' : [30, 50, 70, 90,  100], class: ['D', 'C', 'B', 'A', 'A+']}
marks = 90
Output:
class: A

input = {'marks' : [30, 50, 70, 90, 100],'class': ['D','C','B','A','A+']}
marks = 90
ind = input['marks'].index(marks)
print('class :', input['class'][ind])
# class : A
----------------------------------------------------------------------------------------------------
22). Write a program to insert a key at the beginning of the dictionary.
Input = { 'course' : 'python',  'institute' : 'sqatools' }
Insert : ( 'name' : 'omkar' )
Output= { 'name' : 'omkar', 'course' : 'python', 'institute' : 'sqatools'}

input = { 'course':'python','institute':'sqatools'}
insert = {'name':'omkar'}
output = insert.update(input)
print('After inserting at beginning :', insert)
# After inserting at beginning : {'name': 'omkar', 'course': 'python', 'institute': 'sqatools'}
----------------------------------------------------------------------------------------------------
23). Write a program to create a dictionary where keys are between 1 and 5 and
     values are squares of the keys.
Output = {1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25}

dict1 = {}
for i in range(1,6,1) :
    dict1[i] = i ** 2
print('Required dictionary :', dict1)
# Required dictionary : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
----------------------------------------------------------------------------------------------------
24). Write a program to multiply all the items in the dictionary.
Input = { 'a' : 2, 'b' : 4, 'c' : 5}
Output = 40

input = {'a':2,'b':4,'c':5}
list1 = input.values()
mul = 1
for val in list1 :
    mul *= val
print('Multiplcation of values in the dictionary :', mul)
# Multiplcation of values in the dictionary : 40
----------------------------------------------------------------------------------------------------
25). Write a program to remove a key from dictionary.
Input = {a:2,b:4,c:5}
Output = (a:1,b:4}

input = {'a':2,'b':4,'c':5}
input.pop('c')
print('After removing key from dictionary :', input)
# After removing key from dictionary : {'a': 2, 'b': 4}
----------------------------------------------------------------------------------------------------
26). Write a program to map two lists into a dictionary.
Input :
a = [ 'name', 'sport', 'rank', 'age']
b = ['Virat', 'cricket', 1,  32]
Output =  { 'name' : 'virat', 'sport' : 'cricket', 'rank': 1, 'age' : 32}

a = ['name','sport','rank','age']
b = ['Virat', 'cricket', 1, 32]
dict1 = {}
for i in range(len(a)) :
    dict1[a[i]] = b[i]
print(dict1)
# {'name': 'Virat', 'sport': 'cricket', 'rank': 1, 'age': 32}
------------------------------------------------------------------------------------------------------
27). Write a program to find maximum and minimum values in a dictionary.
Input :
Dict = { 'a' : 10, 'b' : 44 , 'c' : 60, 'd' : 25}
Output :
Maximum value: 60
Minimum value: 10

dict1 = {'a':10,'b':44,'c':60,'d':25}
list1 = dict1.values()
print('Maximum value from the dicitonary :', max(list1))
print('Minimum value from the dicitonary :', min(list1))
# Maximum value from the dicitonary : 60
# Minimum value from the dicitonary : 10
---------------------------------------------------------------------------------------------------
28). Write a program to group same items to dictionary values list.
Input :
list = [1,3,4,4,2,5,3,1,5,5,2,]
Output = {1 : [1, 1], 2 :[2, 2], 3 : [3, 3], 4 : [4, 4], 5 : [5, 5, 5]}

list1 = [1,3,4,4,2,5,3,1,5,5,2,]
dict1 = {}
for val in list1 :
    if val not in dict1 :
        dict1[val] = [val]
    else :
        dict1[val].append(val)
print('Output :', dict1)
# Output : {1: [1, 1], 3: [3, 3], 4: [4, 4], 2: [2, 2], 5: [5, 5, 5]}
----------------------------------------------------------------------------------------------------
29). Write a program to replace words in string using dictionary.
String = 'learning python at sqatools'
Dict = { 'at' : 'is', 'sqatools' : 'fun'}
Output = 'learning python is fun'

string = 'learning python at sqatools'
dict1 = {'at':'is','sqatools':'fun'}
mid = string.split(' ')
output = ''
for val in mid :
    if val == 'at' or val == 'sqatools' :
        output = output + ' ' + dict1[val]
    else :
        output = output + ' ' + val
print('After changing :', output)
# After changing :  learning python is fun
-------------------------------------------------------------------------------------------------------
30). Write a program to remove a word from the string if it is a key in a dictionary.
String = 'sqatools is best for learning python'
Dict = { 'best' : 2, 'learning' : 6}
Output = “sqatools is for python”

string = 'sqatools is best for learning python'
dict = {'best':2,'learning':6}
output = ''
mid = string.split(' ')
for val in mid :
    if val not in dict :
        output = output + ' ' + val
print('After removing values :', output)
# After removing values :  sqatools is for python
-----------------------------------------------------------------------------------------------------
31). Write a program to remove duplicate values from dictionary values.
Input:
Dict1 = { 'marks1' : [25, 24, 23], 'marks2' : [ 25, 14,19] }
Output= { 'marks1' : [24, 23], 'marks2' : [14,19] }

dict1 = {'marks1':[25,24,23],'marks2':[25,14,19]}
list1 = dict1['marks1']
list2 = dict1['marks2']
output = {}
for ch in list1 :
    if ch in list2 :
        list1.remove(ch)
        list2.remove(ch)
output['marks1'] = list1
output['marks2'] = list2
print('After removing duplicates :', output)
# After removing duplicates : {'marks1': [24, 23], 'marks2': [14, 19]}
----------------------------------------------------------------------------------------------------
32). Write a program to check whether a dictionary is empty or not.
Input:
Dict1 = {}
Output : Given dictionary is empty

dict1 = {}

if dict1 == {} :
    print('Dictionary is empty')
else :
    print('Dictionary is not empty')
# Dictionary is empty
----------------------------------------------------------------------------------------------------
33). Write a program to add two dictionaries if keys are same then add their value.
Input:
Dict1 = { 'x':10, 'y':20, 'c':50, 'f':44 }
Dict2 = { 'x':60, 'c':25 }
Output = (x:70, y:20, c:75, f:44)

dict1 = {'x':10,'y':20,'c':50,'f':44}
dict2 = {'x':60,'c':25}
output = {}
for key1 in dict1 :
    if key1 in dict2 :
        output[key1] = dict1[key1] + dict2[key1]
    else :
        output[key1] = dict1[key1]
print('After adding values :', output)
# After adding values : {'x': 70, 'y': 20, 'c': 75, 'f': 44}
-----------------------------------------------------------------------------------------------------
34). Write a program to print all the unique values in a dictionary.
Input :
dict1 = [{'name1':'robert'},{'name2':'john'}, {'name3':'jim'}, {'name4':'robert'}]
Output = ['robert', 'john', 'jim']

listdict = [{'name1':'robert'},{'name2':'john'}, {'name3':'jim'}, {'name4':'robert'}]
mid = []
list1 = ['robert','john','jim']
for val in listdict :
     for value in val.values() :
         mid.append(value)
output = list(set(mid))
print('Unique elements :', output)
# Unique elements : ['robert', 'jim', 'john']
-----------------------------------------------------------------------------------------------------
35). Write a program to display different combinations of letters from dictionary values.
Input:
Dict1 = { x:[e,f], y:[a,b]}
Output:
  ea
  eb
  fa
  fb

dict1 = {'x':['e','f'],'y':['a','b']}
for a in dict1['x'] :
    for b in dict1['y'] :
        print(a+b)
# ea
# eb
# fa
# fb
----------------------------------------------------------------------------------------------------
36). Write a program to create a dictionary from a string.
Input = 'sqatools'
Output = {s:2,q:1,a:1, t:1,o:2, l:1}

input = 'sqatools'
mid = ''
output = {}
for ch in input :
    if ch not in mid :
        output[ch] = input.count(ch)
        mid += ch
print('Dictionary from string :', output)
# Dictionary from string : {'s': 2, 'q': 1, 'a': 1, 't': 1, 'o': 2, 'l': 1}
----------------------------------------------------------------------------------------------------
37). Write a program to print the given dictionary in the form of tables.
Input:
Dict1= {names:['virat','messi','kobe'], sport:['cricket','football','basketball']}
Output:
Names  sport
Virat      cricket
Messi    football
Kobe     basketball

dict1= {'names':['virat','messi','kobe'],'sport':['cricket','football','basketball']}
list1 = dict1['names']
list2 = dict1['sport']
print('names\t\tsports')
for i in range(len(list1)) :
    print(list1[i],'\t\t',list2[i])
# names		sports
# virat 	cricket
# messi 	football
# kobe 		basketball
-----------------------------------------------------------------------------------------------------
38). Write a program to count frequencies in a list using dictionary.
Input:
list1= [2,5,8,1,2,6,8,5]
Output = {1:1,2:2, 5:2, 6:1, 8:2}

list1= [2,5,8,1,2,6,8,5]
mid = []
output = {}
for val in list1 :
    if val not in mid :
        output[val] = list1.count(val)
        mid.append(val)
print('Output :', output)
# Output : {2: 2, 5: 2, 8: 2, 1: 1, 6: 1}
---------------------------------------------------------------------------------------------------
39). Write a program to find mean of values of keys in a dictionary.
Input :
Dict1= {m1:25, m2:20, m3:15}
Output :
Mean is 20

dict1= {'m1':25,'m2':20,'m3':15}
list1 = dict1.values()
output = sum(list1) // len(list1)
print('Mean of the dictionary values :', output)
# Mean of the dictionary values : 20
----------------------------------------------------------------------------------------------------
40). Write a program to convert a list into a nested dictionary of keys.      --> need to understand
Input = [a,b,c,d]
Output = {a: {b: {c: {d: {}}}}}

input = ['a','b','c','d']
output = temp = {}
for val in input :
    temp[val] = {}
    temp = temp[val]
print('Nested dictionary :', output)
------------------------------------------------------------------------------------------------------
41). Write a program to sort a list alphabetically in a dictionary.
Input= { a1 : [1,5,3], a2 : [10,6,20] }
Output= ( a1 : [1,3,5], a2 : [6,10,20] }

input = {'a1':[1,5,3],'a2':[10,6,20]}
for key in input :
    input[key].sort()
print('After sorting the list values :', input)
# After sorting the list values : {'a1': [1, 3, 5], 'a2': [6, 10, 20]}
----------------------------------------------------------------------------------------------------
42). Write a program to get a product with highest price from a dictionary.
Input = { 'price1' : 450, 'price2' : 600,  'price3' : 255,  'price4' : 400}
Output = P2 500

input = {'price1':450,'price2':600,'price3':255,'price4':400}
temp = 0
list1 = input.values()
max1 = max(list1)
for key, value in input.items() :
    if value == max1 :
        output = key
print('higesht priced product :', output)
# higesht priced product : price2
-----------------------------------------------------------------------------------------------------
43). Write a program to print a dictionary line by line.
Input = {'virat': {sport:'cricket', team:'india'}, 'messi': {sport:'football', team:'argentina'}}
Output=
Virat
Sport : cricket
Team : india

input = {'virat':{'sport':'cricket','team':'india'},'messi':{'sport':'football','team':'argentina'}}
for key, value in input.items() :
    print(key)
    for k, v in value.items() :
        print(k, ':', v)
    print()
# virat
# sport : cricket
# team : india

# messi
# sport : football
# team : argentina
-----------------------------------------------------------------------------------------------------
44). Write a program to convert a key value list dictionary into a list of list.
Input = {sqa:[1,4,6], tools:[3,6,9]}
Output= [[sqa,1,4,6],[tools,3,6,9]]

input1 = {'sqa':[1,4,6],'tools':[3,6,9]}
output = []
mid = []
for key in input1 :
    output.append([key, input1[key]])
print('Output :', output)
# Output : [['sqa', [1, 4, 6]], ['tools', [3, 6, 9]]]
---------------------------------------------------------------------------------------------------
45). Write a program to convert list of list into a form of dictionary.
Input= [[s,q,5,6],[a,t,1,2],[o,o,4,5],[l,s,7,8]]
Output= {(s,q) : (5,6), (a,t) : (1,2),  (o,o) : (4,5) , (l,s) : (7,8)}

input = [['s','q',5,6],['a','t',1,2],['o','o',4,5],['l','s',7,8]]

input= [['s','q',5,6],['a','t',1,2],['o','o',4,5],['l','s',7,8]]
dict1 = {}
for val in input:
    dict1[(val[0],val[1])] = (val[2], val[3])
print("Output :", dict1)
# Output : {('s', 'q'): (5, 6), ('a', 't'): (1, 2), ('o', 'o'): (4, 5), ('l', 's'): (7, 8)}
-------------------------------------------------------------------------------------------------
46). Write a program to convert list of dictionaries to list of lists.
Input= [{'sqa':123,'tools':456}]
Output= [[sqa,tools],[123,456]]

input= [{'sqa':123,'tools':456}]
list1 = []
for val in input:
    for key,value in val.items():
        temp = []
        temp.append(key)
        temp.append(value)
        list1.append(temp)
print('Output :', list1)
# Output : [['sqa', 123], ['tools', 456]]
--------------------------------------------------------------------------------------------------
47). Count number of items in a dictionary value that is in a list.
Input = {'virat':['match1',match2','match3'], 'rohit':['match1','match2']}
Output= 5

input = {'virat':['match1','match2','match3'], 'rohit':['match1','match2']}
cnt = 0
for key, value in input.items():
    cnt += len(value)
print('count :', cnt)
# count : 5
---------------------------------------------------------------------------------------------------
48). Write a Python program to sort items in a dictionary in descending order.
Input = {'Math':70, 'Physics':90, 'Chemistry':67}
Output = {'Physics':90, 'Maths':70, 'Chemistry':67}

input = {'Math':70, 'Physics':90, 'Chemistry':67}
list1 = []
for val in input.values():
    list1.append(val)

list1.sort()
output = {}
for val in list1:
    for key,value in input.items():
        if val == value:
            output[key] = val
print('Output :', output)
# Output : {'Chemistry': 67, 'Math': 70, 'Physics': 90}
-------------------------------------------------------------------------------------------------
49). Write a program to replace dictionary values with their average.
Input = { name:'ketan', subject:'maths', p1:80, p2:70}
Output = { name:'ketan',subject:'maths', p1+p2:75}

input = {'name':'ketan','subject':'maths','p1':80,'p2':70}
list1 = []
output = {}
for k1, v1 in input.items():
    if k1 == 'p1' or k1 == 'p2':
        list1.append(v1)
    else:
        output[k1] = v1
output['p1+p2'] = int(sum(list1)/len(list1))
print(output)
# {'name': 'ketan', 'subject': 'maths', 'p1+p2': 75}
-------------------------------------------------------------------------------------------------
50). Write a Python program to match key values in two dictionaries.
Input:
A = {'k1': p, 'k2': q, 'k3': r}
B = {'k1': p, 'k2': s}
Output = k1: p is present in both A and B

A = {'k1':'p','k2':'q','k3':'r'}
B = {'k1':'p','k2':'s'}

for k1,v1 in A.items():
    for k2,v2 in B.items():
        if k1 == k2 and v1 == v2:
            print(k1,':', v1, ' is present in both A and B')
# k1 : p  is present in both A and B
-------------------------------------------------------------------------------------------------
51). Write a Python program to create a dictionary of keys a, b, and c where each key has
as value a list from 1-5,6-10 and 11-15 respectively. Access the third value of each key
from the dictionary.
Input = { a: [1,2,3,4,5],  b: [6,7,8,9,10],  c: [11,12,13,14,15] }
Output = 3,8,13

input = {'a':[1,2,3,4,5],'b':[6,7,8,9,10],'c':[11,12,13,14,15]}
for val in input.values():
    print(val[2], end = ',')
# 3,8,13
-----------------------------------------------------------------------------------------------------
52). Write a python program to drop empty Items from a given dictionary.
Input = {m1:40, m2:50, m3:None}
Output = {m1:40,m2:50}

input = {'m1':40,'m2':50,'m3':None}
output = {}
for key,value in input.items():
    if value != None:
        output[key] = value
print('Output :', output)
# Output : {'m1': 40, 'm2': 50}
----------------------------------------------------------------------------------------------------
53). Write a Python program to filter a dictionary based on values.
Input= { alex : 50,  john : 45, Robert : 30}
Output= value greater than 40
{alex:50, john:45}

input = {'alex':50,'john':45,'Robert':30}
output = {}
for key,value in input.items():
    if value > 40:
        output[key] = value
print('Output :', output)
# Output : {'alex': 50, 'john': 45}
-----------------------------------------------------------------------------------------------------
54). Write a program to convert key-values list to flat dictionary
Input = {'name': ['Apr', 'May', 'June'], 'month': [4, 5, 6]}
Output = {4: 'Apr', 5: 'May', 6: 'June'}

input = {'name':['Apr','May','June'],'month':[4, 5, 6]}
list1 = input['month']
list2 = input['name']
output = {}
for i in range(len(list1)):
    output[list1[i]] = list2[i]
print(output)
# {4: 'Apr', 5: 'May', 6: 'June'}
------------------------------------------------------------------------------------------------------
55). Write a program to convert a list of Tuples into dictionary
Input =  [(“mike”, 1), (“sarah”, 20), (“jim”, 16)]
Output = {“mike”:[1], “sarah”:[20], “jim”:[16] }

input = [('mike',1),('sarah',20),('jim',16)]
output = {}
for val in input:
    output[val[0]] = [val[1]]
print(output)
# {'mike': [1], 'sarah': [20], 'jim': [16]}
-----------------------------------------------------------------------------------------------------
56). Write a program to convert string to dictionary.
Input: str1= ” Jan = January; Feb = February; Mar = March”
Output: {' Jan ': ' January', ' Feb ': ' February', ' Mar ': ' March'}

str1= 'Jan = January; Feb = February; Mar = March'
output = {}
mid = str1.split(';')
for val in mid:
    temp = val.split('=')
    output[temp[0]] = temp[1]
print(output)
# {'Jan ': ' January', ' Feb ': ' February', ' Mar ': ' March'}
-----------------------------------------------------------------------------------------------------
57). Write a program to convert a matrix into dictionary.
Input = [[1,2,3],[4,5,6]]
Output= {1:[1,2,3],2:[4,5,6]}

input = [[1,2,3],[4,5,6]]
output = {}
for i in range(len(input)):
    output[i+1] = input[i]
print(output)
# {1: [1, 2, 3], 2: [4, 5, 6]}
---------------------------------------------------------------------------------------------------
58). Write a Python program to check all values are same in a dictionary.
Input : A={'virat':50, 'rohit':50, 'rahul':50, 'hardik':50}
Output : True

flag = True
A = {'virat':50,'rohit':50,'rahul':50,'hardik':50}
for key,value in A.items():
    if value != 50:
        flag = False
        break
print('Output :',flag)
# Output : True
-----------------------------------------------------------------------------------------------------
59). Write a Python program to create a dictionary grouping a sequence of key-value pairs
    into a dictionary of lists.
Input :
A= {'virat':50, 'rohit':40, 'virat':30, 'rohit':10}
Output = {'virat':[50,30],'rohit':[40,10]}

output = {}
A = {'virat':50,'rohit':40,'virat':30,'rohit':10}
for key,value in A.items():
    if key not in output:
        output[key] = [value]
    else:
        output[key].append(value)
print(output)
# Output = {'virat':[50,30],'rohit':[40,10]}
------------------------------------------------------------------------------------------------------
60). Write a Python program to split a given dictionary of lists into list of dictionaries.
Input :
A={ 't20' : [50,40,30,45], 'odi' : [70,10,0,65] }
Output :
[ {t20:50, odi:70} ,{t20:40, odi:10}, {t20:30, odi:0}, {t20:45, odi:65} ]

output = []
A = {'t20':[50,40,30,45],'odi':[70,10,0,65]}
for i in range(len(A['t20'])):
    temp = {}
    temp['t20'] = A['t20'][i]
    temp['odi'] = A['odi'][i]
    output.append(temp)
print(output)
# [{'t20': 50, 'odi': 70}, {'t20': 40, 'odi': 10}, {'t20': 30, 'odi': 0}, {'t20': 45, 'odi': 65}]
-------------------------------------------------------------------------------------------------
61). Write a Python program to remove a specified dictionary from a given list.
Input = [ { t20:50, odi:70 }, { t20:40, odi:10 }, { t20:30,odi:0 }, { t20:45, odi:65} ]
Remove 4th dictionary
Output=[ { t20:50, odi:70 }, { t20:40, odi:10 } ,{ t20:30, odi:0 } ]

input = [{'t20':50,'odi':70 },{'t20':40,'odi':10 },{'t20':30,'odi':0 },{'t20':45,'odi':65}]
cnt =  3
output = []
for i in range(len(input)):
    if i != cnt:
        output.append(input[i])
print(output)
# [{'t20': 50, 'odi': 70}, {'t20': 40, 'odi': 10}, {'t20': 30, 'odi': 0}]
----------------------------------------------------------------------------------------------------
62). Write a Python program to convert string values of a given dictionary, into integer/float
    datatypes.
Input :
A = [ { 'a': '30',  'b': '20', 'c: '10' } ]
B=  [ { 'a': '3.33', 'b': '20.50', 'c: '12.5' } ]
Output :
A = [ { 'a': 30, 'b': 20, 'c: 10 } ]
B = [ { 'a': 3.33, 'b': 20.50, 'c: 12.5 } ]

A = [{'a':'30','b':'20','c':'10'}]
B = [{'a':'3.33','b':'20.50','c':'12.5'}]
a = []
b = []
for val in A:
    temp = {}
    for k,v in val.items():
        temp[k] = int(v)
    a.append(temp)

for val in B:
    temp = {}
    for k,v in val.items():
        temp[k] = float(v)
    b.append(temp)
print('a :', a)
print('b :', b)
# a : [{'a': 30, 'b': 20, 'c': 10}]
# b : [{'a': 3.33, 'b': 20.5, 'c': 12.5}]
------------------------------------------------------------------------------------------------------
63).  A Python dictionary contains list as value. Write a Python program to clear the
    list values in the said dictionary.
Input={'virat':[50,30],'rohit':[40,10]}
Output= { 'virat': [], 'rohit': [] }

input={'virat':[50,30],'rohit':[40,10]}
for key in input:
    input[key].clear()
print(input)
# {'virat': [], 'rohit': []}
----------------------------------------------------------------------------------------------------
64). A Python dictionary contains list as value. Write a Python program to update
the list values in the said dictionary.
Input = { 'virat' : [ 50,30 ], 'rohit' : [ 40,10 ] }
Output={ 'virat' : [ 50, 30,100 ], 'rohit' : [ 40,10,78 ] }

input = {'virat':[50,30],'rohit':[40,10]}
for key in input:
    if key == 'virat':
        input[key].append(100)
    elif key == 'rohit':
        input[key].append(78)
print(input)
# {'virat': [50, 30, 100], 'rohit': [40, 10, 78]}
-----------------------------------------------------------------------------------------------------
65). Write a Python program to extract a list of values from a given list of dictionaries
Input:
A=[ { t20:50, odi:70 }, { t20:40, odi:10 }, { t20:30, odi:0 }, { t20:45, odi:65 } ]
Extract values for 'odi'
Output = [70,10,0,65]

A = [{'t20':50,'odi':70},{'t20':40,'odi':10},{'t20':30,'odi':0},{'t20':45,'odi':65}]
list1 = []
for val in A:
    for key in val:
        if key == 'odi':
            list1.append(val[key])
print(list1)
# [70, 10, 0, 65]
----------------------------------------------------------------------------------------------------
66). Write a Python program to find the length of a given dictionary values.
Input = { 1:'sqa', 2:'tools', 3:'python' }
Output= { 'sqa':3, 'tools':5, 'python':6 }

input = {1:'sqa',2:'tools',3:'python'}
output = {}
for value in input.values():
    output[value] = len(value)
print(output)
# {'sqa': 3, 'tools': 5, 'python': 6}
---------------------------------------------------------------------------------------------------
67). Write a program to get the depth of the dictionary
Input = {'a':1, 'b': {'c': {'d': {}}}}
Output : 4

input = {'a':1,'b':{'c':{'d':{}}}}
str1 = str(input)
cnt = 0
for i in str1:
    if i == "{":
        cnt += 1
print(cnt)
# 4
----------------------------------------------------------------------------------------------------------------------------
68). Write a program to create nested Dictionary using given List
Input = {'sqatools':8,'python':6} list=[1,2]
Output= { 1: { sqatools':8 }, 2:['python':6] }

input = {'sqatools':8,'python':6}
list1 = [1,2]
list_key = list(input.keys())
output = {}
for i in range(len(list1)):
    temp = {}
    temp[list_key[i]] = input[list_key[i]]
    output[list1[i]] = temp
print(output)
# {1: {'sqatools': 8}, 2: {'python': 6}}
--------------------------------------------------------------------------------------------------------------------------
69). Extract key's value, if key present in list and dictionary
Input:
A = ['sqatools','is','best']
B = {'sqatools':10}
Output = 10

A = ['sqatools','is','best']
B = {'sqatools':10}
for val in A:
    if val in B:
        print(B[val])
        break
# 10
--------------------------------------------------------------------------------------------------------------------------
70). Write a program to remove keys with values greater than n.
Input = { 'sqa':3, 'tools':5, 'python':7 }
n=6
Output = {'sqa':3,'tools':5}

input = {'sqa':3,'tools':5,'python':7 }
n = 6
output = {}
for key,value in input.items():
    if value < n:
        output[key] = value
print(output)
# {'sqa': 3, 'tools': 5}
-------------------------------------------------------------------------------------------------------------------------
71). Write a program to remove keys with substring values.
Input :
D1 = { 1:'sqatools is best', 2: 'for learning python'}
Substr = ['best',' excellent']
Output = { 2:  'for learning python' }

D1 = { 1:'sqatools is best', 2:'for learning python'}
Substr = ['best','excellent']
output = {}
for key,value in D1.items():
    temp = value.split(' ')
    flag = 1
    for val in temp:
        if val in Substr:
            flag = 0
    if flag == 1:
        output[key] = value
print(output)
# {2: 'for learning python'}
--------------------------------------------------------------------------------------------------------------------------
72). Write a Python program to access dictionary key's element by index.
Input :
Drinks = { pepsi:50, sprite:60, slice:55}
Output:
Pepsi
Sprite
Slice

drinks = {'pepsi':50,'sprite':60,'slice':55}
key = list(drinks.keys())
for i in range(len(key)):
    print(key[i])
# pepsi
# sprite
# slice
----------------------------------------------------------------------------------------------------------------------------
73). Write a Python program to filter even numbers from a given dictionary values.
Input = { 'a': [11, 4, 6, 15],  'b': [3, 8, 12],  'c': [5, 3, 10] }
Output = { 'a':[4,6], 'b':[8,12],  'c':[10] }

input = {'a':[11,4,6,15],'b':[3,8,12],'c':[5,3,10]}
output = {}
for key,value in input.items():
    temp = []
    for val in value:
        if val%2 != 0:
            temp.append(val)
    output[key] = temp
print(output)
# {'a': [11, 15], 'b': [3], 'c': [5, 3]}
------------------------------------------------------------------------------------------------------------------------
74). Write a program to find the specified number of maximum values in a given dictionary.
Input = { a:18, b:50, c:36, d:47, e:60 }
Find keys of first 2 max values from the dictionary
Output = [ e, b ]

output = []
input = {'a':18,'b':50,'c':36,'d':47,'e':60}
list1 = list(input.values())
list1.sort(reverse=True)
for key,value in input.items():
    if value == list1[0] or value == list1[1]:
        output.append(key)
print(output)
# ['b', 'e']
---------------------------------------------------------------------------------------------------------------------------
75). Write a program to find shortest list of values with the keys in a given dictionary.
Input = { 'a': [10, 12], 'b': [10],  'c': [10, 20, 30, 40], 'd': [20] }
Output = [ 'b', 'd' ]

input = {'a':[10,12],'b':[10],'c':[10,20,30,40],'d':[20]}
min = len(input['a'])
output = []
for key,value in input.items():
    if len(value) < min:
        min = len(value)

for key,value in input.items():
    if len(value) == min:
        output.append(key)
print(output)
# ['b', 'd']
--------------------------------------------------------------------------------------------------------------------------
76). Write a Python program to count the frequency in a given dictionary.
Input = { a:10, b:20, c:25, d:10, e:30, f:20 }
Output = { 10:2, 20:2, 25:1, 30:1}

input = {'a':10,'b':20,'c':25,'d':10,'e':30,'f':20}
list1 = list(input.values())
output = {}
mid = []
for val in list1:
    if val not in mid:
        output[val] = list1.count(val)
print(output)
# {10: 2, 20: 2, 25: 1, 30: 1}
------------------------------------------------------------------------------------------------------------------------
77). Write a Python program to create a key-value list pairings in a given dictionary
Input = { 1: ['Virat Kohli'], 2: ['Rohit Sharma'], 3: ['Hardik Pandya'] }
Output = [ { 1: 'Virat Kohli'}, {2: 'Rohit Sharma'}, {3: 'Hardik Pandya' } ]

input = {1:['Virat Kohli'],2:['Rohit Sharma'],3:['Hardik Pandya']}
output = []
for key, value in input.items():
    temp = {}
    val = str(value)[2:-2]
    temp[key] = val
    output.append(temp)
print(output)
# [{1: 'Virat Kohli'}, {2: 'Rohit Sharma'}, {3: 'Hardik Pandya'}]
----------------------------------------------------------------------------------------------------------------------------
78). Write a Python program to get the total length of all values of a given dictionary with string values.
Input = { 'virat':50,'Rohit':40,'Rahul':25 }
Output :
Total length: 6

input = {'virat':50,'Rohit':40,'Rahul':25}
list1 = list(input.values())
length = 0
for val in list1:
    length += len(str(val))
print('Total length :', length)
# Total length : 6
-------------------------------------------------------------------------------------------------------------------------
79). Write a Python program to group the elements of a given list based on the given function.
Hint : Function name: len()
Input = ['abc', 'defg', 'hijkl']
Output = { 3:['abc'],  4:['defg'], 5:['hijkl'] }

input = ['abc', 'defg','hijkl']
output = {}
for val in input:
    output[len(val)] = [val]
print(output)
# {3: ['abc'], 4: ['defg'], 5: ['hijkl']}
-------------------------------------------------------------------------------------------------
80). Write a program to retrieve the value of the nested key indicated by the given selector list from a dictionary or list.
Input = {'p1':{name:{first:lionel, last:messi}, team:[psg,argentina]}}
Output :
Messi
Argentina

input = {'p1':{'name':{'first':'lionel','last':'messi'},'team':['psg','argentina']}}
for k1, v1 in input.items():
    for k2, v2 in v1.items():
        if isinstance(v2, dict):
                print(v2['last'])
        else:
            print(v1['team'][1])
# messi
# argentina
---------------------------------------------------------------------------------------------------
81). Write a program to show dictionary with maximum count of pairs.
Input:
A = {name:1,age:2}
B = {name:1,age:2,course:3,institute:4}
Output:
2nd dictionary has maximum keys, 4

A = {'name':1,'age':2}
B = {'name':1,'age':2,'course':3,'institute':4}
if len(A) > len(B):
    print('1 st dictionary has maximum keys,', len(A))
else:
    print('2 nd dictionary has maximum keys,', len(B))
# 2 nd dictionary has maximum keys, 4
----------------------------------------------------------------------------------------------------
82). Write a program to Extract Unique values from dictionary values.
Input = { sqa:[1,2,5,6],tools:[3,8,9],is:[2,5,0],best:[3,6,8] }
Output = [0,1,2,3,5,6,8,9]

list1 = []
input = {'sqa':[1,2,5,6],'tools':[3,8,9],'is':[2,5,0],'best':[3,6,8]}
for k1, v1 in input.items():
    list1.extend(v1)
output = set(list1)
print('Output :', list(output))
# Output : [0, 1, 2, 3, 5, 6, 8, 9]
----------------------------------------------------------------------------------------------------
83). Write a program to show keys associated with values in dictionary
Input = { 'xyz':[20,40], abc:[10,20] }
Output = { 10:[abc], 20:[xyz, abc], 40:[xyz] }

input = {'xyz':[20,40],'abc':[10,20]}
output = {}
list1 = []
for k1, v1 in input.items():
    list1.extend(v1)
set1 = set(list1)
for k1, v1 in input.items():
    for val in set1:
        if val in v1 and val not in output:
            output[val] = [k1]
        elif val in v1:
            output[val].append(k1)
print(output)
# {40: ['xyz'], 20: ['xyz', 'abc'], 10: ['abc']}
--------------------------------------------------------------------------------------------------
84). Write a program to print anagrams together in Python using List and Dictionary
Input = [burger, pizza, fries, bread]
Output = 'burger pizza fries bread'

input = ['burger','pizza','fries','bread']
for val in input:
    print(val, end = ' ')
# burger pizza fries bread
-------------------------------------------------------------------------------------------------
85). Write a Python program to convert a list of dictionaries into a list of values
    corresponding to the specified key.
Input = [ { name:'jos',  age:30 }, { name:'david', age:25 }, { name:'virat', age:32 } ]
Output = [30, 25, 32]

input = [{'name':'jos','age':30 },{'name':'david','age':25 },{'name':'virat','age':32}]
list1 = []
for val in input:
    list1.append(val['age'])
print(list1)
# [30, 25, 32]
------------------------------------------------------------------------------------------------
86). Write a Python program to find all keys in the provided dictionary that have the given value.
Input = {'a': 19, 'b': 20, 'c': 21, 'd': 20}
value = 20
Output = ['b', 'd']

list1 = []
value = 20
input = {'a':19,'b':20,'c':21,'d':20}
for k1,v1 in input.items():
    if v1 == value:
        list1.append(k1)
print(list1)
# ['b', 'd']
----------------------------------------------------------------------------------------------------
87). Write a Python program to convert given a dictionary to a list of tuples.
Input = {'a': 19, 'b': 20, 'c': 21, 'd': 20}
Output =[ (a,19), (b,20), (c,21), (d,20) ]

input = {'a':19,'b':20,'c':21,'d':20}
list1 = []
for k1,v1 in input.items():
    list1.append((k1, v1))
print(list1)
# [('a', 19), ('b', 20), ('c', 21), ('d', 20)]
---------------------------------------------------------------------------------------------------
88). Write a Python program to create a flat list of all the keys in a flat dictionary.
Input = { 'sqa': [1,2,5,6], 'tools': [3,8,9], 'is': [2,5,0], 'best' : [3,6,8] }
Output = [ sqa, tools, is, best]

input = {'sqa':[1,2,5,6],'tools':[3,8,9],'is':[2,5,0],'best':[3,6,8]}
list1 = []
for key in input:
    list1.append(key)
print(list1)
# ['sqa', 'tools', 'is', 'best']
---------------------------------------------------------------------------------------------------\
89). Write a Python program to create a flat list of all the values in a flat dictionary.
Input = { sqa:1, tools:2, is:2, best:4 }
Output =[ 1,2,3,4 ]

input = {'sqa':1,'tools':2,'is':2,'best':4}
list1 = []
for k1,v1 in input.items():
    list1.append(v1)
print(list1)
# [1, 2, 2, 4]
----------------------------------------------------------------------------------------------------
90). Write a program to Initialize dictionary with default values
Name = [ ”Virat”, ”Rohit” ]
Defaults = { 'sport' : 'cricket', 'salary' : 100000 }
Output = { “Virat” : { sport: 'cricket', salary:100000 }, “Rohit”:{ sport: 'cricket', salary:10000}}

Name = ['Virat','Rohit']
Defaults = {'sport':'cricket','salary':100000}
output = {}
for val in Name:
    output[val] = Defaults
print(output)
# {'Virat': {'sport': 'cricket', 'salary': 100000}, 'Rohit': {'sport': 'cricket', 'salary': 100000}}
----------------------------------------------------------------------------------------------------
91). Write a program to delete a list of keys from a dictionary.
Input = { 'a': 19, 'b': 20, 'c': 21, 'd': 20, 'e': 50 }
Keys to be removed:  [ 'a', 'd', 'e' ]
Output = { 'b': 20, 'c': 21 }

input = {'a':19,'b':20,'c':21,'d':20,'e':50}
Keys_to_be_removed = ['a','d','e']
output = {}
for key,value in input.items():
    if key not in Keys_to_be_removed:
        output[key] = value
print(output)
# {'b': 20, 'c': 21}
----------------------------------------------------------------------------------------------------
92). Write a program to rename key of a dictionary
Input = { 'a': 19, 'b': 20, 'c': 21, 'd': 20}
Output = { 'a': 19, 'b': 20, 'c': 21, 'e': 20}

input = {'a':19,'b':20,'c':21,'d':20}
output = {}
for k1,v1 in input.items():
    if k1 == 'd':
        output['e'] = v1
    else:
        output[k1] = v1
print(output)
# {'a': 19, 'b': 20, 'c': 21, 'e': 20}
--------------------------------------------------------------------------------------------------
93). Write a program to Invert a given dictionary with non-unique hashable values.
Input = { 'alex':1, 'bob':2,' martin':1, 'robert':2 }
Output = { 1:['alex','marin'], 2:['bob','robert'] }

input = {'alex':1,'bob':2,'martin':1,'robert':2}
output = {}
for k1, v1 in input.items():
    if v1 in output:
        output[v1].append(k1)
    else:
        output[v1] = [k1]
print(output)
# {1: ['alex', 'martin'], 2: ['bob', 'robert']}
---------------------------------------------------------------------------------------------------
94). Write a program to Sort Dictionary by values summation
Input = { x:[1,5,6], y:[4,8,2], c:[3,9] }
Output = { c:12, x:12, y:14}

list1 = []
input = {'x':[1,5,6],'y':[4,8,2],'c':[3,9]}
for value in input.values():
    list1.append(sum(value))

list1.sort()
output = {}

for val in list1:
    for k1, v1 in input.items():
        if sum(v1) == val:
            output[k1] = sum(v1)
print(output)
# {'x': 12, 'c': 12, 'y': 14}
-----------------------------------------------------------------------------------------------------
95). Write a program to convert a dictionary into n sized dictionary.
Input = { a:1, b:2, c:3, d:4, e:5, f:6 }
N = 3
Output = [{ a:1, b:2, c:3 }, {d:4, e:5, f:6}]

input = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
N = 3
output =[]
temp = {}
cnt = 0
for k1,v1 in input.items():
   temp[k1] = v1
   if len(temp) == N:
       output.append(temp)
       temp = {}
print(output)
# [{'a': 1, 'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
----------------------------------------------------------------------------------------------------
96). Write a program to Sort dictionaries list by Key's Value list index    ------------> not solved
Input = [ { a:[ 6, 7, 8],  b:9, c : 10 }, { a : [4, 6, 9],  b: 16, c : 1 } ]
Key = a,  index=0
Output = [ { a : [4, 6, 9],  b: 16, c : 1}, {a: [ 6, 7, 8],  b:9, c : 10} ]

input = [{'a':[6,7,8],'b':9,'c':10},{'a':[4,6,9],'b':16,'c':1}]


---------------------------------------------------------------------------------------------------
97) Write a python program to reverse each string value in the dictionary
and add underscore before and after the values.
Input  = {“a” : “Python”, “b”: “Programming”, “c”: “Learning”}
Output = {“_a_”: “nythonP”, “_b_” : “grogramminP”, “_c_”: “gearninL”}

input = {'a':'Python','b':'Programming','c':'Learning'}
output = {}
for k1, v1 in input.items():
    temp_key = '_' + k1 + '_'
    temp_val = v1[::-1]
    output[temp_key] = temp_val
print(output)
# {'_a_': 'nohtyP', '_b_': 'gnimmargorP', '_c_': 'gninraeL'}
-----------------------------------------------------------------------------------------------------------------------
98). Write a python program to sum un-common data from dictionary list values.  -----> not solved
Input = { 'a' : [ 6, 7, 2, 8, 1], 'b' : [2, 3, 1, 6, 8, 10], 'd' : [1, 8, 2, 6, 9] }
Output : Sum of 7, 3, 10, 9 = 29

input = {'a':[ 6, 7, 2, 8, 1],'b':[2, 3, 1, 6, 8, 10],'d':[1, 8, 2, 6, 9]}
list1 = []
for value in input.values():
    for v in value:
        list1.append(v)
print(set(list1))
-----------------------------------------------------------------------------------------------------------------------
school = {
 'teacher': [ {'name':'tech1','email':'tech1@gmail.com','mobile':45678},
              {'name': 'tech2', 'email': 'tech2@gmail.com', 'mobile': 45665678},
              {'name': 'tech3', 'email': 'tech3@gmail.com', 'mobile': 456756548},       
              {'name': 'tech4', 'email': 'tech4@gmail.com', 'mobile': 456565478} ],

'student': [  {'name': 'stud1', 'email': 'stud1@gmail.com', 'mobile': 4567865999},
              {'name': 'stud1', 'email': 'stud12@gmail.com', 'mobile': 88888888},
              {'name': 'stud2', 'email': 'stud2@gmail.com', 'mobile': 45665678},
              {'name': 'stud3', 'email': 'stud3@gmail.com', 'mobile': 456756548},
              {'name': 'stud4', 'email': 'stud4@gmail.com', 'mobile': 123456789} ]
}

#99).  Write a python program to get mobile number stud4 from given school dictionary.
#Output = 123456789
for key,val in school.items():
    if key == 'student':
        for v1 in val:
            for k2,v2 in v1.items():
                if v1['name'] == 'stud4':
                    output = v1['mobile']
print(output)
# 123456789
---------------------------------------------------------------------------------------------------------------------------
100). Write a python program to get mobile numbers of same name student from given dictionary.

Student name : ‘stud1’
Output = [4567865999, 88888888]

output = []
for key,val in school.items():
    if key == 'student':
        for v1 in val:
            for k2,v2 in v1.items():
                if v1['name'] == 'stud1':
                    output.append(v1['mobile'])
                    break
print(output)
# [4567865999, 88888888]
----------------------------------------------------------------------------------------------------------------------------
'''