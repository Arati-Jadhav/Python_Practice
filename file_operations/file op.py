'''
obj = open("filename/filepath", "filemode")
mode :
1. read mode (r) : we can read the content of the existing file with read mode.
2. write mode (w) : we can overwrite the content of the file. (Means existing data will get erased)
3. append mode (a) :  Write in the existing file but without erasing the original content.


# Read mode ('r' mode) -------------------------------------------------------------------------------------------------------------------------------------
obj = open("read.txt", "r")
data = obj.read()
print("filename : ", obj.name)
print("filemode : ", obj.mode)
print(data)
obj.close()
# filename :  read.txt
# filemode :  r
# My name is Amit Devadhe. I learn at My Tech Focus.

# write content to the file ('w' mode) -------------------------------------------------------------------------------------------------------------------------------
# case 1 : If file does not exist : When we open file in write mode, it will create new file and add content to the file.
str1 = 'Hello it is python course and we are learning file_operations.'
filew = open('write.txt', 'w')
filew.write(str1)
filew.close()

# case 2 : If file already exists : We open existing file, then it will overwrite the existing content of the file.
str2 = 'A leaf is any of the principal appendages of a vascular plant stem, usually borne laterally aboveground and specialized for photosynthesis. Leaves are collectively called foliage, as in "autumn foliage", while the leaves, stem, flower, and fruit collectively form the shoot system.'
file = open('write.txt', 'w')
file.write(str2)
file.close()
# Content in exisiting file ---->
# Hello it is python course and we are learning file_operations.

# Content after write operation ---->
# A leaf is any of the principal appendages of a vascular plant stem, usually borne laterally aboveground and
# specialized for photosynthesis. Leaves are collectively called foliage, as in "autumn foliage",
# while the leaves, stem, flower, and fruit collectively form the shoot system.

# Append mode ('a' mode) ------------------------------------------------------------------------------------------------------------------------------------
# Case 1 : If file already exists, then append mode will add content to the existing file.
str1 = 'my name is amit devadhe'
file = open('write.txt', 'a')
file.write(str1)
file.close()
# A leaf is any of the principal appendages of a vascular plant stem, usually borne laterally aboveground and specialized
# for photosynthesis. Leaves are collectively called foliage, as in "autumn foliage", while the leaves, stem,
# flower, and fruit collectively form the shoot system.
# my name is amit devadhe

# Case 2 : IF file does not exist, append mode will create new file and append data in the new file.
file = open('append.txt', 'a')
str1 = 'qwertykgfdsasfghjk,mnbdsazxcvbnm,mnbfdsdfghjkjhgsadfghjkjhgfds'
file.write(str1)
file.close()
# qwertykgfdsasfghjk,mnbdsazxcvbnm,mnbfdsdfghjkjhgsadfghjkjhgfds

# context manager method -------------------------------------------------------------------------------------------------------------------------------
# It has it's own enter and exit method, so no need to close the file specifically.
with open('read.txt', 'r') as file  :
    data = file.read()
    print(data)
# My name is Amit Devadhe. I learn at My Tech Focus.

# Open file with read and write operation with r+.
file = open('hw.txt', 'r+')
data = file.read()
print(data)
file.close()
# I am living in maharashtra state. In ahmednagar district.

# Open file with read and write operation with r+.
file = open('hw.txt', 'r+')
str1 = 'ytrvbhytrfhuyrfhuyrfhy'
data = file.write(str1)
print(data)
file.close()
# 22

# when we open file in 'w+' mode then, if we are reading it, it will erase all the content of the file before reading and
# we will get empty string. So, we don't use 'w+' -----------------------------------------------------------------------------------------------

# 'a+' mode ----------------------------------------------------------
file = open('hw2.py', 'a+')
str2 = 'zxcvbnaasdfghjklqwertyuiop'
file.write(str2)
file.close()
# var2 = 123456778990987654322
# print(var2, type(var2))zxcvbnaasdfghjklqwertyuiop
# create multiple files with loop :
ext = ['txt', 'xls', 'java', 'csv']
for val in ext :
    for i in range(1, 3, 1) :
        file = f'test_{i}.{val}'
        str1 = 'python classes are the best'
        file_obj = open(f'{file}', 'w')
        file_obj.write(str1)
        file_obj.close()

# seek method --> we can set cursor position with this seek method
# tell method --> this method returns current position of cursor

def read_content_set_cursor(filename = 'read.txt') :
    with open(filename, 'rb') as file :
        # initial cursor position
        output1 = file.tell()
        print('initial positiion : ', output1)
        # initial positiion :  0

        byte = file.read(10)
        print('byte10 :', byte)
        # byte10 : b'0.This is '

        output2 = file.tell()
        print('Cursor position after reading 10 char : ', output2)
        # Cursor position after reading 10 char :  10

       # file.seek(40, 0)    # set cursor position from beginning of the file
        #file.seek(40, 1)    # set sursor position from current position of the cursor
        file.seek(-50, 2)
        print('cursor position after its position : ', file.tell())
        # cursor position after its position :  461
        output3 = file.read()
        print('output3 : ', output3)
        # output3 :  b'g a substring like, find(), index(), count(), etc.'

read_content_set_cursor()
'''