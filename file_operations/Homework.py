'''
file = open('hw.txt', 'r')
data = file.read()
print("File name : ", file.name)
print("File mode : ", file.mode)
print(data)
file.close()
# File name :  hw.txt
# File mode :  r
# India is very diverse country. It has all the thing that a ideal country needs to make progress in the future.
# I am living in maharashtra state. In ahmednagar district.


file1 = open('hw2.py', 'r')
data1 = file1.read()
print("File name : ", file1.name)
print("File mode : ", file1.mode)
print(data1)
file1.close()
# File name :  hw2.py
# File mode :  r
# var2 = 123456778990987654322
# print(var2, type(var2))

# Write mode (case 1) -------------------------------------------------------------------------------------------------------------------------------------------
file = open('write2.py', 'w')
str2 = #print('amit')
               # aditya = 'tera mera'

# file.write(str2)
# file.close()
# print('amit')
# aditya = 'tera mera'

# Write mode (case 2) -----------------------------------------------------------------------------------------------------------------------------------------
strf = 'vrunda arati amit'
file = open('write.py', 'w')
file.write(strf)
file.close()
# after write operation
#vrunda arati amit

# append mode (case1) -------------------------------------------------------------------------------------------------------------------------------------------
file = open('write.txt', 'a')
str2 = '''#my father's name is vitthal devadhe.'''
'''
file.write(str2)
file.close()
# A leaf is any of the principal appendages of a vascular plant stem, usually borne laterally aboveground and specialized
# for photosynthesis. Leaves are collectively called foliage, as in "autumn foliage", while the leaves, stem,
# flower, and fruit collectively form the shoot system.
# my name is amit devadhe
# my father's name is vitthal devadhe.

# append mode (case 2) -----------------------------------------------------------------------------------------------------------------------------------
file = open('append2.txt', 'a')
str1 = 'svbnmkuytfswertyuikfdsxcvbhytrewasghju543wq'
file.write(str1)
file.close()
# svbnmkuytfswertyuikfdsxcvbhytrewasghju543wq

# r+ mode for reading and writing
file = open('hw.txt', 'r+')
str1 = 'my tech focus'
data = file.write(str1)
print(data)
# 13
'''
