'''
if - else --> control structures. We can control the output based on conditions
structure -->
if condition :
    code
else :
    code

#### Important --> Indentation is very important. Without it, program will give errors


# 1) simple if - else
num1 = 23
if num1:
    print("num1 has value")
else:
    print("num1 is empty")
# num1 has value

# 2)
key = False
if key :
    print("Door open successfully")
else :
    print("cannot open door")
# cannot open door


Conditional and Arithmatic Operators -->
== : equal to operator
< : less than operator
> : greater than operator
<= : less than equal to operator
>= : greater than equal to operator
% : remainder operator
+ : addition operator
- : subtraction operator
* : multiplication operator
/ : division operator (division in float)
// : division operator (division in integer)
** : power operator
!= : not equal to operator
"""
"""
Nested Condition --> 
if condition1 :
    code
    if condition2 :
        code
    else :
        code
else : 
    code


# 1) nested if  - else
num1 = 23
if num1 % 5 == 0 :
    if num1 % 3 == 0 :
        print("number is divisible by 5 and 3 both")
    else :
        print("number is divisible by 5 only")
else :
    print("number is not divisible by 5 and 3")

#  num1 = 23 --> number is not divisible by 5 and 3
# num1  = 20 --> number is not divisible by 5 only
# num1 = 30 --> number is divisible by 5 and 3


if - elif - else
structure --> 
if condition1 :
    code
elif conddition2 :
    code
elif condition3 :
    code
else :
    code


# 1)
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


Logical Operators -->
############################  AND  #########################
If both conditions are true then output will be true, otherwise false.
    condition_1 AND condition_2
    TRUE AND TRUE : TRUE
    TRUE AND FALSE : FALSE
    FALSE AND TRUE : FALSE
    FALSE AND FALSE : FALSE
    
############################  OR  ############################
If both conditions are false then output will be false otherwise true.
    condition_1 OR condition_2
    TRUE OR TRUE : TRUE
    TRUE OR FALSE : TRUE
    FALSE OR TRUE : TRUE
    FALSE OR FALSE : FALSE


# 1)
marks = 50
if marks > 40 and marks <= 50 :
    print("Third grade")
elif marks > 50 and marks <= 60 :
    print("Second grade")
elif marks > 60 :
    print("First grade")
else : print("Wrong input")

# marks = 50 --> Third grade
# marks = 56 --> Second grade
# marks = 80 --> First Grade
# marks = 10 --> Wrong input

# 2)
marks = int(input("Enter marks of a student : "))
if marks <= 100 :
    if marks > 30 and marks <= 40 :
        print("Student passed with lowest grade")
    elif marks > 40 and marks <= 50 :
        print("Student passed with second grade")
    elif marks > 50 and marks <= 60 :
        print("Student passed with first grade")
    elif marks > 60 and marks <= 80 :
        print("Student passed with A grade")
    elif marks > 80 and marks <= 100 :
        print("Student passed with A++ grade")
    else :
        print("Student failed in the exam")
else :
    print("Invalid input, marks cannot be grater than 100")

# Enter marks of a student : 47
# Student passed with second grade

# Enter marks of a student : 106
# Invalid input, marks cannot be grater than 100

# Enter marks of a student : 75
# Student passed with A grade

# Enter marks of a student : 86
# Student passed with A++ grade

# Enter marks of a student : 20
# Student failed in the exam
"""
# Homework --------------->
"""
Program1: Write a python program to create basic calculator. User has to give three inputs
input1 : decision -->  1 = addition, 2 = multiplication, 3 = subtraction, 4 = divide
input2 = num1
input2 = num2

input1 = int(input("Enter which operation you want to perform"
                                    "\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\nEnter code : "))
input2 = int(input("Enter first number : "))
input3 = int(input("Enter second number : "))

if input1 == 1 :
    print("Addition of 2 numbers is : ", input2 + input3)
elif input1 == 2 :
    print("Subtraction of 2 numbers is : ", input2 - input3)
elif input1 == 3 :
    print("Multiplication of 2 numbers is : ", input2 * input3)
elif input1 == 4 :
    print("Division of 2 numbers is : ", input2 / input3)
else :
    print("Invalid operation code entered")


1) --------------------------------------------------------------
Enter which operation you want to perform
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter code : 2
Enter first number : 3
Enter second number : 1
Subtraction of 2 numbers is :  2

2) -----------------------------------------------------------------
Enter which operation you want to perform
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter code : 3
Enter first number : 3
Enter second number : 8
Multiplication of 2 numbers is :  24

3) ------------------------------------------------------------------
Enter which operation you want to perform
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter code : 1
Enter first number : 34
Enter second number : 78
Addition of 2 numbers is :  112

4) ------------------------------------------------------------------------
Enter which operation you want to perform
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter code : 4
Enter first number : 26
Enter second number : 5
Division of 2 numbers is :  5.2

5) ----------------------------------------------------------------------------
Enter which operation you want to perform
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter code : 5
Enter first number : 45
Enter second number : 67
Invalid operation code entered
"""

"""
Program2 : Write a python program to find greatest of 3 numbers --> a, b, c
a > b and a > c : print(a)
b > a and b > c : print(b)
c > a and c > b : print(c)
"""
"""
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if a > b :
    if a > c :
        print("Greatest number is : ", a)
    else :
        print("Greatest number is : ", c)
elif b > c :
    print("Greatest number is : ", b)
else :
    print("Greatest number is : ", c)
"""
"""
1) ---------------------------------------------------------------------------------
Enter first number : 5
Enter second number : 4
Enter third number : 8
Greatest number is :  8

2) ---------------------------------------------------------------------------------
Enter first number : 3
Enter second number : 4
Enter third number : 5
Greatest number is :  5
"""

"""
Program3 : Write a python program to check that given number is divide by 3 and 5:
"""
'''
num1 = 23
if num1 % 5 == 0 :
    if num1 % 3 == 0 :
        print("number is divisible by 5 and 3 both")
    else :
        print("number is divisible by 5 only")
else :
    print("number is not divisible by 5 and 3")
'''
num1 = 23 --> number is not divisible by 5 and 3
num1  = 20 --> number is not divisible by 5 only
num1 = 30 --> number is divisible by 5 and 3
'''