# Declaring variables and assigning values
z = 2
x = 3.6
y = "my name is python"

# type returns datatype of variable
print(type(z))
# <class 'int'>

print(type(x))
# <class 'float'>

print(type(y))
# <class 'str'>

# = is for assigning value to a variable
g = 6
print(g)
# output -> 6

# == is for comparing
r = 6
e = 6
print(r == e)
# output -> False (datatype boolean)

# assigning multiple values to multiple variables
v, n, m = 10, 30, 40
print(v, n, m)
# 10 30 40

# Comparing variables
print( v == n == m)
# False

# Addition
num1 = 3
num2 = 6
output = num1 + num2
print("Addition is: ", output)
# output -> Addition is: 9

num1 = 34
num2 = 23
output = num1 + num2
print("Addition is: ", output)
# output -> Addition is: 57

# Subtraction
num1 = 4
num2 = 16
output = num1 - num2
print("Subtraction is: ", output)
# output -> Subtraction is: -12

num1 = 45
num2 = 12
output = num1 - num2
print("Subtraction is: ", output)
# output -> Subtraction is: 33

# Multiplication
num1 = 3
num2 = 6
output = num1 * num2
print("Multiplication is: ", output)
# Output -> Multiplication is: 18

num1 = 78
num2 = 34
output = num1 * num2
print("Multiplication is: ", output)
# Output -> Multiplication is: 2652

# Division with /  -> returns float
num1 = 24
num2 = 5
output = num1 / num2
print("Division is: ", output)
# Output -> Division is: 4.8

num1 = 80
num2 = 4
output = num1 / num2
print("Division is: ", output)
# Output -> Division is: 20.0

# Division with // -> returns integer
num1 = 14
num2 = 3
output = num1 // num2
print("Division is: ", output)
# Output -> Division is: 4

num1 = 24
num2 = 6
output = num1 // num2
print("Division is: ", output)
# Output -> Division is: 4

# Remainder Operator
num1 = 24
num2 = 5
output = num1 % num2
print("Remainder is: ", output)
# Output -> Remainder is: 4

num1 = 23
num2 = 2
output = num1 % num2
print("Remainder is: ", output)
# Output -> Remainder is: 1

# Power Operator
num1 = 6
num2 = 3
output = num1 ** num2
print("Answer is: ", output)
# Output -> Answer is: 216

num1 = 2
num2 = 8
output = num1 ** num2
print("Answer is: ", output)
# Output -> Answer is: 256