'''
# 1). Write a python program to check given number is divided by 3 or not.
num = 30
if num % 3 == 0 :
    print("divisible by 3")
else :
    print("not divisible by 3")

# divisible by 3

# 2). Write a python program to get all the numbers divided by 3 from 1 to 30.

# 3) Write a python program and get grades as per total marks.
marks > 40 : Fail

marks 40 - 50 : grade C

marks 50 - 60 : grade B

marks 60 - 70 : grade A

marks 70 - 80 : grade A+

marks 80 - 90 : grade A++

marks 90 - 100 : grade Excellent

marks > 100 : Invalid marks

marks = int(input("Enter marks of a student : "))
if marks <= 100 :
    if marks < 40 :
        print("Student failed")
    elif marks >= 40 and marks <= 50 :
        print("C grade")
    elif marks > 50 and marks <= 60 :
        print("B grade")
    elif marks > 60 and marks <= 80 :
        print("A grade")
    elif marks > 80 and marks <= 90 :
        print("A++ grade")
    elif marks > 90 and marks <= 100 :
        print("Excellent grade")
else :
    print("Invalid input, marks cannot be grater than 100")

#Enter marks of a student : 60
# B grade

# 4). Write a python program to check the given number divided by 3 and 5.
num = 60
if num % 2 == 0 :
    print("number is divisible by 2")
elif num % 5 == 0 :
    print("number is divisoble by 5")
else :
    print("number is not divisible by 2 and 5")

#num = 60 --> number is divisible by 2
# num = 25 --> number is divisible by 5
#num = 53 --> number is not divisible by 2 and 5

# 5). Write a python program to print the square of the number if it is divided by 11.
num = 27
if num % 11 == 0 :
    print("square is : ", num * num)
else :
    print("not divisible by 11")

# num = 27 --> not divisible by 11
# num = 22 --> 484

# 6). Write a python program to check given number is a prime number or not.
num = int(input("enter number to check prime or not prime : "))
if num % 2 == 0 :
    print("not prime")
elif num % 3 == 0 :
    print("not prime")
elif num % 5 == 0 :
    print("not prime")
elif num % 7 == 0 :
    print("not prime")
else :
    print("prime")

# enter number to check prime or not prime : 24
# not prime

# enter number to check prime or not prime : 37
# prime

# 7). Write a python program to check given number is odd or even.
num = int(input("enter number to check odd or even : "))
if num % 2 == 0 :
    print("even")
else :
    print("odd")

# enter number to check odd or even : 14786324
# even

# enter number to check odd or even : 1478632369
# odd

# 8). Write a python program to check given number is part of the Fibonacci series from 1 to 10.
# fibonacci Series --> 0, 1, 1, 2, 3, 5, 8, 13.

num = int(input("Enter number to check in fibonacci series : "))
list1 = [1, 1, 2, 3, 5, 8]
if num <= 10 :
    if num == list1[0] :
        print("in fibonacci series")
    elif num == list1[1] :
        print("in fibonacci series")
    elif num == list1[2] :
        print("in fibonacci series")
    elif num == list1[3] :
        print("in fibonacci series")
    elif num == list1[4] :
        print("in fibonacci series")
    elif num == list[5] :
        print("in fibonacci series")
    else :
        print("not in fibonacci series")
else :
    print("not in range")

# Enter number to check in fibonacci series : 2
# in fibonacci series

# Enter number to check in fibonacci series : 13
# not in range

# 9). Write a python program to check authentication with the given username and password.
username = "vivek"
password = "vivek@123"
un = input("Enter username : ")
pas = input("Enter password : ")

if un == username and pas == password :
    print("authentication successful")
else :
    print("unsuccessful")

# Enter username : amit
# Enter password : ait
# unsuccessful

# Enter username : vivek
# Enter password : vivek@123
# authentication successful

# 10). Write a python program to validate user_id in the list of user_ids.
use = int(input("enter user_id to validate : "))
list2 = [1, 2, 3, 4, 5, ]
if use == list2[0] :
    print("validation successful")
elif use == list2[1] :
    print("validation successful")
elif use == list2[2] :
    print("validation successful")
elif use == list2[3] :
    print("validation successful")
elif use == list2[4] :
    print("validation successful")
else :
    print("User_id not found")

# enter user_id to validate : 3
# validation successful

# enter user_id to validate : 6
# User_id not found

# 11). Write a python to print a square or cube if the given number is divided by 2 or 3 respectively.
num  = int(input("enter number to check : "))
if num % 2 == 0 :
    print("square is : ", num * num)
elif num % 3 == 0 :
    print("Cube is : ", num * num * num)

# enter number to check : 4
# square is :  16

# enter number to check : 9
# Cube is :  729

# 12). Write a python program to describe the interview process
# 1st round clear: move to next round else failed
# 2nd round clear: move to next round else failed
# 3rd round clear: move to the next round else failed
# 4th round clear: You are selected.

num = int(input("result of first_round : "))
if num == 1 :
    print("proceed to second round")
    num1 = int(input("result of second round : "))
    if num1 == 1 :
        print("proceed to third round")
        num2 = int(input("result of third round : "))
        if num2 == 1 :
            print("proceed to fourth round")
            num3 = int(input("result of fourth round : "))
            if  num3 == 1 :
                print("You are selected !!")
            else :
                print("Failed in fourth round")
        else :
            print("Third round failed")
    else :
        print("second round failed")
else :
    print("1 round failed")

# result of first_round : 0
# 1 round failed

# result of first_round : 1
# proceed to second round
# result of second round : 0
# second round failed

#result of first_round : 1
# proceed to second round
# result of second round : 1
# proceed to third round
# result of third round : 0
# Third round failed

# result of first_round : 1
# proceed to second round
# result of second round : 1
# proceed to third round
# result of third round : 1
# proceed to fourth round
# result of fourth round : 0
# Failed in fourth round

# result of first_round : 1
# proceed to second round
# result of second round : 1
# proceed to third round
# result of third round : 1
# proceed to fourth round
# result of fourth round : 1
# You are selected !!

# 13). Write a python program to given number is available in the list of numbers or not.
list2 = [1, 2, 3, 4, 5]
use = int(input("enter number to check present or absent : "))
if use == list2[0] :
    print("present")
elif use == list2[1] :
    print("present")
elif use == list2[2] :
    print("present")
elif use == list2[3] :
    print("present")
elif use == list2[4] :
    print("present")
else :
    print("absent")

# enter number to check present or absent : 2
# present

# enter number to check present or absent : 9
# absent

# 15). Write a python program to check any person eligible to vote or not
# age > 18+ : eligible
# age < 18 : not eligible

num1 = int(input("Enter age to check : "))
if num1 >= 18 :
    print("eligible")
else :
    print("not eligible")

# Enter age to check : 30
# eligible

#Enter age to check : 13
# not eligible

# 16). Write a python program to check any given number is palindrome or not.
# Num: 121
# Output: palindrome
# Num: 234
# Output: not a palindrome

# 17). Write a python to check any given string is palindrome or not
# str1 : 'jaj'
# output: palindrome
# str1: 'Hello'
# output: not palindrome
--------------------------------------------------------------------------------------------------
18). Write a program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
Input = Enter marks: 45
Output = Pass

marks = int(input('Enter marks to check pass or fail : '))
if marks > 35:
    print('pass')
else:
    print('fail')
# Enter marks to check pass or fail : 30
# fail

# Enter marks to check pass or fail : 40
# pass
-----------------------------------------------------------------------------------------------------
19). Write a program to check whether the given number is positive or not.
Input = 56
Output = True

Input = -20
Output = False

number = int(input('Enter number to check positive or not : '))
if number < 0:
    print('Not posititve')
else:
    print('Positive')
# Enter number to check positive or not : -1
# Not posititve

# Enter number to check positive or not : 32
# Positive
----------------------------------------------------------------------------------------------------
20). Write a program to check whether the given number is negative or not.
Input = -45
Output = True

number = int(input('Enter number to check negative or not : '))
if number >= 0:
    print('Not negative')
else:
    print('Negative')
# Enter number to check negative or not : -3
# Negative

# Enter number to check negative or not : 30
# Not negative
----------------------------------------------------------------------------------------------------
21). Write a program to check whether the given is positive or negative and even or odd.
Input = 26
Output = The given number is positive and even

number = int(input('Enter number : '))
if number >= 0 and number % 2 == 0:
    print('Positive and Even')
elif number >= 0 and number % 2 == 1:
    print('Positive and Odd')
elif number < 0 and number % 2 == 0:
    print('Negative and Even')
elif number < 0 and number % 2 == 1:
    print('Negative and Odd')
# Enter number : 26
# Positive and Even
---------------------------------------------------------------------------------------------------
22). Write a program to print the largest number from two numbers.
Input:
25, 63
Output = 63

num1 = int(input('Enter num1 : '))
num2 = int(input('Enter num2 : '))
if num1 > num2 :
    print(num1,'is the largest')
else:
    print(num2, 'is the largest')
# Enter num1 : 32
# Enter num2 : 23
# 32 is the largest
----------------------------------------------------------------------------------------------------
23). Write a program to check whether a given character is uppercase or not.
Input = A
Output = The given character is an Uppercase

char = input('Enter char to check upper or not : ')
if char.isupper() == True:
    print('Given character is uppercase')
else:
    print('Given character is not uppercase')
# Enter char to check upper or not : A
# Given character is uppercase

# Enter char to check upper or not : d
# Given character is not uppercase
-----------------------------------------------------------------------------------------------------
24). Write a program to check whether the given character is lowercase or not.
Input = c
Output = True

char = input('Enter char to check upper or not : ')
if char.islower() == True:
    print('Given character is lowercase')
else:
    print('Given character is not lowercase')
# Enter char to check upper or not : a
# Given character is lowercase

# Enter char to check upper or not : B
# Given character is not lowercase
------------------------------------------------------------------------------------------------------
25). Write a program to check whether the given number is an integer or not.
Input = 54
Output = True

Input = 25.3
Output = False

num = input('Enter number to check integer : ')
if num.isnumeric() == True:
    print('Number is integer')
else:
    print('Number is not integer')
# Enter number to check integer : 456
# Number is integer

# Enter number to check integer : 63.23
# Number is not integer
-----------------------------------------------------------------------------------------------------
26). Write a program to check whether the given number is float or not.
Input = 12.6
Output = True

Input = 45
Output: =False

num = input('Enter number to check for float : ')
if num.isnumeric() == False:
    print('Number is float')
else:
    print('Number is not float')
# Enter number to check for float : 456
# Number is not float

# Enter number to check for float : 123.321
# Number is float
-----------------------------------------------------------------------------------------------------\
27). Write a program to check whether the given input is a string or not.
Input = ‘sqatools’
Output = True

Input = 125
Output = False

str1 = input('Enter data : ')
if str1.isalpha() == True:
    print('Given data is string')
else:
    print('Given data is not string')
# Enter data : sqatools
# Given data is string

# Enter data : 123
# Given data is not string
------------------------------------------------------------------------------------------------------
28). Write a program to print all the numbers from 10-15 except 13
Hint: Use the continue statement.
Output:
10
11
12
14

for i in range(10,16,1):
    if i == 13:
        continue
    else:
        print(i, end = ' ')
# 10 11 12 14 15
----------------------------------------------------------------------------------------------------
29). Write a program to find the electricity bill. According to the following conditions:
Up to 50 units rs 0.50/unit
Up to 100 units rs 0.75/unit
Up to 200 units rs 1.25/unit
above 250 rs 1.50/unit
an additional surcharge of 17% is added to the bill
Input = 350
Output = 525

unit = int(input('Enter units : '))
if unit <= 50:
    print('bill is :', unit*0.5)
elif unit > 50 and unit <= 100:
    print('bill is :', unit * 0.75)
elif unit > 100 and unit <= 200:
    print('bill is :', unit * 1.25)
elif unit > 200:
    bill = unit * 1.50
    fbill = bill + (bill * 17 //100)
    print('Bill is :', fbill)
# Enter units : 300
# Bill is : 526
-----------------------------------------------------------------------------------------------------
30). Write a program to check whether a given year is a leap or not.    ---------> not solved
Input = 2000
Output = The given year is a leap year
--------------------------------------------------------------------------------------------------
'''
