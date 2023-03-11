"""
String is immutable. Once it is defined, it cannot be changed.
String follows positive and negative indexing to read.
Any char or word is considered as string.

str1 = "Python Programming"
print(str1, type(str1))
# Python Programming <class 'str'>

name = "Amit"
age = 23
salary = 102032
# Hello my name is Amit and my age is 23. I earn 102032 rupees per month.

# String formatting -->
# Plus operator -->
output1 = "Hello my name is " + name + " and my age is " + str(age) + ". I earn " + str(salary) + " rupees per month."
print(output1)
# Hello my name is Amit and my age is 23. I earn 102032 rupees per month.

# Format method -->
output2 = "Hello my name is {} and my age is {}. I earn {} rupees per month.".format(name, age, salary)
print(output2)
# Hello my name is Amit and my age is 23. I earn 102032 rupees per month.

# F string formatting -->
output3 = f"Hello my name is {name} and my age is {age}. I earn {salary} rupees per month."
print(output3)
# Hello my name is Amit and my age is 23. I earn 102032 rupees per month.

# Indexing -->
# left to right default index is 0
# right to left default index is -1

str2 = "Python programming"
print(str2[7])
# p

print(str2[-3])
# i

# Slicing of string -->
str3 = "My Tech Focus"
print(str3[1 : 6 : 1])
# y Tec

print(str3[ : 6 : 1])   # --> Rule 1 : If not given deafault first parameter is 0
# My Tec

print(str3[3 :  : 1])   # --> Rule 2 : If not given deafault last parameter is end of string
# Tech Focus

print(str3[3 : 8 : ])   # --> Rule 3 : If not given deafault jump is 1
# Tech

# Negative index -->
str4 = "Amit Vitthal Devadhe"
print(str4[-1 : -10 : -1])
# ehdaveD l

print(str4[1 : -8 : -1])
# No Output

print(str4[-1 : 8 : -1])    # --> Little tricky : Start from end of string but stop untill second parameter from left is not reached.
# ehdaveD lah

str5 = "Very Good Morning"
print(str5[1 : : 2])
# eyGo onn

print(str5[-1 : : -1])
# gninroM dooG yreV

# If we give only jump value then --->
# 1) If it is positive, first parameter will be 0 and second parameter will be right end of string
# 2) If it is negative, first parameter will be -1 and second parameter will be left end of string

print(str5[ : : 1])
# Very Good Morning

print(str5[ : : -1])
# gninroM dooG yreV

# Program to print every second character of the string.
str1 = "Programming"
output1 = str1[1 : : 2]
print(output1)
# rgamn

# Program to find first 2 and last 2 characters of the string.
str2 = "Python Programming"
ft  = str2[0 : 2 : 1]
lt = str2[-2 : : 1]
print(ft + lt)
# Pyng

# Program to swap first and last character of the string.
str3 = "Programming"
output = str3[-1] + str3[1 : -1 : 1] + str3[0]
print(output)
# grogramminP

str4 = "Very Good Morning"
for char in str4 :
    print(char, end = "")

print(dir(str))

 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 
 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 
 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


# count method --> count of each character in a string
# get count of all character -->
str1 = "Python Programming"
for char in str1 :
    print(char, " : ", str1.count(char))
# P  :  2
# y  :  1
# t  :  1
# h  :  1
# o  :  2
# n  :  2
#    :  1
# P  :  2
# r  :  2
# o  :  2
# g  :  2
# r  :  2
# a  :  1
# m  :  2
# m  :  2
# i  :  1
# n  :  2
# g  :  2

# program to get count of unique characters -->
str1 = "Python Programming"
temp = ""
for char in str1 :
    if char in temp :
        continue
    else :
        print(char, " : ", str1.count(char))
        temp = temp + char
    print("temp : ", temp)
# P  :  2
# temp :  P
# y  :  1
# temp :  Py
# t  :  1
# temp :  Pyt
# h  :  1
# temp :  Pyth
# o  :  2
# temp :  Pytho
# n  :  2
# temp :  Python
#    :  1
# temp :  Python
# r  :  2
# temp :  Python r
# g  :  2
# temp :  Python rg
# a  :  1
# temp :  Python rga
# m  :  2
# temp :  Python rgam
# i  :  1
# temp :  Python rgami

# index --> get index of any character in the given string
str2 = "Very Good Morning, We are learning python"
# if we have repeated character then it will return index of first character occurance.
print(str2.index("g"))
# 16

print(str2.index("We"))
# 19

str2 = "Very Good Morning, We are learning python"
for i in range(len(str2)) :
    print(str2[i], ":", i)
# V : 0
# e : 1
# r : 2
# y : 3
#   : 4
# G : 5
# o : 6
# o : 7
# d : 8
#   : 9
# M : 10
# o : 11
# r : 12
# n : 13
# i : 14
# n : 15
# g : 16
# , : 17
#   : 18
# W : 19
# e : 20
#   : 21
# a : 22
# r : 23
# e : 24
#   : 25
# l : 26
# e : 27
# a : 28
# r : 29
# n : 30
# i : 31
# n : 32
# g : 33
#   : 34
# p : 35
# y : 36
# t : 37
# h : 38
# o : 39
# n : 40

str2 = "Very Good Morning, We are learning python"
print(str2.upper())
# VERY GOOD MORNING, WE ARE LEARNING PYTHON

print(str2.lower())
# very good morning, we are learning python

str3 = "PYTHON"
str4 = "python"

print(str3.isupper())
# True

print(str3.islower())
# False

print(str4.isupper())
# False

print(str4.islower())
# True

# Print string like every even position character is upper otherwise lower
str1 = "Very Good Morning, We are learning python"
output = " "
for i in range(len(str1)) :
    if i % 2 == 0 :
        output = output + str1[i].upper()
    else :
        output = output + str1[i].lower()

print(str1)
print(output)

# Very Good Morning, We are learning python
#  VeRy gOoD MoRnInG, wE ArE LeArNiNg pYtHoN

# split method --> help to split any string with given delimeters and return as list of words/substring
str2 = "Very Good Morning, We are learning python"
output = str2.split(" ")
print(output)
# ['Very', 'Good', 'Morning,', 'We', 'are', 'learning', 'python']

str3 = "Very_Good_Morning_We_are_learning_python"
output2 = str3.split("_")
print(output2)
# ['Very', 'Good', 'Morning', 'We', 'are', 'learning', 'python']

str4 = "Very Good Morning, We are learning python"
output4 = str4.split("o")
print(output4)
# ['Very G', '', 'd M', 'rning, We are learning pyth', 'n']

url = "https://www.google.co.in"
output = url.split("//")
print(output)
# ['https:', 'www.google.co.in']

protocol = output[0][0 : -1]
print(protocol)
# https

w = output[1][0 : 3]
print(w)
# www

server = output[1][4: ]
print(server)
# google.co.in

url = "https://www-google.co.in"
output = url.split("//")[1].split("-")[1]
print(output)
# google.co.in

# Replace method --> helps to replace word1 with word2
str1 = "We are learning python and it is fun"
output = str1.replace("python", "football")
print(output)
# We are learning football and it is fun

output2 = str1.replace("learning", "practicing")
print(output2)

print(str1.replace("python", "football").replace("learning", "practicing").replace("a", "b"))
# We bre prbcticing footbbll bnd it is fun

# Write a program to replace specific character in given string
input1 = "Learning programming is fun and easy to learn"

# get wordlist with split
wordl = input1.split(" ")
temp = " "
output = " "

# go through each word using loop in input1
for word in wordl :
    # check word is equal to required word "programming"
    if word == "programming" :
            # get index of "g" char from the word
            char_index = word.index("g")
            # apply loop using word leg and range
            for i in range(len(word)) :
                # match each index with char "g"
                if i == char_index :
                    # once it matched, replace it with special character temp = temp + "$"
                    temp = temp + "$"
                else :
                    # else add other characters without change
                    temp = temp + word[i]
            output = output + temp
    else :
            output = output + " "
print("Output : ", output)
# Output :     pro$ramming

# Reverse the string -->

1. Slicing
2. for Loop
3. While loop
4. reversed method

# 1. Slicing -->
str1 = "Python"
print(str1[ : : -1])
# nohtyP

# 2. Loop -->
for i in range(len(str1) -1, -1, -1) :
    print(str1[i], end = "")
print()
# nohtyP

# 3. While loop -->
num = len(str1) - 1
temp = ""
while num > -1 :
    temp = temp + str1[num]
    num = num - 1
print(temp)
# nohtyP

# 4. Reversed method -->
str2 = "Programming"
output = reversed(str2)
for char in output  :
    print(char, end = "")
# gnimmargorP

# Strip method---------------------------------------------------------------------
This method is useful to trim spaces from both sides of the string
syntax --> string_name.strip()
2 methods --> Lstrip and Rstrip
Lstrip --> strip spaces at the left side of the string
Rstrip --> strip spaces at the right side of the string

str1 = "        My name is amit devadhe         "
output = str1.strip()
print(str1)
print(output)
#         My name is amit devadhe         #
# My name is amit devadhe

str2 = "I learn at My Tech Focus"
output = str2.strip('Focus')
print(output)
# I learn at My Tech

str3 = "Honesty is the best."
output = str3.strip("Honesty")
print(output)
#  is the best.

str4 = "Python is the best language in the world"
output = str4.lstrip("Python")
print(output)
# is the best language in the world

str5 = "Python is the best language in the world"
output = str5.rstrip("world")
print(output)
# Python is the best language in the

# find method -------------------------------------------------------------------------
This method find and return first occurance of the given key (character) from given string
Returns -1 if it did not find the given key
syntax --> str_name.find(key, start, end)

str1 = "Python is the best language in the world"
output = str1.find("is", 0, len(str1))
print(output)
# 7

str2 = "Python is the best language in the world"
output = str2.find("l")
print(output)
# 19

# join method------------------------------------------------------------------------
This method takes all items in an iterable and join them in one string
A string must be specified as the separator
syntax--> "iterable".join(str_name)

str1 = "Python"
output = "-".join(str1)
print(output)
# P-y-t-h-o-n

str2 = "Python"
output = " ".join(str2)
print(output)
# P y t h o n

# title method --------------------------------------------------------------------------
This method converts first letter of each word present in the string into upper case
If first character of the string is number or special character then letter after that will be captial
No parameters reqiured

str1 = "my tech focus"
output = str1.title()
print(output)
# My Tech Focus

str2 = "my 23tech @focus"
output = str2.title()
print(output)
# My 23Tech @Focus

# swap case method ------------------------------------------------------------------------------
this method return a strin where all uppercase letters in the strin in lowercase and vice versa
syntax --> str_name.swapcase()
No parameters required

str1 = "I Learn At My Tech Focus"
output = str1.swapcase()
print(output)
# i lEARN aT mY tECH fOCUS

str2 = "NaMe Of My HoUsE iS PaRiJaT"
output = str2.swapcase()
print(output)
# nAmE oF mY hOuSe Is pArIjAt

# chr method --------------------------------------------------------------------------------------------
This method return the character associated with given unicode value
for character to ascii use ord() function

print(chr(85))
# U

print(ord("r"))
# 114

# isnumeric method ------------------------------------------------------------------------------------
This method is used to check whether the given string contains numbers

str1 = "586.256"
print(str1.isnumeric())
# False

str2 = "586256"
print(str2.isnumeric())
# True

# isdigit method ------------------------------------------------------------------------------------------------
str1 = '4545'
print(str1.isdigit())
# True

str2= '4545.25'
print(str2.isdigit())
# False

# isalnum method -------------------------------------------------------------------------------------
str1 = "23dvfgbn"
print(str1.isalnum())
# True

str2 = "23456"
print(str2.isalnum())
# True

str3 = "2@3456"
print(str3.isalnum())
# False

# isalpha method ------------------------------------------------------------------------------------------------------
str1 = "python"
print(str1.isalpha())
# True

str2 = "12344"
print(str2.isalpha())
# False
"""
print(dir(str))
str1 = 'amit0'
print(type(str1))