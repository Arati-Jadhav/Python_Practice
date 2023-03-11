'''
function syntax --->
def fun_name() :
    code
'''

# def addition() :
#     n1 = 25
#     n2 = 36
#     print(n1 + n2)

# addition()
#61

# provide parameter/ argumants ---------------------------------------------------------------
# def addition2(no1, no2) :
#     print("addition : ", no1 + no2)

# 1. pass by value ----------------------------------------------------------------
# addition2(41, 69)
# addition : 110

# 2. pass by reference ----------------------------------------------------------
# x = 80
# y = 36
# addition2(x, y)
# addition :  116

# Examples ----->
# def add(num1, num2 = 60) :
#     print("add : ", num1 + num2)

# add(700)
# add :  760

# add('arati', 'jadhav')
# add :  aratijadhav

# def mul(num1 = 60, num2 = 90) :     # default parameters
#     print("mult : ", num1 * num2)

# mul()   # if not given it takes default parameters
# mult :  5400

# mul(0)   # if given one parameter then second is from default
# mult :  0

# mul(10, 20)     # if given 2 parameters then they will replaced the default
# mult :  200

# function to find largest value from 2 values ------>
# def lar(n1, n2) :
#     if n1 > n2 :
#         print("largest number is : ", n1)
#     else :
#         print("largest number is : ", n2)

# lar(3, 7)
# largest number is :  7

# function to find length of given string --------->
# def leng(str1) :
#     cnt = 0
#     for val in str1 :
#         cnt += 1
#     print("Length of ", str1, " is : ", cnt)

# leng('arati')
# Length of  arati  is :  5
# ------------------------------------------------------------------------------
# *args : provide list of values to the function
# def square(*args) :
#     for data in args :
#         print(data, " : ", data ** 2)

# square(4, 7, 1, 23, 19)
# 4  :  16
# 7  :  49
# 1  :  1
# 23  :  529
# 19  :  361
# ------------------------------------------------------------------------------
# function to print number after adding 10 to each number
# def add10(*args) :
#     for val in args :
#         print(val + 10, end = ' ')

# add10(1,2,3,4,5,6)
# 11 12 13 14 15 16
# ---------------------------------------------------------------------------
# function to reverse the list ------->
# def rev(*args) :
#     print("Reverse : ", args[ : : -1])

# list1 = [1,2,3,4,5]
# rev(list1)
# Reverse :  ([1, 2, 3, 4, 5],)
# ----------------------------------------------------------------------------
# def ptuple(tup1) :
#     print("tuple : ", tup1)

# tup1 = (4, 'amit', 6, 8.0, 'Stars')
# ptuple(tup1)
# tuple :  (4, 'amit', 6, 8.0, 'Stars')
# -------------------------------------------------------------------------
# **kwargs : defined parameters in key value format

# def empl(**kwargs) :
#     print(kwargs)
#     for key, value in kwargs.items() :
#         print(key, ' : ', value)

# empl(name = 'rahul', email = 'rahul@gmail.com')
# name  :  rahul
# email  :  rahul@gmail.com
# --------------------------------------------------------------------------
# def login(**kwargs)  :
#     username = 'amit'
#     password = 'asdfg'
#     if kwargs['username'] == username and kwargs['password'] == password :
#         print('login successful')
#     else :
#         print('Login failed')

# login(username = 'amit', password = 'asdfg')
# login successful

# login(username = 'aishwarya', password = 'aditya')
# Login failed

# ----------------------------------------------------------------------------
# def amit(**kwargs)  :
#     output = {}
#     for key, value in kwargs.items() :
#         output[key] = value ** 2
#     print(output)

# dict1 = {'a' : 4, 'b' : 5, 'c' : 12}
# amit(dict1)
# TypeError: amit() takes 0 positional arguments but 1 was given

# amit(a = 3, b = 4, c = 8)
# {'a': 9, 'b': 16, 'c': 64}
# --------------------------------------------------------------------------------

'''
Variable scope ---->
global scope ---> scope in all functions
local scope ----> scope in only respective function
nonlocal scope ----> 
'''

# global variable
# var1 = 90

# def show() :
#     var2 = 40   # local variable
#     print('Global variable :', var1)
#     print('Local variable : ', var2)

# show()
# Global variable : 90
# Local variable :  40

# def outer () :
#     print('outer variable')
#
#     def inner() :
#         print('inner variable')
#
#     inner()
# outer()

# outer variable
# inner variable