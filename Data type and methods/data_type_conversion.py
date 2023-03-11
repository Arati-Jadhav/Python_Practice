################################## Integer ##############################
"""
# 1)  int --> float : possible
num1 = 145325
output1 = float(num1)
print(output1, type(output1))
# 145325.0 <class 'float'>

num2 = 2356
output2 = float(num2)
print(output2, type(output2))
# 2356.0 <class 'float'>

# 2) int --> str : possible
num3 = 452
output3 = str(num3)
print(output3, type(output3))
# 452 <class 'str'>

print(output3[1])
# 5

num4 = 684315634891
output4 = str(num4)
print(output4, type(output4))
# 684315634891 <class 'str'>

# 3) int --> list : NOT possible
num5 = 652
output5 = list(num5)
print(output5, type(output5]))
# TypeError: 'int' object is not iterable

# 4) int --> tuple : NOT possible
num6 = 41578
output6 = tuple(num6)
print(output6, type(output6))
# TypeError: 'int' object is not iterable

# 5) int --> dictionary : NOT possible
num7 = 89658
output7 = dict(num7)
print(output7, type(output7))
# TypeError: 'int' object is not iterable

# 6) int --> set : NOT possible
num8 = 234567
output8 = set(num8)
print(output8, type(output8))
# TypeError: 'int' object is not iterable

############################## Float #####################################
# 1) float --> int : possible
num1 = 5682.586
output1 = int(num1)
print(output1, type(output1))
# 5682 <class 'int'>

num2 = 2342.234
output2 = int(num2)
print(output2, type(output2))
# 2342 <class 'int'>

# 2) float --> str : possible
num3 = 45.34
output3 = str(num2)
print(output3, type(num3))
# 45.34 <class 'fstr'>

num4 = 6582.25478
output4 = str(num4)
print(output4, type(output4))
# 6582.25478 <class 'str'>

# 3) float --> list : NOT possible
# 4) float --> tuple : NOT possible
# 5) float --> dict : NOT possible
# 6) float --> set : NOT possible
# 7) float --> boolean : NOT possible

################################### String #######################################

# 1) str --> int : possible
# case 1 : NOT possible when string has characters in it
str1 = 'python'
output1 = int(str1)
print(output1, type(output1))
# ValueError: invalid literal for int() with base 10: 'python'

# case 2 : possible when str contains only numbers
str2 = '1852412'
output2 = int(str2)
print(output2, type(output2))
# 1852412 <class 'int'>

# 3) str --> float : possibe when str contains only numbers
str3 = '23456.76542'
output3 = float(str3)
print(output3, type(output3))
# 23456.76542 <class 'float'>

# 4) str --> list : possible
str4 = 'python'
output4 = list(str4)
print(output4, type(output4))
# ['p', 'y', 't', 'h', 'o', 'n'] <class 'list'>

str5 = 'i am a boy'
output5 = list(str5)
print(output5, type(output5))
# ['i', ' ', 'a', 'm', ' ', 'a', ' ', 'b', 'o', 'y'] <class 'list'>

# 5) str --> tuple : possible
str6 = 'Good Morning'
output6 = tuple(str6)
print(output6, type(output6))
# ('G', 'o', 'o', 'd', ' ', 'M', 'o', 'r', 'n', 'i', 'n', 'g') <class 'tuple'>

str7 = 'amit vithal devadhe'
output7 = tuple(str7)
print(output7, type(output7))
# ('a', 'm', 'i', 't', ' ', 'v', 'i', 't', 'h', 'a', 'l', ' ', 'd', 'e', 'v', 'a', 'd', 'h', 'e') <class 'tuple'>

# 6) str --> dict : normal string conversion to dictionary is not possible
# if string follows proper dictionary format, then we can convert it into dictionary with "json" module
str8 = 'swapnil shelar'
output8 = dict(str8)
print(output8, type(output8))
# no output

import json
str9 = '{"name" : "vishal", "job" : "Data Engineer" }'
data  = json.loads(str9)
print(data, type(data))
# {'name': 'vishal', 'job': 'Data Engineer'} <class 'dict'>

str10 = '{"company" : "honda", "model" : "city"}'
data2 = json.loads(str10)
print(data2, type(data2))
# {'company': 'honda', 'model': 'city'} <class 'dict'>

print(data2['company'])
# honda

# 7) str --> set : possible
str11 = 'python programming'
output11 = set(str11)
print(output11, type(output11))
# {'i', 'y', 'p', ' ', 'a', 'm', 'h', 'r', 'o', 'n', 'g', 't'} <class 'set'>
str12 = 'amhi sagle python shikto'
output12 = set(str12)
print(output12, type(output12))
# {'i', 'e', 'l', 'h', 'm', 'k', 't', 'o', 's', ' ', 'a', 'n', 'g', 'p', 'y'} <class 'set'>

# 8) str --> boolean : NOT possible

################################## List ######################################
# 1)  list --> int : NOT possible

# 2) list --> float : NOT possible

# 3) list --> str : possible
list1 = ['amit', 4, 8.6]
output1 = str(list1)
print(output1, type(output1))
# ['amit', 4, 8.6] <class 'str'>

print(output1[4])
# i

# 4) list --> tuple : possible
list2 = [3, 5.5, 'asdf']
output2 = tuple(list2)
print(output2, type(output2))
# (3, 5.5, 'asdf') <class 'tuple'>

# 5) list --> dictionary : NOT possible directly (with json module like 'str --> dict')

# 6) list --> boolean : NOT possible

# 7) list --> set : possible
list3 = [4, 5.6, 'f']
output3 = set(list3)
print(output3, type(output3))
# {'f', 4, 5.6} <class 'set'>

######################################### Tuple #######################################
# List aur Tuple bhai bhai hai.

# 1) tuple --> int : NOT possible

# 2) tuple --> float : NOT possible

# 3) tuple --> str : possible
tup1 = (1, 2, 3)
output1 = str(tup1)
print(output1, type(output1))
# (1, 2, 3) <class 'str'>

tup2 = ('b', 'g', 'h')
output2 = str(tup2)
print(output2, type(output2))
# ('b', 'g', 'h') <class 'str'>

# 4) tuple --> list : possible
tup3 = (1, 2, 3)
output3 = list(tup3)
print(output3, type(output3))
# [1, 2, 3] <class 'list'>

tup4 = ('b', 'g', 'h')
output4 = list(tup4)
print(output4, type(output4))
# ['b', 'g', 'h'] <class 'list'>

# 5) tuple --> dictionary : NOT possible

# 6) tuple --> set : possible
tup5  = (4, 5, 6, 7, 8)
output5 = set(tup5)
print(output5, type(output5))
# {4, 5, 6, 7, 8} <class 'set'>

tup6 = (4, 5, 6.7, 'DJ')
output6 = set(tup6)
print(output6, type(output6))
# {'DJ', 4, 5, 6.7} <class 'set'>

# 7) tuple --> boolean : NOT possible

###################################### Dictionary #######################################
# 1) dict --> int : NOT possible

# 2) dict --> float : NOT possible

# 3) dict --> str : possible
dict1 = {"nana" : "ajoba" , "nani" : "aajji" }
output1 = str(dict1)
print(output1, type(output1))
# {'nana': 'ajoba', 'nani': 'aajji'} <class 'str'>

dict2 = {"appa" : "shelar", "sir" : "shinde"}
output2 = str(dict2)
print(output2, type(output2))
# {'appa': 'shelar', 'sir': 'shinde'} <class 'str'>

# 4) dict --> list : possible (only return keys as members)
dict3 = {"name" : "bravo", "surname" : "DJ"}
output3 = list(dict3)
print(output3, type(output3))
# ['name', 'surname'] <class 'list'>

dict4 = {"mithai" : "gulabjam", "namkeen" : "bakarvadi"}
output4 = list(dict4)
print(output4, type(output4))
# ['mithai', 'namkeen'] <class 'list'>

# 5) dict --> tuple : possible (only return keys as members)
dict6 = {"name" : "bravo", "surname" : "DJ"}
output6 = tuple(dict6)
print(output6, type(output6))
# ('name', 'surname') <class 'tuple'>

dict7 = {"mithai" : "gulabjam", "namkeen" : "bakarvadi"}
output7 = tuple(dict7)
print(output7, type(output7))
# ('mithai', 'namkeen') <class 'tuple'>

# 6) dict --> set : possible (only return keys as members)
dict8 =  {"name" : "bravo", "surname" : "DJ"}
output8 = set(dict8)
print(output8, type(output8))
# {'name', 'surname'} <class 'set'>

dict9 = {"mithai" : "gulabjam", "namkeen" : "bakarvadi"}
output9 = set(dict9)
print(output9, type(output9))
# {'mithai', 'namkeen'} <class 'set'>

# 7) dict --> boolean : NOT possible

############################################# Set ################################################
# 1) set --> int : NOT possible

# 2) set --> float : NOT possible
"""
# 3)  set --> str : possible
set1 = {1, 4, 'h', 5.7}
output1 = str(set1)
print(output1, type(output1))
# {'h', 1, 4, 5.7} <class 'str'>

set2 = {4, 6, 7, 7.9}
output2 = str(set2)
print(output2, type(output2))
# {4, 7, 6, 7.9} <class 'str'>

# 4) set --> list : possible
set3 = {4, 6, 7, 7.9}
output3 = list(set3)
print(output3, type(output3))
# [4, 7, 6, 7.9] <class 'list'>

set4 = {1, 4, 'h', 5.7}
output4 = list(set4)
print(output4, type(output4))
# [1, 'h', 4, 5.7] <class 'list'>

# 5) set --> tuple : possible
set5 = {4, 7, 8.7, 'amit hushar ahe'}
output5 = tuple(set5)
print(output5, type(output5))
# (8.7, 4, 'amit hushar ahe', 7) <class 'tuple'>

set6 = {'swapnil', 'vishal', 'vrunda'}
output6 = tuple(set6)
print(output6, type(output6))
# ('vishal', 'swapnil', 'vrunda') <class 'tuple'>

# 6) set --> dictionary : NOT possible

# 7) set --> boolean : NOT possible

############################################### boolean ########################################

# boolean to any data type conversion is not possible