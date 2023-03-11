"""
Python data types
1) Numbers :
        a) Integer
        b) Float
        c) Imaginary

2) Sequence :
        a) String
        b) List
        c) Tuple

3) Dictionary
    a) Sets
    b) Boolean
"""
"""
################################ 1) Numbers#################################
# a) Integer <class 'int'> ###################################
var1 = 12344
print(var1, type(var1))
# 12344 <class 'int'>

var2 = 123456778990987654322
print(var2, type(var2))
# 123456778990987654322 <class 'int'>

# b) Float <class 'float'> ###################################
var3 = 23242.2342
print(var3, type(var3))
# 23242.2342 <class 'float'>

var4 = 4353.234678568674649898546
print(var4, type(var4))
# 4353.234678568675 <class 'float'> it takes 12 digits after decimal point and round 12 th digit according to 13th digit

# Operations and data types of their results
# 1) int + int = int
output1 = 5 + 6
print(output1 , type(output1))
# 11 <class 'int'>

# 2) int - int = int
output2 = 6 - 4
print(output2 , type(output2))
# 2 <class 'int'>

# 3) int * int  = int
output3 = 3 * 7
print(output3 , type(output3))
# 21 <class 'int'>

# 4) int // int = int
output4 = 10 // 3
print(output4 , type(output4))
# 3 <class 'int'>

# 5) float + float = float
output5 = 3.5 + 6.8
print(output5 , type(output5))
# 10.3 <class 'float'>

# 6) float - float = float
output6 = 6.7 - 3.8
print(output6 , type(output6))
# 2.9000000000000004 <class 'float'>

# 7) float * float = float
output7 = 4.5 * 2.5
print(output7 , type(output7))
# 11.25 <class 'float'>

# 8) float / float = float
output8 = 6.9 / 2.3
print(output8 , type(output8))
# 3.0000000000000004 <class 'float'>

# 9) float // float = float
output9 = 6.9 // 2.3
print(output9 , type(output9))
# 3.0 <class 'float'>

# 10) int / int = float
output10 = 8 / 4
print(output10 , type(output10))
# 2.0 <class 'float'>

# 11) int  + float = float
output11 = 4 + 5.6
print(output11 , type(output11))
# 9.6 <class 'float'>

# 12) int - float = float
output12 = 6 - 3.4
print(output12 , type(output12))
# 2.6 <class 'float'>

# 13) float - int =
output13 = 6.5 - 3
print(output13 , type(output13))
# 3.5 <class 'float'>

# 14) float * int =
output14 = 4.0 * 7
print(output14 , type(output14))
# 28.0 <class 'float'>

################################ 2) Sequence #################################
# a) String <class 'str'>

str1 = "My Tech Focus"
print(str1, type(str1))
# My Tech Focus <class 'str'>

str2 = "Python " \
       "Programming"
print(str2, type(str2))
# Python Programming <class 'str'>

str3 = "1. My" \
       "2. Tech" \
       "3. Focus"
print(str3, type(str3))
# 1. My2. Tech3. Focus <class 'str'>

str4 = ''' my name is amit.
                I am 23 years old.
                I am writing this for python lecture classwork'''
print(str4, type)
#  my name is amit.
#   I am 23 years old.
#   I am writing this for python lecture classwork
#   <class 'type'>

str5 = " Your Blogger blog’s content will be downloaded to 
                  your computer in an XML file. Once the download 
                  is complete, it is time to import your Blogger
                  content into your WordPress site.
            "
print(str5, type(str5))
# Your Blogger blog’s content will be downloaded to
# your computer in an XML file. Once the download
# is complete, it is time to import your Blogger
# content into your WordPress site.
# <class 'str'>

# "\n"to move cursor to the new line (number of \n means gap of same number of lines)
str6 = "Name of my class is \n My Tech Focus"
print(str6)
# Name of my class is
#  My Tech Focus

# "\t" to give tabs in string (1 tab is equal to 4 spaces or according to IDE)
str7 = "I am learning \t python \t SQl \t PL/SQL"
print(str7)
# I am learning 	 python 	 SQl 	 PL/SQL

# Convert entire string into raw format (means print string which is written in editor)
# write 'r' before single or double quotes of string start
str8 = r"My \t\t Tech \n\n Focus"
print(str8)
# My \t\t Tech \n\n Focus

# to print character multiple times on a single line in OUTPUT
print("-" * 50)
# --------------------------------------------------

print("*" * 70)
# **********************************************************************

# String follows positive and negative index, so string is sequential data type
str9 = "GOOD"
"""
# 0       1       2       3       --> positive index
# G       O       O       D
# -4      -3      -2      -1      --> negative index
"""
# Positive index
print(str9[0])
# G

print(str9[3])
# D

# Negative index
print(str9[-1])
# D

print(str9[-3])
# O

# String slicing (positive index)
str10 = "Programming"
print(str10 [ 2 : 5 ] )
# ogr --> It includes first index of slice but exclude last index of slice
# takes character at place 2 but exclude character at place 5, takes till 4

# String slicing (negative index)
str10 = "Programming"
print(str10 [ -7 : -3 ] )
# ramm --> It includes first index of slice but exclude last index of slice
# takes character at place -7 but exclude character at place -3, takes till -4

# IMPORTANT ---> slicing goes from left to right only. That's why we have to give smaller negative index first
# and larger negative index as second parameter of slicing###################################
"""
