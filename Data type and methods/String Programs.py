'''
# 1). Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string
str1 = "PythonProgramming"
print(str1[0 : 2] + str1[-2 : ])
# Pyng
-------------------------------------------------------------------------------------------------------------------------------------------------
# 2). Write a Python program that takes a list of words and returns the length of the longest one.
str1 = "My name is Amit Devadhe"
output = str1.split(" ")
leng = 0
lword = ""
for word in output :
    if len(word) > leng :
        leng = len(word)
        lword = word
    else :
        continue
print("Longest word from the string : ", lword)
# Longest word from the string :  Devadhe
------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3). Write a Python program to get a string made of 4 copies of the last two characters of a specified string
# (length must be at least 2).
str1 = "Programming"
print(str1[-2 : ] * 4)
# ngngngng
------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4). Write a Python program to reverse a string if its length is a multiple of 4.
str1 = "Programmings"
if len(str1) % 4 == 0 :
    output = reversed(str1)
    for char in output :
        print(char, end = "")
else :
    print("length is not divisible by 4")
# Programming
# length is not divisible by 4

# Programmings
# sgnimmargorP
--------------------------------------------------------------------------------------------------------------------------------------------
# 5). Write a Python program to count occurrences of a substring in a string.
str2 = "Python Training Technical Analysis Data Python"
list1 = []
for word in str2.split(" ") :
    if word not in list1 :
        print(word, " : ", str2.count(word))
        list1.append(word)
    else :
        continue
# Python  :  2
# Training  :  1
# Technical  :  1
# Analysis  :  1
# Data  :  1
-------------------------------------------------------------------------------------------------------------------------------------------------
# 6). Write a Python program to test whether a passed letter is a vowel or consonant.
list1 = ["a", "e", "i", "o", "u", "A", "E", "i", "O", "U"]
input2 = "PythoN"
for char in input2 :
    if char not in list1 :
        print("Consonent", end = " ")
    else :
        print("Vowel", end = " ")

# Consonent Consonent Consonent Consonent Vowel Consonent
---------------------------------------------------------------------------------------------------------------------------------------------------------------

# 7). Write a Python program to check given string is a palindrome.
str1 = "jahaj"
if str1 == str1[ : : -1] :
    print("Palindrome")
else :
    print("Not Palindrome")

# str1 = "jahaj"
# Palindrome
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 8) Find the longest and smallest word in the input string.
str1  = "My name is Amit Devadhe"
longest = ""
shortest = ""
shleng = len(str1)
loleng = 0
output = str1.split(" ")
for word in output :
    if len(word) <= shleng :
        shortest = word
        shleng = len(word)
    elif len(word) >= loleng :
        longest = word
        loleng = len(word)

print("Longest word : ", longest)
print("Shortest word : ", shortest)

# Longest word :  Devadhe
# Shortest word :  is
----------------------------------------------------------------------------------------------------------------------------------------
# 9). Print most simultaneously repeated characters in the input string.

count = 1
sim = ""
str1 = "devadhewwwwwwwwwwdevadhe"
for i in str1 :
    if count < str1.count(i) :
        count = str1.count(i)
        sim = sim + i
print("Most repeated character : ", sim)
# Most repeated character :  dw
----------------------------------------------------------------------------------------------------------------------------------------------------------------
# 10). Write a Python program to calculate the length of a string with loop logic.

str1 = "aditya"
cnt = 0
for i in str1 :
    cnt += 1
print(cnt)
# aditya
# 6
-------------------------------------------------------------------------------------------------------------------------------------------------------
11). Write a Python program to replace the second occurrence of any char with special character $.

Input = "Programming"
output = "Prog$am$in$"

temp = ""
str1 = "programming"

for i in range(len(str1)) :
    if str1[i] in temp :
        temp += "$"
    else :
        temp += str1[i]

print(temp)
# prog$am$in$
-----------------------------------------------------------------------------------------------------------------------------------------------------------
12). Write a Python program to get to swap the last character of two words in a given string.
Input = "Sql Tools"
Output = "Sqs Tooll"

str1 = "Sql Tools"
output = str1.split(" ")
print(output[0][0 : -1] + output[1][-1], "", output[1][0 : -1] + output[0][-1])
# Sqs  Tooll
----------------------------------------------------------------------------------------------------------------------------------------------------------
13). Write a Python program to exchange the first and last character of each word from the given string.
Input = "Its Online Learning"
Output = "stI enlino gearninL"

str2 = "Its Online Learning"
output = str2.split(" ")
for word in output :
    print(word[-1] + word[1 : -1] + word[0], end = " ")

# stI enlinO gearninL
---------------------------------------------------------------------------------------------------------------------------------------------------------
14). Write a Python program to count vowels from each word in the given string
   show as dictionary output.
Input = "We are Learning Python Codding"
output = {"We" : 1, "are" : 2, "Learning" : 3, "Python":1, "Codding"}

str1 = "We are Learning Python Coding"
dict1 = {}
vowels = "aeiou"
output = str1.split(" ")
for word in output :
    cnt = 0
    for i in range(len(word)) :
        if word[i] in vowels :
            cnt = cnt + 1
    dict1[word] = cnt
print(dict1)
# {'We': 1, 'are': 2, 'Learning': 3, 'Python': 1, 'Coding': 2}
--------------------------------------------------------------------------------------------------------------------------------------------------------------
15). Write a Python program to repeat vowels 3 times and consonants 2 times.
Input = "Sqa Tools Learning"
Ouput = "SSqqaaa TToooooollss LLeeeaaarrnniiinngg"

str1 = "Sqa Tools Learning"
temp = ""
vowels = "aeiou"
output = str1.split(" ")
for word in output :

    for i in range(len(word)) :
        if word[i] in vowels :
            temp = temp + word[i] * 3
        else :
            temp = temp + word[i] * 2
    temp = temp + " "
print(temp)
# SSqqaaa TToooooollss LLeeeaaarrnniiinngg
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
16). Write a Python program re-arrange the given string.
Input = "Cricket Plays Virat"
Output = "Virat Plays Cricket"

str1 = "Cricket Plays Virat"
output = str1.split(" ")
i = len(output)
while  i > 0:
    print(output[i-1], end = " ")
    i  = i - 1
# Virat Plays Cricket
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
17). Write a python program to get all the digits from the given string.
Input =
Sinak’s 1112 aim	is	to 1773	create	a	new	generation	of	people	who
understand 444	that	an	organisation’s 5324	success	or	failure	is
based	on	555 leadership	excellence	and	not	managerial
acumen

Output = [1112, 5324, 1773, 5324, 555]

list1 = []
str1 = "Sinak’s 1112 aim is to 1773 create a new generation of people who understand 444 that an organisation’s 5324 " \
            "success or failure is based on 555 leadership excellence and not managerial acumen"
output = str1.split(" ")
for word in output :
        if word.isnumeric() :
            list1.append(word)
print(list1)
# ['1112', '1773', '444', '5324', '555']
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
18). Write a Python program to replace the words "Java" with "Python" in the given string.
Input = "JAVA is Best programming Language in the Market"
Output = "Python is Best programming Language in the Market"

str1 = "JAVA is Best programming Language in the Market"
print(str1.replace("JAVA", "Python"))
# Python is Best programming Language in the Market
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
19). Write a Python program to get all the palimdrome words from the string.
Input = "Python efe language aakaa hellolleh"
output = ["efe", "aakaa", "hellolleh"]

list1 = []
str1 = "Python efe language aakaa hellolleh"
output = str1.split(" ")
for word in output :
    if (word == word[: : -1]) :
        list1.append(word)
print(list1)
# ['efe', 'aakaa', 'hellolleh']
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
20). Write a Python program to create string with given list of words.
input = ["There", "are", "Many", "Progamming", "Language"]
Output = There are many programming language.

list1 = ["There", "are", "Many", "Progamming", "Language"]
for word in list1 :
    print(word , end = " ")
# There are Many Progamming Language
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
21). Write a Python program to remove duplicate words from the string.

Input = "John jany sabi row John sabi"
output = "John jany sabi row"

str1 = "John jany sabi row John sabi"
output = str1.split(" ")
temp = ""
for word in output :
    if word in temp :
        continue
    else :
        temp =  temp + word + " "
print(temp)
# John jany sabi row
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
22). Write a Python to remove unwated characters from the given string.
Input = "Prog^ra*m#ming"
Output = "Programming"

temp = ""
spe = "`~!@#$%^&*"
str1 = "Prog^ra*m#ming"

for i in range(len(str1)) :
    if str1[i] in spe :
        continue
    else :
        temp += str1[i]
print(temp)
# Programming
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
23). Write a Python program to find longest capital letter word.
Input = "Learning PYTHON programming is FUN"
output = "PYTHON"

str1 = "Learning PYTHON programming is FUN"
max_len = 0
longe = ""
output = str1.split(" ")
for word in output :
    if word.isupper() :
        if max_len < len(word) :
            max_len = len(word)
            longe = word
print(longe)
# PYTHON
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
24). Write a Python program to get common words in given string.
Input String1 = "Very Good Morning, How are You"
Input String1 = "You are a Good student, keep it up"

Output = "Good are"

str1 = "Very Good Morning, How are You"
str2 = "You are a Good student, keep it up"
temp = ""
output1 = str1.split(" ")
output2 = str2.split(" ")
for word in output1 :
    if word in output2 :
        temp += word + " "
print(temp)
# Good are You
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
25). Write a Python program to find the smallest and largest word in a given string.
Input = "Learning is a part of life and we strive"
smallest = "a"
Longest = "Learning"

str1  = "Learning is a part of life and we strive"
longest = ""
shortest = ""
shleng = len(str1)
loleng = 0
output = str1.split(" ")
for word in output :
    if len(word) >= loleng:
        longest = word
        loleng = len(word)
    elif len(word) <= shleng :
        shortest = word
        shleng = len(word)

print("Longest word : ", longest)
print("Shortest word : ", shortest)

# Longest word :  Learning
# Shortest word :  a
--------------------------------------------------------------------------------------------------------
26). Check whether the given string is palindrome (similar) or not.
Input = sqatoolssqatools
Output = Given string is not palindrome

input = 'sqatoolssqatools'
palin = input[: : -1]
if input == palin :
    output = 'Given string is palindrome'
else :
    output = 'Given string is not palindrome'

print(output)
# Given string is not palindrome
-------------------------------------------------------------------------------------------------------
27). Reverse the words in a string.
Input= sqatools
Output= slootaqs

input = 'sqatools'
output = input[ : : -1]
print(output)
# slootaqs
-----------------------------------------------------------------------------------------------------
28). Write a program to calculate the length of a string.
Input= “python”
Output=5

input = 'python'
cnt = 0
for ch in input :
    cnt += 1
print('length of string is :', cnt)
# length of string is : 6
-----------------------------------------------------------------------------------------------------
29). Write a program to calculate frequency of each characters in a string|
Input = “sqatools”
Output = {‘s’:2, ‘q’:1, ‘a’: 1, ‘t’:1,‘o’:2, ‘l’:1, ‘s’:1}

input = 'sqatools'
mid = ''
output = {}
for ch in input :
    if ch not in mid :
        cnt = input.count(ch)
        mid += ch
        output[ch] = cnt
print(output)
# {'s': 2, 'q': 1, 'a': 1, 't': 1, 'o': 2, 'l': 1}
------------------------------------------------------------------------------------------------------
30). Write a program to combine two strings
Input:
A = ’abc’
B = ’def’
Output = abcdef

a = 'abc'
b = 'def'
output = a + b
print('Combined strings :', output)
# Combined strings : abcdef
---------------------------------------------------------------------------------------------------
31). Write a program to print characters at even places
Input = ‘sqatools’
Output = saol

input = 'sqatools'
output = ''
for i in range(len(input)) :
    if i % 2 == 0 :
        output += input[i]
print('Characteers at even places :', output)
# Characteers at even places : saol
---------------------------------------------------------------------------------------------------
32). Write a program to check if a string has a number or not
Input = ‘python1’
Output = ‘Given string has a number’

flag = 0
input = 'python1'
for ch in input :
    if ch.isnumeric() == True :
        flag = 1

if flag == 1 :
    print('Given string has number')
# Given string has number
-----------------------------------------------------------------------------------------------
33). Write a program to count number of vowels in a string
Input= ‘I am learning python’
Output= 6

input = 'I am learning python'
vow = 'AEIOUaeiou'
cnt = 0
for ch in input :
    if ch in vow :
        cnt += 1
print('Vowels in the string :', cnt)
# Vowels in the string : 6
----------------------------------------------------------------------------------------------------
34). Write a program to count number of consonants in a string.
Input= ‘sqltools’
Output= 6

input = 'sqltools'
vow = 'AEIOUaeiou'
cnt = 0
for ch in input :
    if ch not in vow :
        cnt += 1
print('Consonants in the string :', cnt)
# Consonants in the string : 6
---------------------------------------------------------------------------------------------------
35). Write a program to print characters at odd places in a string.
Input = ‘abcdefg’
Output = ‘bdf’

input = 'abcdefg'
output = ''
for i in range(len(input)) :
    if i % 2 != 0 :
        output += input[i]
print('Characteers at odd places :', output)
# Characteers at odd places : bdf
-----------------------------------------------------------------------------------------------------
36). Write a program to remove all duplicates char from a given string in python.
Input = ‘sqatools’
Output = ‘sqatol’

input = 'sqatools'
output = ''
for ch in input :
    if ch not in output :
        output += ch
print('String after removing duplicates :', output
# String after removing duplicates : sqatol
--------------------------------------------------------------------------------------------------
37). Write a program to check if a string has a special characters or not
Input = ‘python$$#sqatools’
Output =  ‘Given string has special characters’

flag = 0
input = 'python$$#sqatools'
spe = '!@#$%^&*'
for ch in input :
    if ch in spe :
        flag  = 1
        break
if flag == 1 :
    print('String has special characters')
else :
    print('String has no special characters')
# String has special characters
--------------------------------------------------------------------------------------------------
38). Write a program to exchange the first and last letters of the string
Input = We are learning python
Output = ne are learning pythoW

input = 'We are learning python'
output = input[-1] + input[1 : -1] + input[0]
print('Output :', output)
# Output : ne are learning pythoW
---------------------------------------------------------------------------------------------------
39). Write a program to convert all the characters in a string to Upper Case.
Input = ‘I live in pune’
Output = ‘I LIVE IN PUNE’

input = 'I live in pune'
output = ''
for ch in input :
    output += ch.upper()
print('Upper case :', output)
# Upper case : I LIVE IN PUNE
--------------------------------------------------------------------------------------------------
40). Write a program to remove a new-line a python
Input = ‘objectorientedprogramming\n’
Output = ‘Objectorientedprogramming’

input = 'objectorientedprogramming\n'
output = input[ :-1]
print('After removing newline :', output)
# After removing newline : objectorientedprogramming
--------------------------------------------------------------------------------------------------
41). Write a python program to split and join a string
Input =‘Hello world’
Output = [‘Hello’, ‘world’]
                 Hello-world

input = 'Hello World'
mid = input.split(' ')
output = '-'.join(mid)
print('After joining :', output)
# After joining : Hello-World
--------------------------------------------------------------------------------------------------
42). Write a program to print floating numbers up to 3 decimal places.
Input = 2.14652
Output= 2.146

input = 2.14652
mid = str(input).split('.')
output = mid[0] + '.' + mid[1][:3]
print('Upto 3 decimal places :', float(output))
# Upto 3 decimal places : 2.146
--------------------------------------------------------------------------------------------------
43). Write a program to convert numeric words to numbers.
Input = ‘five four three two one’
Output = 54321

input = 'five four three two one'
mid = input.split(' ')
output = ''
for ch in mid :
    if ch == 'one' :
        output += '1'
    if ch == 'two' :
        output += '2'
    if ch == 'three' :
        output += '3'
    if ch == 'four' :
        output += '4'
    if ch == 'five' :
        output += '5'
    if ch == 'six' :
        output += '6'
    if ch == 'seven' :
        output += '7'
    if ch == 'eight' :
        output += '8'
    if ch == 'nine' :
        output += '9'
    if ch == 'zero' :
        output += '0'
print('Number in digits :', int(output))
# Number in digits : 54321
----------------------------------------------------------------------------------------------------
43). Write a python program to find the location of a word in a string
Input word = ‘problems’
Input string = ‘ I am solving problems based on strings’
Output = 4

word = 'problems'
input = 'I am solving problems based on strings'
mid = input.split(' ')
ind = mid.index(word) + 1
print('Location of given word :', ind)
# Location of given word : 4
---------------------------------------------------------------------------------------------------
44). Write a program to count occurrences of a substring in a string.
Word = ‘food’
Input str = ‘ I want to eat fast food’
Occurrences output= 1

word = 'food'
input = 'I want to eat fast food'
fre = input.count(word)
print('Occurrence of given word is :', fre)
# Occurrence of given word is : 1

word2 = 'are'
input2 = 'We are learning Python, wow are you'
fre2 = input2.count(word2)
print('Occurrence of given word is :', fre2)
# Occurrence of given word is : 2
---------------------------------------------------------------------------------------------------
45). Write a python program to find the least frequent character in a string
Input =  ‘abcdabdggfhf’
Output = ‘c’

input = 'abcdabdggfhf'
fre = input.count(input[0])
for ch in input :
    temp = input.count(ch)
    if fre > temp :
        fre = temp
        output = ch
print('Least frequent character :', output)
# Least frequent character : c
-------------------------------------------------------------------------------------------------
46). Find words that are greater than the given length.
Ex length = 3
Input = ‘We are learning python’
Output – ‘learning python’

length = 3
output = ''
input = 'We are learning python'
for word in input.split(' ') :
    if len(word) > 3 :
        output = output + ' ' + word
print('Words having length greater than 3 :', output)
# Words having length greater than 3 :  learning python
-------------------------------------------------------------------------------------------------
47). Write a program to get the first 4 characters of a string
Input = ‘Sqatools’
Output = ‘sqat’

input = 'Sqatools'
output = input[0:4]
print('First 4 characters of the given string :', output)
# First 4 characters of the given string : Sqat
--------------------------------------------------------------------------------------------------
48). Write a Python program to get a string made of the first 2 and the last 2 chars
    from a given string.
Input = ‘Sqatools’
Output = ‘Sqls’

input = 'Sqatools'
output = input[0:2] + input[-2:]
print('String consist of first 2 and last 2 characters :', output)
# String consist of first 2 and last 2 characters : Sqls
-------------------------------------------------------------------------------------------------
49). Write a python program to print mirror images of the string.
Input = ‘Python’
Output = ‘nohtyp

input = 'python'
output = input[::-1]
print('Mirror image of the given string :', output)
# Mirror image of the given string : nohtyp
-------------------------------------------------------------------------------------------------
50). Write a python program to split strings on vowels
Input = ‘qwerty’
Output = ‘qw rty’

vow = 'aeiou'
output = ''
input = 'qwerty'
for ch in input :
    if ch in vow :
        output += ' '
    else :
        output += ch
print('Splitting on vowels :', output)
# Splitting on vowels : qw rty
------------------------------------------------------------------------------------------------
51). Write a python program to replace multiple words with certain words.
Input = “I’m learning python at Sqatools”
Replace python with SQA  and sqatools with TOOLS
Output = “I’m learning SQA at TOOLS “

input = 'I am learning python at Sqatools'
output = input.replace('python', 'SQA').replace('Sqatools', 'TOOLS')
print('After replacing :', output)
# After replacing : I am learning SQA at TOOLS
-------------------------------------------------------------------------------------------------
51). Write a python program to replace different characters in the string at once.
Input = ‘Sqatool python’
Replace a with 1,
Replace t with 2,
Replace o with 3
Output = ‘sq1233l py2h3n”

input = 'Sqatool python'
output = input.replace('a', '1').replace('t', '2').replace('o', '3')
print('After replacing :', output)
# After replacing : Sq1233l py2h3n
-------------------------------------------------------------------------------------------------
52). Write a python program to remove multiple empty spaces from a list of
Input = [‘Python’, ‘ ‘, ‘ ‘, ‘sqatools’,‘ ‘, ‘sql’]
Output = [‘Python’, ‘sqatools’, ‘sql’]

input = ['Python', ' ', ' ', 'sqatools',' ', 'sql']
output = []
for ch in input :
    if ch != ' ' :
        output.append(ch)
print('After removing spaces :', output)
# After removing spaces : ['Python', 'sqatools', 'sql']
---------------------------------------------------------------------------------------------------
53).  Write a python program to remove punctuations from a string
Input = ‘Sqatools : is best, for python’
Output = ‘Sqatools is best for python’

pun = ',.?:''"";!'
input = 'Sqatools : is best , for python'
output = ''
for ch in input.split(' ') :
    if ch not in pun :
        output = output + ' ' + ch
print('After removing punctuation :', output)
# After removing punctuation :  Sqatools is best for python
--------------------------------------------------------------------------------------------------
54).  Write a python program to find duplicate characters in a string
Input = “hello world”
Output = ‘lo'

input = 'hello world'
mid = ''
for ch in input :
    if input.count(ch) > 1 and ch not in mid :
        mid += ch
print('Duplicate characters :', mid)
# Duplicate characters : lo
---------------------------------------------------------------------------------------------------
55).  Write a python program to check whether the string is a subset of another string or not
Input str1 = “iamlearningpythonatsqatools”
str = ‘pystlmi’
Output = True

input = 'iamlearningpythonatsqatools'
str1 = 'pystlmi'
flag = 1
for ch in str1 :
    if ch not in input :
        flag = 0
        break
if flag == 1 :
    print('string is subset : True')
else :
    print('string is subset : False')
# string is subset : True
------------------------------------------------------------------------------------------------
56). Write a python program to sort a string
Input = ‘xyabkmp’
Output = ‘abkmpxy’

input = 'xyabkmp'
output = ''.join(sorted(input))
print('Sorted string :', output)
# Sorted string : abkmpxy
------------------------------------------------------------------------------------------------
57). Write a python program to generate a random binary string of a given length.
Input = 8
Output = 10001001

import random
input = 8
str1 = ''
for i in range(input) :
    str1 += str(random.randint(0,1))
print('Random binary string of given length is: ', str1)
# Random binary string of given length is:  01110000
--------------------------------------------------------------------------------------------------
58). Write a python program to check if the substring is present in the string or not
Input string= ‘I live in pune’
Substring= ‘I live‘
Output = ‘Yes’

input = 'I live in pune'
search = 'I live'
if search in input :
    print('Is substring present : Yes')
else:
    print('Is substring present : No')
# Is substring present : Yes
---------------------------------------------------------------------------------------------------
59). Write a program to find all substring frequencies in a string.
Input str1 = “abab”
Output = {‘a’: 2, ‘ab’: 2, ‘aba’: 1,‘abab’: 1, ‘b’: 2, ‘ba’: 1, ‘bab’: 1}

input = 'abab'
temp = [input[i:j] for i in range(len(input)) for j in range(i+1, len(input)+1)]
d = {}
for i in temp :
    d[i] = input.count(i)
print('Frequencies of substrings :', d)
# Frequencies of substrings : {'a': 2, 'ab': 2, 'aba': 1, 'abab': 1, 'b': 2, 'ba': 1, 'bab': 1}
----------------------------------------------------------------------------------------------------
60). Write a program to find the longest substring length of a given string.    ----> not solved
Input string = ‘sqatoolsssppy’
char=s
Output = 3

input = 'sqatoolsssppy'
char = 's'
for i in range(len(input)) :
    cnt = 1
    t = input.index(char)
    for j in range(len(input)):
----------------------------------------------------------------------------------------------------
61). Write a python program to print the index of the character in a string.
Input = ‘Sqatools’
Output = ‘The index of q is 1′

input = 'Sqatools'
temp = input.index('q')
print('Index of q is :', temp)
# Index of q is : 1
----------------------------------------------------------------------------------------------------
62). Write a program to strip trailing spaces from a string
Input = ‘    sqaltoolspythonfun     ‘
Output = ‘sqaltoolspythonfun‘

input = '    sqaltoolspythonfun     '
output = input.strip()
print('Output after stripping :', output)
# Output after stripping : sqaltoolspythonfun
----------------------------------------------------------------------------------------------------
63). Write a program to check whether a string contains all letters of alphabet or not.
Input = ‘abcdgjksoug’
Output = False

input = 'abcdgjksoug'
alpha = 'abcdefghijklmnopqrstuvwxyz'
for ch in alpha :
    if ch not in input :
        print('All alphabets are present : False')
        break
# All alphabets are present : False
----------------------------------------------------------------------------------------------------
64). Write a python program to convert a string into list of words.
Input = ‘learning python is fun’
Output = [learning, python, is, fun]

input = 'learning python is fun'
output = input.split(' ')
print('string convert into list of words :', output)
# string convert into list of words : ['learning', 'python', 'is', 'fun']
----------------------------------------------------------------------------------------------------
63). Write a python program to swap commas and dots in a string.
Input = sqa,tools.python
Output = sqa.tools,python

input = 'sqa,tools.python'
maketrans = input.maketrans
output = input.translate(maketrans(',.', '.,', '  '))
final = output.replace(',', ", ")
print('Final output :', final)
# Final output : sqa.tools, python
----------------------------------------------------------------------------------------------------
64). Write a python program to count and display the vowels in a string
Input = ‘welcome to Sqatools’
Output = 7

cnt = 0
vow = 'AEIOUaeiou'
input = 'welcome to Sqatools'
for ch in input :
    if ch in vow :
        cnt += 1
print('Count of vowels :', cnt)
# Count of vowels : 7
----------------------------------------------------------------------------------------------------
65). Write a Python program to split a string on the last occurrence of the delimiter.
Input = ‘l,e,a,r,n,I,n,g,p,y,t,h,o,n’
Output = [‘l,e,a,r,n,I,n,g,p,y,t,h,o ‘ ,‘n’]

input = 'l,e,a,r,n,I,n,g,p,y,t,h,o,n'
output = input.rsplit(',', 1)
print('Output after splitting on last occurrence of delimeter :', output)
# Output after splitting on last occurrence of delimeter : ['l,e,a,r,n,I,n,g,p,y,t,h,o', 'n']
---------------------------------------------------------------------------------------------------
66). Write a Python program to find the first repeated word in a given string.
Input = ‘ab bc ca ab bd’
Output = ‘ab’

from collections import Counter
input = 'ab bc ca ab bd'
words = input.split(' ')
dict1 = Counter(words)
for key in words :
    if dict1[key] > 1 :
        output = key
        break
print('First repeated string :', output)
# First repeated string : ab
---------------------------------------------------------------------------------------------------
67). Write a Python program to find the second most repeated word in a given string.
Input = ‘ab bc ac ab bd ac nk hj ac’
Output = ‘ab’

from collections import Counter
input = 'ab bc ac ab bd ac nk hj ac'
words = input.split(' ')
dict1 = Counter(words)
value = sorted(dict1.values(), reverse = True)
second = value[1]
for key,value in dict1.items() :
    if value == second :
        output = key
        break
print('Second most repeated word in string :', output)
# Second most repeated word in string : ab
----------------------------------------------------------------------------------------------------
68). Write a Python program to remove spaces from a given string.
Input = ‘python at sqatools’
Output = ‘pythonatsqatools’

input = 'python at sqatools'
mid = input.split(' ')
output = ''.join(mid)
print('After removing space :', output)
# After removing space : pythonatsqatools
----------------------------------------------------------------------------------------------------
70). Write a Python program to capitalize the first and last letters of each word of a given string.
Input = ‘this is my first program’
Output = ‘ThiS IS MY FirsT PrograM’

input = 'this is my first program'
mid = input.split(' ')
mid2 = []
for word in mid :
    mid2.append(word[0].upper() + word[1:-1] + word[-1].upper())
output = ' '.join(mid2)
print('After applying changes :', output)
# After applying changes : ThiS IS MY FirsT PrograM
----------------------------------------------------------------------------------------------------
71). Write a Python program to compute the sum of digits of a given string.
Input = ’12sqatools78′
Output = 18

input = '12sqatools78'
mid = []
for ch in input :
    if ch.isnumeric() == True :
        mid.append(int(ch))
output = sum(mid)
print('Sum of digits from the string :', output)
# Sum of digits from the string : 18
----------------------------------------------------------------------------------------------------
72). Write a Python program to remove leading zeros from an IP address.
Input = 289.03.02.054
Output = 289.3.2.54

input = '289.03.02.054'
output = ''
for i in range(len(input)) :
    if input[i-1] != '.' and input[i] != 0 :
        output += input[i]
print('After removing leading zeros :', output)
# After removing leading zeros : 289.3.2.54
-----------------------------------------------------------------------------------------------------
73). Write a Python program to find the maximum length of consecutive 0’s in a given binary string.
Input = '10001100000111'
Output = 5

input = '10001100000111'
output = max(map(len, input.split('1')))
print('Maximum length of consecutive zeros :', output)
# Maximum length of consecutive zeros : 5
----------------------------------------------------------------------------------------------------
74). Write a Python program to remove all consecutive duplicates of a given string.
Input = ‘xxxxy’
Output = ‘xy’

input = 'xxxxy'
mid = ''
for ch in input :
    if ch not in mid :
        mid += ch
print('After removing duplicates :', mid)
# After removing duplicates : xy
-----------------------------------------------------------------------------------------------------
75). Write a Python program to create two strings from a given string.
Create the first string using those character that occurs only once and create the
second string which consists of multi-time occurring characters in the second string.
Input = “aabbcceffgh”
Output str1 = ‘egh’
Output str2 = ‘abcf’

input = 'aabbcceffgh'
dict1 = {}
once = ''
fre = ''
for ch in input :
    if ch not in dict1 :
        dict1[ch] = input.count(ch)
for key, value in dict1.items() :
    if value == 1 :
        once += key
    else :
        fre += key
print('Ocurrence = 1 :', once)
print('Ocurrence > 1 :', fre)
# Ocurrence = 1 : egh
# Ocurrence > 1 : abcf
---------------------------------------------------------------------------------------------------
76). Write a Python program to create a string from two given strings
    concatenating uncommon characters of the said strings.
Input string :
s1 = ‘abcdefg’
s2 = ‘xyzabcd’
Output string : ‘efgxyz’

s1 = 'abcdefg'
s2 = 'xyzabcd'
output = ''
for ch in s1 :
    if ch not in s2 :
        output += ch
for ch in s2 :
    if ch not in s1 :
        output += ch
print('String from uncommon characters from both strings :', output)
# String from uncommon characters from both strings : efgxyz
---------------------------------------------------------------------------------------------------
77). Write a Python program to move all spaces to the front of a given string in a single traversal.
Input = ”     Sqatools python”
Output =Sqatools python

input = 'sqa tools python'
cnt = input.count(' ')
mid = input.replace(' ', '')
output = (' ' * cnt) + mid
print('After moving spaces to front :', output)
# After moving spaces to front :   sqatoolspython
----------------------------------------------------------------------------------------------------
78). Write a Python code to remove all characters except a specified character in a given string.
Input = “Sqatools python”
Remove all characters except S
Output = ‘S’

input = 'Sqatools python'
char = 'S'
output = input.strip('qatools python')
print('After removing remaining characters :', output)
# After removing remaining characters : S
---------------------------------------------------------------------------------------------------
79). Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.
Input = ‘@SqaTools.lin’
Output:
Special characters: 1
Uppercase characters: 2
Lowercase characters: 8

input = '@SqaTools.lin'
sp = 0
up = 0
lo = 0
nu = 0
spe = '!@#$%^&*'
for ch in input :
    if ch.isalpha() == True :
        if ch.isupper() == True :
            up += 1
        else :
            lo += 1
    elif ch.isnumeric() == True :
        nu += 1
    elif ch in spe :
        sp += 1
print('Special characters :', sp)
print('Uppercase letters : ', up)
print('Lowercase letters :', lo)
print('Numbers :', nu)
# Special characters : 1
# Uppercase letters :  2
# Lowercase letters : 9
# Numbers : 0
---------------------------------------------------------------------------------------------------
80). Write a Python program to count a number of non-empty substrings of a given string.
Input a string = ‘sqatools12’
Number of substrings = 55

input = 'abc'
leng = len(input)
output = int(leng * (leng + 1) / 2) + 1
print('Count of non empty substring : ', output)
# Count of non empty substring :  7
----------------------------------------------------------------------------------------------------
81). Write a Python program to find the smallest and largest word in a given string.
Original Strings = ‘Write a python program’
Smallest word = ‘a’
Largest word = ‘program’

str1 = 'Write a python program'
longest = ""
shortest = ""
shleng = len(str1)
loleng = 0
output = str1.split(" ")
for word in output :
    if len(word) <= shleng :
        shortest = word
        shleng = len(word)
    elif len(word) >= loleng :
        longest = word
        loleng = len(word)

print("Longest word : ", longest)
print("Shortest word : ", shortest)
# Longest word :  program
# Shortest word :  a
--------------------------------------------------------------------------------------------------
82). Write a Python program to find the index of a given string at which a given substring starts.
Input = ‘Sqatools python’
substr = 'python'
Output = 9

input = 'Sqatools python'
output = input.index('python')
print('Index of starting of substring :', output)
# Index of starting of substring : 9
---------------------------------------------------------------------------------------------------
83). Write a Python program to remove unwanted characters from a given string.
Input = ‘sqa****too^^{ls’
Output = ‘Sqatools’

output = ''
input = 'sqa****too^^{ls'
for ch in input :
   if ch.isalpha() == True :
       output += ch
print('After removing unwanted characters :', output)
# After removing unwanted characters : sqatools
---------------------------------------------------------------------------------------------------
84). Write a Python program to remove duplicate words from a given string.
Input = ‘learning python is fun learning’
Output = ‘learning python is fun’

input = 'learning python is fun learning'
mid = input.split(' ')
output = ''
for word in mid :
    if word not in output :
        output = output + ' ' + word
print('After removing duplicates :', output)
# After removing duplicates :  learning python is fun
----------------------------------------------------------------------------------------------------
85). Write a Python program to convert a given list into a string.
Input = [ ‘Sqatools’, ‘123’, ‘python’, ‘learning’, ‘blue’, ‘white’]
Output = ‘sqatools 123 python learning blue white’

input = [ 'Sqatools', '123', 'python', 'learning', 'blue', 'white']
output = ''
for word in input :
    output = output + ' ' + word
print('List converted into string : ', output)
# List converted into string :   Sqatools 123 python learning blue white
----------------------------------------------------------------------------------------------------
86). Write a Python program to find the string similarity between two given strings.
Input :
Str1 = ‘Learning is fun in Sqatools’
Str2 = ‘Sqatools Online Learning Platform’

Output :
Similarity : 2

input1 = 'Learning is fun in Sqatools'
input2 = 'Sqatools Online Learning Platform'
list1 = input1.split(' ')
list2 = input2.split(' ')
cnt = 0
for word in list1 :
    if word in list2 :
        cnt += 1
print('Similarity : ', cnt)
# Similarity :  2
----------------------------------------------------------------------------------------------------
87). Write a Python program to extract numbers from a given string.
Input = ‘python 456 self learning 89’
Output = [456, 89]

input = 'python 456 self learning 89'
mid = input.split(' ')
output = []
for word in mid :
    if word.isnumeric() == True :
        output.append(int(word))
print('Numbers from the string :', output)
# Numbers from the string : [456, 89]
----------------------------------------------------------------------------------------------------
88). Write a Python program to decapitalize the first letter of a given string.
Input = ‘Python’
Output = ‘python’

input = 'Python'
output = input.lower()
print('After decapitalizing first letter of the string :', output)
# After decapitalizing first letter of the string : python
---------------------------------------------------------------------------------------------------
89). Write a Python program to split a given multiline string into a list of lines
Input =”’This string Contains
Multiple
Lines”’
Output = [‘This string Contains’, ‘Multiple’, ‘Lines’]

input = """This string Contains 
Multiple 
Lines"""
output = input.splitlines()
print(output)
# ['This string Contains ', 'Multiple ', 'Lines']
----------------------------------------------------------------------------------------------------
90). Write a Python program to add two strings as they are numbers
Input :
a=’3′, b=’7′
Output  = ’10’

a='3'
b='7'
output = int(a) + int(b)
print('Output =', str(output))
# Output = 10
---------------------------------------------------------------------------------------------------
91). Write a Python program to extract and display the name from a given email address.
Input = ‘student.new@gmail.com‘
Output = ‘student’

input = 'student.new@gmail.com'
output = input.split('.')
print('Student name :', output[0])
# Student name : student
---------------------------------------------------------------------------------------------------
92). Write a Python program that counts the number of leap years within the range of years.
The range of years should be accepted as a string.
('1981-2001')  =  Total leap year 5
('2010-2021') = Total leap year 3

input1 = '1981-2001'
input2 = '2010-2021'
mid = input2.split('-')
start = int(mid[0])
end = int(mid[1])
cnt = 0
for i in range(start, end, 1) :
    if (i % 100 != 0) and (i % 4 == 0) or (i % 400 == 0):
        cnt += 1
print('Total leap year count :', cnt)

# input1 = '1981-2001'
# Total leap year count : 5

# input1 = '1981-2001'
# Total leap year count : 3
---------------------------------------------------------------------------------------------------
93). Write a Python program to insert space before every capital letter appears in a given word.
Input = ‘SqaTools pyThon’
Output= ‘ Sqa Tools py Thon’

input = 'SqaTools pyThon'
output = ''
for ch in input :
    if ch.isupper() == True :
        output += ' '
        output += ch
    else :
        output += ch
print('After giving space before capital letter :', output)
# After giving space before capital letter :  Sqa Tools py Thon
---------------------------------------------------------------------------------------------------
94). Write a Python program that takes a string and replaces all the characters with
    their respective numbers.
Input – “Python”
Output- “16 25 20 8 15 14”

input = 'Python'
dict1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12,
         'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22,
         'w':23, 'x':24, 'y':25, 'z':26}
output = ''
mid = input.lower()
for ch in mid :
    output = output + str(dict1[ch])
    output += ' '
print('After replacing wth numbers :', output)
# After replacing wth numbers : 16 25 20 8 15 14
----------------------------------------------------------------------------------------------------
95). Write a program to uppercase half string.
Input = ‘banana’
Output = ‘banANA’

input = 'banana'
output = ''
for i in range(len(input)) :
    if i >= len(input)//2 :
        output += input[i].upper()
    else :
        output += input[i]
print('After making last half capital :', output)
# After making last half capital : banANA
----------------------------------------------------------------------------------------------------
96). Write a program to split and join a string using.
Input = ‘Sqatools is best’
Output = ‘Sqatools-is-best’

input = 'Sqatools is best'
mid = input.split(' ')
output = '-'.join(mid)
print('After joining :', output)
# After joining : Sqatools-is-best
----------------------------------------------------------------------------------------------------
97). Write a python program to find permutations of a given string using in built function.
Input  = ‘CDE’
Output = [‘CDE’, ‘CED’ ‘EDC’, ‘ECD’, ‘DCE’, ‘DEC’]

input = 'CDE'
from itertools import permutations
per = permutations(input)
output = []
for p in list(per) :
    output.append(''.join(p))
print('All permutations :', output)
# All permutations : ['CDE', 'CED', 'DCE', 'DEC', 'ECD', 'EDC']
----------------------------------------------------------------------------------------------------
98). Write a program to slice a string to print the first 3 characters.
Input = ‘Sqatools’
Output = ‘Sqa’

input = 'Sqatools'
output = input[0:3]
print('First 3 characters of string :', output)
# First 3 characters of string : Sqa
----------------------------------------------------------------------------------------------------
99). Write a program to avoid spaces in string and get the total length
Input = ‘sqatools is best for learning python’
Output = 31

input = 'sqatools is best for learning python'
cnt = 0
for ch in input :
    if ch != ' ' :
        cnt += 1
print('Length after avoiding spaces :', cnt)
# Length after avoiding spaces : 31
----------------------------------------------------------------------------------------------------
100). Write a program to accept a string that contains only vowels
Input = ‘python’
Output- ‘not accepted’

Input = ‘aaieou’
Output = ‘accepted’

input1 = 'python'
input2 = 'aaieou'
flag  = 1
vow = 'aeiou'
for ch in input2 :
    if ch not in vow :
        flag = 0
        break
if flag == 1 :
    print('Accepted')
else :
    print('Not accepted')

# input1 = 'python'
# Not accepted

# input2 = 'aaeiou'
# Accepted
----------------------------------------------------------------------------------------------------
101). Write a program to remove the kth element from the string
K=2
Input = ‘sqatools’
Output = ‘sqtools’

input = 'sqatools'
k = 2
output = ''
for i in range(len(input)) :
    if i != (k+1) :
        output += input[i]
print('After removing k th element :', output)
# After removing k th element : sqaools
---------------------------------------------------------------------------------------------------
102). Write a program to check if a given string is binary or not.
Hint: Binary numbers only contain 0 or 1.

Input = ‘01011100’
Output = yes

input = '011010101'
flag = 1
c = '01'
for ch in input :
    if ch not in c:
        flag = 0
        break
if flag == 1 :
    print('yes')
else :
    print('no')
# yes
---------------------------------------------------------------------------------------------------
103). Write a program to convert a string into the dictionary.
Input = “Jan=January; Feb=February; Mar=March”
Output = {‘Jan’: ‘January’, ‘Feb’: ‘February’, ‘Mar’: ‘March’}

input = 'Jan=January;Feb=February;Mar=March'
mid = input.split(';')
outdict = {}
for word in mid :
    temp = word.split('=')
    outdict[temp[0]] = temp[1]
print('After converting string into dictionary :', outdict)
# After converting string into dictionary : {'Jan': 'January', 'Feb': 'February', 'Mar': 'March'}
-----------------------------------------------------------------------------------------------------
104). Write a program to get a string from a given string
where all occurrences of its first char have been changed to $ except the first char itself.
Input = ‘calculator’
Output = ‘cal$u$$tor’

input = 'calculator'
output = ''
for ch in input :
    if ch not in output :
        output += ch
    else :
        output += '$'
print('After applying chnages :', output)
# After applying chnages : cal$u$$tor
---------------------------------------------------------------------------------------------------
105). Write a program to add ing at the end of the string.
Input = ‘xyz’
Output = ‘xyzing’

input = 'xyz'
output = input + 'ing'
print('After adding ing :', output)
# After adding ing : xyzing
---------------------------------------------------------------------------------------------------
106). Write a program to add ly at the end of the string if the given string ends with ing
Input = ‘winning’
Output = ‘winningly’

input = 'winning'
output = ''
if input[-3::] == 'ing' :
    output = input + 'ly'
print('After applying changes :', output)
# After applying changes : winningly
--------------------------------------------------------------------------------------------------
107). Write a program to find a substring ‘good’ in a given string and replace it by ‘poor’
Input = ‘The movie was good’
Output = ‘The movie was bad’

input = 'The movie was good'
output = input.replace('good', 'poor')
print('After applying changes :', output)
# After applying changes : The movie was poor
---------------------------------------------------------------------------------------------------
108). Write a program to accept an answer from the user and display it in Upper and Lower case.
Input = ‘Which site is best for learning python?
Output1 = ‘SQATOOLS is the best site for learning python’
Output2 = ‘Sqatools is the best site for learning python’

answer = input('Which site is best for learning python?\n')
sen1 = answer.upper() + ' is the best site for learning python.'
sen2 = answer.lower() + ' is the best site for learning python.'
print('Uppercase answer :', sen1)
print('Lowercase answer :', sen2)
# Which site is best for learning python?
# sqatools
# Uppercase answer : SQATOOLS is the best site for learning python.
# Lowercase answer : sqatools is the best site for learning python.
---------------------------------------------------------------------------------------------------
109). Write a program to get a string made of 6 copies of the last two
    characters of a specified string.
Input = ‘sqatools’
Output = ‘lslslslslsls’

input = 'sqatools'
output = input[-2::] * 6
print('String made of 6 copies of last 2 characters of input string :', output)
# String made of 6 copies of last 2 characters of input string : lslslslslsls
---------------------------------------------------------------------------------------------------
110). Write a program to reverse words in a string.
Input = ‘string problems’
Output = ‘problems string’

input = 'string problems'
output = input.split(' ')[::-1]
for ch in output :
    print(ch, end = ' ')
# problems string
---------------------------------------------------------------------------------------------------
111). Write a program to print the index of each character in a string.
Input =  ‘sqatools’
Output :
Index of s is 0
Index of q is 1
Index of a is 2
Index of t is 3
Index of o is 4
Index of o is 5
Index of l is 6
Index of s is 7

input = 'sqatools'
for i in range(len(input)) :
    print('The index of ', input[i], ' is ', i)
# The index of  s  is  0
# The index of  q  is  1
# The index of  a  is  2
# The index of  t  is  3
# The index of  o  is  4
# The index of  o  is  5
# The index of  l  is  6
# The index of  s  is  7
---------------------------------------------------------------------------------------------------
112). Write a program to find the first repeated character in a string and its index.
Input = ‘sqatools’
Output = (o, 4)

input = 'sqatools'
output = ''
t = 0
c = ''
for ch in input :
    if ch in output :
        t = input.index(ch)
        c = c + ch
        break
    else :
        output = output + ch
print('Output :', (c, t))
# Output : ('o', 4)
-----------------------------------------------------------------------------------------------------
113). Write a program to swap cases of a given string.
Input = ‘Learning Python’
Output = ‘lEARNING pYTHON’

output = ''
input = 'Learning Python'
for ch in input :
    output = output + ch.swapcase()
print('After swapping case :', output)
# After swapping case : lEARNING pYTHON
----------------------------------------------------------------------------------------------------
114). Write a program to find common values that show in two given strings
Input:
str1 = ‘Version1.2.3’
str2 = ‘Version1.5.7’
Output=’Version1′

str1 = 'Version1.2.3'
str2 = 'Version1.5.7'
output = ''
for ch in str1 :
    if ch in str2 :
        output += ch
print('Common characters :', output)
# Common characters : Version1..
----------------------------------------------------------------------------------------------------
115). Write a program to remove repeated characters in a word of a string and \
        replace it with a single letter.
Input = ‘aabbccdd’
Output = ‘abcd’

input = 'aabbccdd'
output = ''
for i in range(len(input)-1) :
    if input[i] != input[i+1] :
        output += input[i]
output = output + input[-1]
print('After removing duplicates values :', output)
# After removing duplicates values : abcd
--------------------------------------------------------------------------------------------------
116). Write a program to print a string 3 times.
Input = ‘sqatools’
Output = ‘sqatoolssqatoolssqatools’

input = 'sqatools'
output = input * 3
print('Print string 3 times :', output)
# Print string 3 times : sqatoolssqatoolssqatools
---------------------------------------------------------------------------------------------------
117). Write a program to print each character of a string on a new line.
Input = ‘python’
Output:
p
y
t
h
o
n

input = 'python'
for ch in input :
    print(ch)
# p
# y
# t
# h
# o
# n
----------------------------------------------------------------------------------------------------
118). Write a program to generate a password using a string.
Example Output=’Abnd@#4125hh’

import random
import string
chara = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chara) for i in range(8))
print('Random password :', password)
# Random password : 6Lw)`s}3
---------------------------------------------------------------------------------------------------
119). Write a program to move each character in a string to 3 indices to the right. --> not solved
Input = ‘python is easy to learn’
Output = ‘earnpy th onis ea sytol’

input =
----------------------------------------------------------------------------------------------------
120). Write a python program to get all the email id’s from given string.
Input str = “”” We have some employee whos john@gmail.com email id’s are randomly distributed
jay@lic.com we want to get hari@facebook.com all the email mery@hotmail.com
id’s from this given string.“””
Output = [‘john@gmail.com‘, ‘ jay@lic.com‘, ‘hari@facebook.com‘, ‘mery@hotmail.com‘ ]

input = """We have some employee whos john@gmail.com email id’s are randomly distributed jay@lic.com we want to get hari@facebook.com all the email mery@hotmail.com id’s from this given string."""
mid = input.split(' ')
output = []
for ch in mid :
    if '@' in ch :
        output.append(ch)
print('Only emails :', output)
# Only emails : ['john@gmail.com', 'jay@lic.com', 'hari@facebook.com', 'mery@hotmail.com']
-----------------------------------------------------------------------------------------------------
121). Write a python program to get a list of all the mobile numbers from the given string.
Input str = “”” We have 2233 some employee 8988858683 whos 3455 mobile numbers are randomly distributed 2312245566 we want 453452 to get 4532892234 all the mobile numbers 9999234355  from this given string.“””
Output = [‘8988858683‘, ‘2312245566‘, ‘4532892234‘, ‘9999234355‘]

input = """We have 2233 some employee 8988858683 whos 3455 mobile numbers are randomly distributed 2312245566 we want 453452 to get 4532892234 all the mobile numbers 9999234355  from this given string."""
mid = input.split(' ')
output = []
for ch in mid :
    if ch.isnumeric() == True and len(ch) == 10 :
        output.append(ch)
print('Mobile numbers :', output)
# Mobile numbers : ['8988858683', '2312245566', '4532892234', '9999234355']
----------------------------------------------------------------------------------------------------
122). Write a python program to get all usernames and passwords from the given string.
Input str = “”” SQA tools is online password:user%$%* learning username:john999 platform, password:hrday5554 which helps you become password:P@ssword expert in IT industry username:harry12345 with practice and username:jack38383 solve as much problems you can solve.
“””

input = """SQA tools is online password:user%$%* learning username:john999 platform, password:hrday5554 which helps you become password:P@ssword expert in IT industry username:harry12345 with practice and username:jack38383 solve as much problems you can solve."""
mid = input.split(' ')
output = []
for ch in mid :
    if 'username' in ch or 'password' in ch :
        output.append(ch.split(':')[1])
print('All usernames and passwords :', output)
# All usernames and passwords : ['user%$%*', 'john999', 'hrday5554', 'P@ssword', 'harry12345', 'jack38383']
----------------------------------------------------------------------------------------------------
'''