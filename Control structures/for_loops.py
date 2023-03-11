"""
For loop -->
structure -->
for i in range(start_point, end_point, jump) :
    code

Important --> for loop will go always till "end_point - 1"

if we give only 1 parameter in range bracket then it will treat it as end_point and start will be 0 and jump will be 1.
if we give 2 parameters then they will be start_point and end_point. Default jump value will be 1
if we want to go backwards, give third parameter aka jump value negative.
"""
"""
for i in range(10) :
    print(i)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for i in range(1,10) :
    print(i)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for i in range(1, 10, 2) :
    print(i)

# 1
# 3
# 5
# 7
# 9

# Program : To print even  numbers from 1 to 30
for i in range(1,30,1) :
    if i % 2 == 0 :
        print(i)
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
# 22
# 24
# 26
# 28

# Program : To find number which are divisible by 5 and 7 between 1 and 100
for i in range(1,100,1) :
    if i % 5 == 0 and i % 7 == 0 :
        print(i)
# 35
# 70

####################################  Read Data  ##################################
# Read different data types with for loop -->
str1 = "Python"
for char in str1 :
    print(char)
# P
# y
# t
# h
# o
# n

# loop on string with indexes
str2 = "PythonPython"
str_len = len(str2)
for i in range(str_len) :
    print(str2[i])
# P
# y
# t
# h
# o
# n
# P
# y
# t
# h
# o
# n

# Read list data with for loop
list1 = [1, 4, 5, 7.8, 'adi']
for var in list1 :
    print(var)
# 1
# 4
# 5
# 7.8
# adi

# with index
for i in range(len(list1)) :
    print(list1[i])
# 1
# 4
# 5
# 7.8
# adi

# Read dictionary with loop
dict1 = {'a' : 152, 'b' : 'amit', 'c' : 'vrunda23'}
for i in dict1 :
    print(i)
# a  --> only keys
# b
# c

for val in dict1.items() :
    print(val)
# ('a', 152)
# ('b', 'amit')
# ('c', 'vrunda23')

for key, val in dict1.items() :
    print('key : ', key, '  value: ', val)
# key :  a   value:  152
# key :  b   value:  amit
# key :  c   value:  vrunda23
"""

# nested loops -->
"""
Structure -->
for condition :
    for condition2 :
        code

for address in range(1, 4, 1) :
        for pkg in range(1, 4, 1) :
            print('add : ', address, '  pkg : ', pkg)
# add :  1   pkg :  1
# add :  1   pkg :  2
# add :  1   pkg :  3
# add :  2   pkg :  1
# add :  2   pkg :  2
# add :  2   pkg :  3
# add :  3   pkg :  1
# add :  3   pkg :  2
# add :  3   pkg :  3

################################## Print Patterns ###############################
1) 
*
* *
* * *
* * * * 
* * * * *

for i in range(1, 6) :
    for j in range(i) :
        print('*', end = " ")
    print()
# *
# * *
# * * *
# * * * *
# * * * * *

2) 
* * * * *
* * * *
* * *
* *
*

for i in range(5, 0, -1) :
    for j in range(i) :
        print('*', end = "  ")
    print()
# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *

"""

###############################  While loop  #####################################
"""
while loop structure -->
while condition :
    code

# program 1
n = 10
temp = 0

while temp <= n :
    print(temp, end = " ")
    temp = temp + 1

# 0 1 2 3 4 5 6 7 8 9 10

# program 2 : python program to reverse a number
n = int(input("Enter number to reverse : "))
result = 0
while n > 0 :
    temp = n % 10
    result = result * 10 + temp
    n = n // 10
print("Reverse of the number is : ", result)

# Enter number to reverse : 18963
# Reverse of the number is :  36981

# Calculator Program

while True :
    input1 = int(input("Enter which operation you want to perform"
                                    "\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\nEnter code : "))

    if input1 == 1 :
        input2 = int(input("Enter first number : "))
        input3 = int(input("Enter second number : "))
        print("Addition of 2 numbers is : ", input2 + input3)
    elif input1 == 2 :
        input2 = int(input("Enter first number : "))
        input3 = int(input("Enter second number : "))
        print("Subtraction of 2 numbers is : ", input2 - input3)
    elif input1 == 3 :
        input2 = int(input("Enter first number : "))
        input3 = int(input("Enter second number : "))
        print("Multiplication of 2 numbers is : ", input2 * input3)
    elif input1 == 4 :
        input2 = int(input("Enter first number : "))
        input3 = int(input("Enter second number : "))
        print("Division of 2 numbers is : ", input2 / input3)
    else :
        print("Invalid operation code entered. Number should be in 1 to 4.")
        break
    print("~" * 50)

# Enter which operation you want to perform
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# Enter code : 3
# Enter first number : 6
# Enter second number : 9
# Multiplication of 2 numbers is :  54
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Enter which operation you want to perform
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# Enter code : 5
# Invalid operation code entered. Number should be in 1 to 4.

# program for continue -->
for i in range(1, 21, 1) :
    if i == 5 or i == 7 or i == 16 :
        continue
    print(i, end = " ")
# 1 2 3 4 6 8 9 10 11 12 13 14 15 17 18 19 20

# program for break -->
for i in range(1, 21, 1) :
    if i == 5 or i == 7 or i == 16 :
        break
    print(i, end = " ")
# 1 2 3 4

# Program : to check given number is prime or not -->
import time
num = 625389
prime = True
t1 = time.time()
for i in range(2, num // 2) :
    if num % i == 0 :
        prime = False
    else :
        continue
t2 = time.time()

print("total execution time is : ", t2 - t1)
if prime :
    print("This is a prime number : ", num)
else :
    print("This is not a prime number : ", num)

# for i in range(2, num // 2) -->
# total execution time is :  0.03590202331542969
# This is not a prime number :  625389

# for i in range(2, num) -->
# total execution time is :  0.0857686996459961
# This is not a prime number :  625389
"""