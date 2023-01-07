"""
try:
    num1 = 123
    output = num1/0
    print(output)
except Exception as e:
    print('division by zero is not allowed')
    print(e)



try:
    num2 = 456
    str1 = 'Arati'
    print(num2 + str1)
except Exception as e:
    print('addition of number and string is not possible')
    # print(e)
    raise

# try ->except->else:If there isno exception in the program then else condition will be executed.
try:
    num11 = 50
    num22 = 100
    print('addition :',num11 + num22)
except Exception as e:
    print(e)
else:
    output = num11 + num22
    print('multiply values :',output*2)
# In above code it will not throw the exception because code is right.

try:
    num11 = 50
    num22 = '100'
    print('addition :',num11 + num22)
except Exception as e:
    print(e)
else:
    output = num11 + num22
    print('multiply values :',output*2)
# In above code it throw an exception because code was wrong.


# try  -> except -> finally :code present finally block always executes even
# there is exception or not in the code.
list1 = [4,8,6,2,3,4]
list2 = ['b','c',444,897]
try:
    for val in list1:
        print(val ,':',val**2)
# # except Exception as e:
# #     print(e)
#     assert  sum(list1) == 50
#     with open('readfile.txt','r') as file:
#         data = file.write('file')
#         print(data)
# except AssertionError:
#     print("Assertion Error")
# except IOError:
#     print('IOError')
# except ArithmeticError:
#     print('ArithmeticError')

finally:
    for val in list2:
        print(val,':',val*2)

# try ->except -> else ->finally :
# else condition only executes when there is no exception in the code:
list11 = [4,8,6,2,3,4]
list22 = ['b','c',444,897]
try:
    for val in list11:
        print(val , ':' ,val**2)

except Exception as e:
    print(e)
else:
    print('there is exception in the code')

finally:
    for val in list22:
        print(val , ':',val*2)

# Nested Exception:
num1 = 10
num2 = 40
try:
    print('we are first exception block')
    print('Addition :',num1 + num2)
    try:
        print('we are second exception block')
        print("division :",num1/0)
    except Exception as e:
        print('second exception raised :',e)
except Exception as var:
    print('first exception raised :',var)
"""