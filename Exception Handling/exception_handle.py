'''
syntax -->
try :
    code that may cause error
except Exception as e(any name) :
    print(customized messgae)
    print(e) from line 5
'''
'''
try :
    num1 = 456
    str1 = 'hello'
    output = num1 + str1
except Exception as e :
    print(e)
    print('Addition of number and string is not possible')
# unsupported operand type(s) for +: 'int' and 'str'
# Addition of number and string is not possible
--------------------------------------------------------------------------------------------------------------------------

# try --> except --> else : If there is no exception in the program then else part will get executed.
try :
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print('addition :', sum)
except Exception as e :
    print(f'something is broken : {e}')
else :
    output = num1 + num2
    print('multiply value :', output*2)
# addition : 90
# multiply value : 180
---------------------------------------------------------------------------------------------------------------------------

# try --> except --> finally : code present in finally block always executes
# even there is exception or no exception in the code
list1 = [7,8,9,2]
list2 = ['a', 'b', 567, 23]
try :
    for val in list1 :
        print(val, ':', val**2)

    # assert sum(list1) == 50
    # with open('read.txt', 'r') as file:
    #     data = file.write
except AssertionError:
    print('Assertion error')
except IOError:
    print('IO error')
except ArithmeticError:
    print('Arithemtaic error')

finally :
    print('#'*30)
    for val in list2 :
        print(val, ':', val*2)
# 7 : 49
# 8 : 64
# 9 : 81
# 2 : 4
# ##############################
# a : aa
# b : bb
# 567 : 1134
# 23 : 46
-------------------------------------------------------------------------------------------------------------------------

# try --> except --> else --> finally
# else condition only executes when there is no exception in the code.

list1 = [7,8,9,2]
list2 = ['a', 'b', 567, 23]
try :
    for val in list1 :
        print(val, ':', val**2)

    # assert sum(list1) == 50
    # with open('read.txt', 'r') as file:
    #     data = file.write
except AssertionError:
    print('Assertion error')
except IOError:
    print('IO error')
except ArithmeticError:
    print('Arithemtaic error')
else :
    print('There is no exception in the code')

finally :
    print('#'*30)
    for val in list2 :
        print(val, ':', val*2)
# 7 : 49
# 8 : 64
# 9 : 81
# 2 : 4
# There is no exception in the code
# ##############################
# a : aa
# b : bb
# 567 : 1134
# 23 : 46
-----------------------------------------------------------------------------------------------------------------------------

# nested exception
num1 = 40
num2 = 50
try :
    print('We are in first exception block')
    print('addition :', num1 + num2)
    try :
        print('we are in second exception')
        print('addition :', num1/0)
    except Exception as e:
        print('second exception raised')
except Exception as var:
    print('first exception raised')
# We are in first exception block
# addition : 90
# we are in second exception
# second exception raised
'''

def subtract(n1, n2) :
    try :
        num3 = n1 - n2
        print('subtraction', num3)
    except Exception as e :
        print('asach')
        print(e)
        # raise(e)
        print('amit')

subtract(5,'amit')