"""
1). Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
      between 1500 and 2700 (both included).
Input1 : 1500
Input2 : 2700

for i in range(1500, 2701, 1) :
    if i % 5 == 0 and i % 7 == 0 :
        print(i, ',' , end = ' ')
# 1505 , 1540 , 1575 , 1610 , 1645 , 1680 , 1715 , 1750 , 1785 , 1820 , 1855 , 1890 , 1925 , 1960 , 1995 , 2030 , 2065 , 2100 , 2135 ,
# 2170 , 2205 , 2240 , 2275 , 2310 , 2345 , 2380 , 2415 , 2450 , 2485 , 2520 , 2555 , 2590 , 2625 , 2660 , 2695,
----------------------------------------------------------------------------------------------------------------------------------------
2). Write a Python program to construct the following pattern, using a nested for loop.

Output :
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

for i  in range(1, 6, 1) :
    for j in range(i) :
        print('*', end = " ")
    print()

for i  in range(4, 0, -1) :
    for j in range(i) :
        print('*', end = " ")
    print()

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
-----------------------------------------------------------------------------------------------------------------------------------------------
3). Write a Python program that accepts a word from the user and reverse it.
Input : "python"
Output : "nohtyp"

str1 = 'python'
for i in range(len(str1) - 1, -1, -1) :
    print(str1[i], end =  "")
# nohtyp
-----------------------------------------------------------------------------------------------------------------------------------------------------
4). Write a Python program to count the number of even and odd numbers from a series of numbers.
Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
Output :
Number of even numbers : 4
Number of odd numbers : 5

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cnte = 0
cnto = 0
for i in list2 :
    if i % 2 == 0 :
        cnte = cnte + 1
    else :
        cnto = cnto + 1

print('Number of even numbers : ', cnte)
print('Number of odd numbers : ', cnto)

# Number of even numbers :  4
# Number of odd numbers :  5
-----------------------------------------------------------------------------------------------------------------------------------------------------
5). Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

for  i in range(0, 7, 1) :
    if i < 3 :
        print(i)
    elif i % 3 != 0 :
        print(i)
# 0
# 1
# 2
# 4
# 5
-----------------------------------------------------------------------------------------------------------------------------------------------------
6). Write a Python program to get the Fibonacci series between 0 to 50. -----------------> while loop
x = 0
y = 1
while y < 50 :
    x, y  = y, y+x
    print(x, end = " ")
# 1 1 2 3 5 8 13 21 34
-----------------------------------------------------------------------------------------------------------------------------------------------------
7). Write a Python program which iterates the integers from 1 to 30.
For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers that are multiples of both three and five print "FizzBuzz". Print all values in a dictionary.

dict1 = {}
for i in range(1, 31, 1) :
    if i % 3 == 0 and i % 5 == 0 :
        dict1[i] = "FizzBuzz"
        conxtinue
    elif i % 5 == 0 :
        dict1[i] = "Buzz"
        continue
    elif i % 3 == 0 :
        dict1[i] = "Fizz"
        continue
print(dict1)

# {3: 'Fizz', 5: 'Buzz', 6: 'Fizz', 9: 'Fizz', 10: 'Buzz', 12: 'Fizz',
# 15: 'FizzBuzz', 18: 'Fizz', 20: 'Buzz', 21: 'Fizz', 24: 'Fizz', 25: 'Buzz', 27: 'Fizz', 30: 'FizzBuzz'}
-------------------------------------------------------------------------------------------------------------------------------------------------------
8). Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j. (Note : (i = 0,1.., m-1) ( j = 0,1, n-1)).

Input1 : number of rows: 5
Input2 : number of columns: 6
Output :
[[0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5], [0, 2, 4, 6, 8, 10], [0, 3, 6, 9, 12, 15], [0, 4, 8, 12, 16, 20]]

row = int(input("Enter number of rows : "))
col = int(input("Enter number of columns : "))

list1 = [ [0 for c in range(col) ] for r in range(row) ]
for r in range(row) :
    for c in range(col) :
        list1[r][c] = r * c

for i in range(row) :
    for j in range(col) :
        print(list1[i][j], end = "\t\t")
    print()

# Enter number of rows : 5
# Enter number of columns : 6
# 0		0		0		0		0		0
# 0		1		2		3		4		5
# 0		2		4		6		8		10
# 0		3		6		9		12		15
# 0		4		8		12		16		20
-----------------------------------------------------------------------------------------------------------------------------------------------------
9). Write a Python program that accepts a sequence of lines (blank line to terminate) as
input and prints the lines as output (all characters in lower case).
Input1 : "sqa tools"
Input2 : "python"
Output1 : "SQA TOOLS"
Output2 : "PYTHON"

lines = []
while True :
    l = input()
    if l :
        lines.append(l.upper())
    else :
        break
for l in lines :
    print(l)

# amit devadhe
#  (blank line to terminate)
# AMIT DEVADHE
---------------------------------------------------------------------------------------------------------------------------

10). Write a Python program that accepts a string and calculates the number of digits and letters.
Input : "python1234"
Output :
Letters 6
Digits 4

str1 = input("Enter string to calculate number of digits and letters : ")
cd = 0
cl = 0
for i in str1 :
    if i.isdigit() :
        cd = cd + 1
    elif i.isalpha() :
        cl = cl + 1
    else :
        continue
print("Number of letters : ", cl)
print("Number of digits is : ", cd)

# Enter string to calculate number of digits and letters : python1234
# Number of letters :  6
# Number of digits is :  4
-----------------------------------------------------------------------------------------------------------------------------------------------------

11). Write a Python program to print the alphabet pattern 'O'.
Output:
  ***
*       *
*       *
*       *
*       *
*       *
  ***

print("   ***")
for i in range(0, 6, 1) :
    print("*        *")
print("   ***")
-----------------------------------------------------------------------------------------------------------------------------------------------------

12).	Write a Python program to print all natural numbers from 1 to n. - using while loop

n = int(input("Enter last number : "))
for i in range(1, n+1, 1) :
    print(i, end = " ")

# Enter last number : 10
# 1 2 3 4 5 6 7 8 9 10
-----------------------------------------------------------------------------------------------------------------------------------------------------

13).	Write a Python program to print all natural numbers in reverse (from n to 1). - using while loop.

n = int(input("Enter last number : "))
for i in range(n, 0, -1) :
    print(i, end = " ")
# Enter last number : 10
# 10 9 8 7 6 5 4 3 2 1
-----------------------------------------------------------------------------------------------------------------------------------------------------
14).	Write a Python program to print all alphabets from a to z. - using while loop
        Take chr method help to print character with ascii values
        chr(65) = 'A'
        A-Z ASCII Range  65-90
        a-z ASCII Range  97-122

for i in range(97, 123, 1) :
    print(chr(i), end = " ")
# a b c d e f g h i j k l m n o p q r s t u v w x y z
-----------------------------------------------------------------------------------------------------------------------------------------------------
15).	Write a Python program to print all even numbers between 1 to 100. - using while loop

for i in range(2, 101, 2) :
    print(i, end = " ")
# 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50
# 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100
-----------------------------------------------------------------------------------------------------------------------------------------------------
16).	Write a Python program to print all odd number between 1 to 100.

for i in range(1, 101, 2) :
    print(i, end = " ")
# 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49
# 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99
-----------------------------------------------------------------------------------------------------------------------------------------------------
17).	Write a Python program to find sum of all natural numbers between 1 to n.
sum = 0

input1 = int(input("enter number to find sum : "))
for i in range(1, input1+1, 1) :
    sum = sum + i

print(sum)

# enter number to find sum : 10
# 55
-----------------------------------------------------------------------------------------------------------------------------------------------------
18).	Write a Python program to find sum of all even numbers between 1 to n.

num = int(input("Enter number to find sum : "))
sum = 0
for i  in range(0, num+1, 2) :
    sum = sum + i

print(sum)
# Enter number to find sum : 10
# 30
-----------------------------------------------------------------------------------------------------------------------------------------------------
19).	Write a Python program to find sum of all odd numbers between 1 to n.
num = int(input("Enter number to find sum : "))
sum = 0
for i  in range(1, num+1, 2) :
    sum = sum + i

print(sum)
# Enter number to find sum : 10
# 25
-----------------------------------------------------------------------------------------------------------------------------------------------------
20).	Write a Python program to count number of digits in a number.

num = int(input("Enter number : "))
cnt = 0
while num > 0 :
    temp = num % 10
    cnt = cnt + 1
    num = num // 10
print(cnt)

# Enter number : 6523
# 4
-----------------------------------------------------------------------------------------------------------------------------------------------------
21).	Write a Python program to find the first and last digits of a number.

num = int(input("Enter number to find fiirst and last digit : "))
last = num % 10
while num//10 > 0 :
    num = num // 10
print("First and last digits of given number : \nfirst : ", num, "\tLast :  ", last)

# Enter number to find fiirst and last digit : 4563247893289
# First and last digits of given number :
# first :  4 	Last :   9
-----------------------------------------------------------------------------------------------------------------------------------------------------
22).	Write a Python program to find the sum of the first and last digit of a number.

num = int(input("Enter number to find fiirst and last digit : "))
last = num % 10
while num//10 > 0 :
    num = num // 10
print("Sum of first and last digit of given number is : ", num + last)

# Enter number to find fiirst and last digit : 1234
# Sum of first and last digit of given number is :  5
-----------------------------------------------------------------------------------------------------------------------------------------------------
23).	Write a Python program to swap first and last digits of a number.

num = input("Enter number to swap first and last digit : ")
new_num = num[-1] + num[1 : -1] + num[0]
print(new_num)

# Enter number to swap first and last digit : 1234
# 4231
-----------------------------------------------------------------------------------------------------------------------------------------------------
24).	Write a Python program to calculate sum of digits of a number.

num = int(input("Enter number : "))
sum = 0
while num > 0 :
    temp = num % 10
    sum = sum + temp
    num = num // 10
print(sum)

# Enter number : 1234
# 10
-----------------------------------------------------------------------------------------------------------------------------------------------------
25).	Write a Python program to calculate the product of digits of a number.

num = int(input("Enter number : "))
mul = 1
while num > 0 :
    temp = num % 10
    mul = mul * temp
    num = num // 10
print(mul)

# Enter number : 1234
# 24
-----------------------------------------------------------------------------------------------------------------------------------------------------
26).	Write a Python program to enter a number and print its reverse.

n = int(input("Enter number to reverse : "))
result = 0
while n > 0 :
    temp = n % 10
    result = result * 10 + temp
    n = n // 10
print("Reverse of the number is : ", result)

# Enter number to reverse : 125639
# Reverse of the number is :  936521
-----------------------------------------------------------------------------------------------------------------------------------------------------
27).	Write a Python program to check whether a number is a palindrome or not.

n = int(input("Enter number to check palindrome : "))
a = n
result = 0
while n > 0 :
    temp = n % 10
    result = result * 10 + temp
    n = n // 10

if a == result :
    print("Number is palindrome")
else:
    print("Not palindrome")

# Enter number to check palindrome : 1221
# Number is palindrome

# Enter number to check palindrome : 1234
# Not palindrome
-----------------------------------------------------------------------------------------------------------------------------------------------------
28).	Write a Python program to find the frequency of each digit in a given integer.

num = int(input("Enter number to find frequency of digits : "))
print("Digit\t\tFrequency")
for i in range(0, 10, 1) :
    count = 0
    temp = num
    while temp > 0 :
        digit = temp % 10
        if digit == i :
            count = count + 1
        temp = temp // 10
    if count > 0 :
        print(i, "\t\t", count)

    # Enter number to find frequency of digits : 22556633
    # Digit		Frequency
    # 2 		 2
    # 3 		 2
    # 5 		 2
    # 6 		 2
-----------------------------------------------------------------------------------------------------------------------------------------------------
29).	Write a Python program to enter a number and print it in words.

num = input("Enter number to print in words : ")
lenn = len(num)
for i in range(lenn) :
    if num[i] == '1' :
        print("One", end = " ")
    elif num[i] == '2' :
        print("Two", end = " ")
    elif num[i] == '3' :
        print("Three", end = " ")
    elif num[i] == '4' :
        print("Four", end = " ")
    elif num[i] == '5' :
        print("Five", end = " ")
    elif num[i] == '6' :
        print("Six", end = " ")
    elif num[i] == '7' :
        print("Seven", end = " ")
    elif num[i] == '8' :
        print("Eight", end = " ")
    elif num[i] == '9' :
        print("Nine", end = " ")
    elif num[i] == '0' :
        print("Zero", end = " ")

# Enter number to print in words : 4521
# Four Five Two One
-----------------------------------------------------------------------------------------------------------------------------------------------------
30).	Write a Python program to find the power of a number using for loop.
    Take values as an input base number and power, and get the total value using a loop.

num = int(input("Enter number to find power : "))
powr = int(input("Enter power to find : "))
result = 1
for i in range(0, powr, 1) :
    result = result * num
print(result)

# Enter number to find power : 2
# Enter power to find : 4
# 16
-----------------------------------------------------------------------------------------------------------------------------------------------------
31).	Write a Python program to find all factors of a number.
        Get all the numbers that can divide this number from 1 to n.

num = int(input("Enter number to find factors : "))
for i in range(1, num, 1) :
    if num % i == 0 :
        print(i, end = " ")
    else :
        continue

# Enter number to find factors : 16
# 1 2 4 8
-----------------------------------------------------------------------------------------------------------------------------------------------------
32).	Write a Python program to calculate the factorial of a number.

num = int(input("Enter number to find factorial : "))
result = 1
for i in range(1, num+1, 1) :
    result = result * i
print(result)

# Enter number to find factorial : 4
# 24
-----------------------------------------------------------------------------------------------------------------------------------------------------
33).	Write a Python program to check whether a number is a Prime number or not.

num = int(input("Enter number to check for prime : "))
prime = True
for i in range(2, num // 2) :
    if num % i == 0 :
        prime = False
    else :
        continue

if prime :
    print("This is a prime number : ", num)
else :
    print("This is not a prime number : ", num)

# Enter number to check for prime : 31
# This is a prime number :  31

# Enter number to check for prime : 25
# This is not a prime number :  25
-----------------------------------------------------------------------------------------------------------------------------------------------------
34).	Write a Python program to print all Prime numbers between 1 to n.

num = int(input("Enter last number to prime numbers till that number : "))
for j in range(2, num + 1, 1) :
    prime = True
    for i in range(2, j, 1) :
        if j % i == 0 :
            prime = False
        else :
            continue
    if prime:
        print(j, end = " ")

# Enter last number to prime numbers till that number : 20
# 2 3 5 7 11 13 17 19
-----------------------------------------------------------------------------------------------------------------------------------------------------
35).	Write a Python program to find the sum of all prime numbers between 1 to n.

result = 0
num = int(input("Enter last number to prime numbers till that number : "))
for j in range(2, num + 1, 1) :
    prime = True
    for i in range(2, j, 1) :
        if j % i == 0 :
            prime = False
        else :
            continue
    if prime:
        result += j
print(result)

# Enter last number to prime numbers till that number : 10
# 17
-----------------------------------------------------------------------------------------------------------------------------------------------------
36).	Write a Python program to find all prime factors of a number. ---> Not completed

result = 0
num = int(input("Enter number to find all prime factors : "))
for i in range(2, (num+1)//2, 1) :
    if num % i == 0 :
        prime = True
        for j in range(2, i // 2):
            if num % j == 0:
                prime = False
                continue
        print(i, end = " ")
-----------------------------------------------------------------------------------------------------------------------------------------------------
37).	Write a Python program to check whether a number is an Armstrong number or not.
        Armstrong Example : 153 = 1*1*1 + 5*5*5 + 3*3*3

result = 0
num = int(input("Enter number to check for Armstrong number : "))
temp = num
while temp > 0 :
    digit = temp % 10
    result += digit ** 3
    temp //= 10

if num == result :
        print(num, " is an armstrong number")
else :
    print(num, " is not an armstrong number")

# Enter number to check for Armstrong number : 153
# Armstrong Number

# Enter number to check for Armstrong number : 181
# Not an Armstrong number
-----------------------------------------------------------------------------------------------------------------------------------------------------
38).	Write a Python program to print all Armstrong numbers between 1 to n.
        Armstrong Example : 153 = 1*1*1 + 5*5*5 + 3*3*3

num = int(input("Enter number to check for Armstrong number : "))
for i in range(1, num+1, 1) :
    order = len(str(i))
    temp = i
    result = 0
    while temp > 0 :
        digit = temp % 10
        result += digit ** order
        temp //= 10

    if i == result :
        print(i, end = " ")

# Enter number to check for Armstrong number : 2000
# 1 2 3 4 5 6 7 8 9 153 370 371 407 1634

-----------------------------------------------------------------------------------------------------------------------------------------------------
39).	Write a Python program to check whether a number is a Perfect number or not.
        Get factors of any number and the sum of those factor should be equal to given number
        Factor of 28: 1, 2, 4, 7, 14 and their sum is 28.

sum = 0
num = int(input("Enter number to check for perfect number : "))
for i in range(1, num, 1) :
    if num % i == 0 :
        sum += i
    else :
        continue

if sum == num :
    print(num, " is Perfect number.")
else :
    print(num, " is not Perfect number.")

# Enter number to check for perfect number : 28
# 28  is Perfect number.

# Enter number to check for perfect number : 16
# 16  is not Perfect number.
-----------------------------------------------------------------------------------------------------------------------------------------------------
40).	Write a Python program to print all Perfect numbers between 1 to n.
        Factor of 28: 1, 2, 4, 7, 14 and their sum is 28.

num = int(input("Enter number to print perfect numbers till : "))
for j in range(1, num+1, 1) :
    sum = 0
    for i in range(1, j, 1) :
        if j % i == 0 :
            sum += i
    if sum == j :
        print(j, end = " ")

# Enter number to print perfect numbers till : 1000
# 6 28 496
-----------------------------------------------------------------------------------------------------------------------------------------------------
41).	Write a Python program to print Fibonacci series up to n terms.
        1, 2, 3, 5, 8, 13, 21 .....n

num = int(input("Enter how number of terms for fibonacci series : "))
x = 0
y = 1
for i in range(num) :
    x, y  = y, y+x
    print(x, end = " ")

# Enter how number of terms for fibonacci series : 9
# 1 1 2 3 5 8 13 21 34
-----------------------------------------------------------------------------------------------------------------------------------------------------
42). Write a Python program to print the multiplication table of any number.

num = int(input("Enter number to print table : "))
for i in range(1, 11, 1) :
    print(num * i, end = " ")

# Enter number to print table : 18
# 18 36 54 72 90 108 126 144 162 180
-----------------------------------------------------------------------------------------------------------------------------------------------------
43).Write a Python program to print the alphabet T work with a pattern.

for i in range(1, 4, 1) :
    for j in range(1, 10, 1) :
        print("*", end = " ")
    print()

for j in range(1, 7, 1) :
    print("         * * *")

# * * * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
#         * * *
#         * * *
#         * * *
#         * * *
#         * * *
#         * * *
-----------------------------------------------------------------------------------------------------------------------------------------------------
44).  Write a Python program to print number patterns.
Output:
1
2   3
4   5   6
7   8   9   10
11  12  13  14  15
14  13  12  11
10  9   8
7   6
5

num = 1
n = int(input("Enter number to print pattern : "))
for i in range(0, n, 1) :
    for j in range(i+1) :
        print(num, end = "  ")
        num += 1
    print()
num = num - 2
for i in range(n-1, 0, -1) :
    for j in range(i) :
        print(num, end = "  ")
        num -= 1
    print()

# Enter number to print pattern : 5
# 1
# 2  3
# 4  5  6
# 7  8  9  10
# 11  12  13  14  15
# 14  13  12  11
# 10  9  8
# 7  6
# 5
-----------------------------------------------------------------------------------------------------------------------------------------------------
44). Write a Python program to print A char with * pattern.

n = 8
for i in range(n):
    for j in range((n // 2) + 1):
        if ((j == 0 or j == n // 2) and i != 0 or
                i == 0 and j != 0 and j != n // 2 or
                i == n // 2):
            print("*", end="")
        else:
            print(" ", end=" ")
    print()

#   ***
# *      *
# *      *
# *      *
# *****
# *      *
# *      *
# *      *
-----------------------------------------------------------------------------------------------------------------------------------------------------
45). Write a Python program to print the pyramid structure.

num = int(input("Enter number of steps for triangle pattern with * : "))
k = num - 1
for i in range(0, num, 1) :
    for j in range(0, k, 1) :
        print(end = "  ")
    k = k - 1
    for j in range(0, i + 1, 1) :
        print("* ", end = " ")
    print()

# Enter number of steps for triangle pattern with * : 5
#         *
#       *  *
#     *  *  *
#   *  *  *  *
# *  *  *  *  *
-----------------------------------------------------------------------------------------------------------------------------------------------------
"""