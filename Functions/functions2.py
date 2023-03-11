# return value from function
def addition(n1, n2) :
    output = n1 + n2
    return output

def multiply(nu1, nu2) :
    return nu1 * nu2

n1 = 20
n2 = 30
nu1 = 12
nu2 = 6

var1 = addition(n1, n2)
print('result of addition : ', var1)
# result of addition :  50

var2 = multiply(nu1, nu2)
print('result of multiplication : ', var2)
# result of multiplication :  72

var3 = addition(34, 67)
print('result of addition : ', var3)
# result of addition :  101

var4 = multiply(34,7)
print('result of multiplication : ', var4)
# result of multiplication :  238

# we can give data type of variable in parameter list for expected datatype
# we can write documentation in function and show it with magic method
#  __doc__
# syntax  --->  fun_name.__doc__

def provide_default()  :
    return 5

def factorial(num: int) :
    '''
    this function will provide factorial of given number.
    factorial means multiplying that number with number less than it
    till 1. E.g. 5! = 5 * 4 * 3 * 2 * 1= 120
    :param num:
    :return:
    '''
    if num == 0 :
        num = provide_default()
    fact = 1
    for i in range(num, 0, -1) :
        fact *= i
    return fact

print("Factorial : ", factorial(10))
# Factorial :  3628800

print("Factorial : ", factorial(0))
# Factorial :  120

print(factorial.__doc__)        # magic method to print documentation
# this function will provide factorial of given number.
#     factorial means multiplying that number with number less than it
#     till 1. E.g. 5! = 5 * 4 * 3 * 2 * 1= 120
#     :param num:
#     :return:
