"""
--> dict contains key - pair values
--> dictionary contains unique values, no duplicate values allowed
--> any data can be a a part of "value"  like int, float, string, list, tuple, dict
--> only immutable data type can become "key"  like dict, int, float, string, tuple
--> dict dos not follow indexing

dict1 = {'a' : 3456, 'b' : 7643}
print(dict1)
# {'a': 3456, 'b': 7643}

print(dict1['a'])
# 3456

# duplicate values are not allowed, if we write it, it will take the latest value of the same key
dict1 = {'a' : 3456, 'b' : 7643, 'b' : 345}
print(dict1)
# {'a': 3456, 'b': 345}

dict1['a'] = 56301563
print(dict1)
# {'a': 56301563, 'b': 345}

# add string as value in dict
dict1[(2, 4, 6)] = "Good morning"
print(dict1)
# {'a': 56301563, 'b': 345, (2, 4, 6): 'Good morning'}

# add set as value in dict
dict1['amit'] = {4, 6, 8, 3}
print(dict1)
# {'a': 56301563, 'b': 345, (2, 4, 6): 'Good morning', 'amit': {8, 3, 4, 6}}

# boolean values as key in dict
dict1[True] = "aditya"
print(dict1)
# {'a': 56301563, 'b': 345, (2, 4, 6): 'Good morning', 'amit': {8, 3, 4, 6}, True: 'aditya'}

# add list as key in dict
dict1[[4, 5, 9]] = "asach"
print(dict1)
# TypeError: unhashable type: 'list'

print(dir(dict)) ----------------------------------------------------------------------------------------------------------------------------------------------
'clear', 'copy', 'fromkeys', 'get', 'items',
'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

# clear method (to clear the dictionary) ----------------------------------------------------------------------------------------------------------
dict1 = {'a' : 123, 'b' : 456, 'c' : 789, 'd' : 142}
dict1.clear()
print("Dictionary after clear  : ", dict1)
# Dictionary after clear  :  {}

# copy method (to copy dictionary into another dictionary) -------------------------------------------------------------------------------
dict1 = {'a' : 123, 'b' : 456, 'c' : 789, 'd' : 142}
dict2 = dict1.copy()
print("Dict2 : ", dict2)
# Dict2 :  {'a': 123, 'b': 456, 'c': 789, 'd': 142}

# Get method (get value by giving key to get method) --------------------------------------------------------------------------------------
dict1 = {'a' : 123, 'b' : 456, 'c' : 789, 'd' : 142}
var = dict1.get('b')
print("value of var : ", var)
# value of var :  456

# items method (separate keys and values from the dictionary) --------------------------------------------------------------------------
dict1 = {'a' : 123, 'b' : 456, 'c' : 789, 'd' : 142}
print(dict1.items())
# dict_items([('a', 123), ('b', 456), ('c', 789), ('d', 142)])

dict1 = {'a' : 123, 'b' : 456, 'c' : 789, 'd' : 142}
for keys, values in dict1.items() :
    print("Key : ", keys, "     value : ", values)
# Key :  a      value :  123
# Key :  b      value :  456
# Key :  c      value :  789
# Key :  d      value :  142

# pop method (method to pop the key value pair by giving the key)
dict1 = {'a' : 123, 'b' : 456, 'c' : 789, 'd' : 142}
var = dict1.pop('c')
print("pop value : ", var)
print("dict1after pop : ", dict1)
# pop value :  789
# dict1after pop :  {'a': 123, 'b': 456, 'd': 142}

# popitem method (pop key value pair inserted at last from dictionary) ----------------------------------------------------------------------
dict1 = {'a' : 123, 'b' : 456, 'c' : 789, 'd' : 142}
dict1.popitem()
print("dict1 after popitem : ", dict1)
# dict1 after popitem :  {'a': 123, 'b': 456, 'c': 789}

# update method (to update a dictionary with another) ----------------------------------------------------------------------------------------
dict1 = {'a' : 123, 'b' : 456, 'c' : 789, 'd' : 142}
dict2 = {'d' : 453, 'e' : 697}
dict1.update(dict2)
print("Dict1 after update : ", dict1)
# Dict1 after update :  {'a': 123, 'b': 456, 'c': 789, 'd': 453, 'e': 697}

# fromkeys method (provide multiple keys a single value) -----------------------------------------------------------
keys = ('a', 'b', 'c', 'd')
values = (123)
output = dict.fromkeys(keys, values)
print(output)
# {'a': 123, 'b': 123, 'c': 123, 'd': 123}

# setdefault method ----------------------------------------------------------------------------------------------------------------------------------------------
# (return value for specified key, if key doesnot exist, insert the key with specified value)

dict1 = {'a' : 123, 'b' : 456, 'c' : 789, 'd' : 142}
var = dict1.setdefault('c', 2345678)        # key is present so return it's value
print(var)
# 789

var = dict1.setdefault('e', 2345678)        # key is not present so insert it
print(var)
# 2345678
---------------------------------------------------------------------------------------------------------------------------------------------
# program to move elements of a dictionary to another (by popitem method)
dict11 = {'a': 1234, 'b': 345, 'c': 67, 'd': 98}
dict22 = {}
for i in range(len(dict11)) :
    var = dict11.popitem()
    dict22[var[0]] = var[1]
print("dict11 : ", dict11)
print("dict22 : ", dict22)
# dict11 :  {}
# dict22 :  {'d': 98, 'c': 67, 'b': 345, 'a': 1234}
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# program to move elements of a dictionary to another (by pop method)
dicta = {'a': 1234, 'b': 345, 'c': 67, 'd': 98}
dictcopy = dicta.copy()
dictb = {}
for key, value in dictcopy.items() :
    var = dicta.pop(key)
    dictb[key] = value
print("dicta : ", dicta)
print("dictb : ", dictb)
# dicta :  {}
# dictb :  {'a': 1234, 'b': 345, 'c': 67, 'd': 98}
"""
"""
--> dict contains key - pair values
--> dictionary contains unique values, no duplicate values allowed
--> any data can be a a part of "value" of a key like int, float, string, list, tuple, dict
--> only immutable data type can become "key"  like dict, int, float, string, tuple
--> dict dos not follow indexing

dict1 = {'a' : 3456, 'b' : 7643}
print(dict1)
# {'a': 3456, 'b': 7643}

print(dict1['a'])
# 3456

# duplicate values are not allowed, if we write it, it will take the latest value of the same key
dict1 = {'a' : 3456, 'b' : 7643, 'b' : 345}
print(dict1)
# {'a': 3456, 'b': 345}

dict1['a'] = 56301563
print(dict1)
# {'a': 56301563, 'b': 345}

# add string as value in dict
dict1[(2, 4, 6)] = "Good morning"
print(dict1)
# {'a': 56301563, 'b': 345, (2, 4, 6): 'Good morning'}

# add set as value in dict
dict1['amit'] = {4, 6, 8, 3}
print(dict1)
# {'a': 56301563, 'b': 345, (2, 4, 6): 'Good morning', 'amit': {8, 3, 4, 6}}

# boolean values as key in dict
dict1[True] = "aditya"
print(dict1)
# {'a': 56301563, 'b': 345, (2, 4, 6): 'Good morning', 'amit': {8, 3, 4, 6}, True: 'aditya'}

# add list as key in dict
dict1[[4, 5, 9]] = "asach"
print(dict1)
# TypeError: unhashable type: 'list'

print(dir(dict)) ----------------------------------------------------------------------------------------------------------------------------------------------
'clear', 'copy', 'fromkeys', 'get', 'items',
'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

# clear method (to clear the dictionary) ----------------------------------------------------------------------------------------------------------
dict1 = {'a' : 123, 'b' : 456, 'c' : 789, 'd' : 142}
dict1.clear()
print("Dictionary after clear  : ", dict1)
# Dictionary after clear  :  {}

# copy method (to copy dictionary into another dictionary) -------------------------------------------------------------------------------
dict1 = {'a' : 123, 'b' : 456, 'c' : 789, 'd' : 142}
dict2 = dict1.copy()
print("Dict2 : ", dict2)
# Dict2 :  {'a': 123, 'b': 456, 'c': 789, 'd': 142}

# Get method (get value by giving key to get method) --------------------------------------------------------------------------------------
dict1 = {'a' : 123, 'b' : 456, 'c' : 789, 'd' : 142}
var = dict1.get('b')
print("value of var : ", var)
# value of var :  456

# items method (separate keys and values from the dictionary) --------------------------------------------------------------------------
dict1 = {'a' : 123, 'b' : 456, 'c' : 789, 'd' : 142}
print(dict1.items())
# dict_items([('a', 123), ('b', 456), ('c', 789), ('d', 142)])

dict1 = {'a' : 123, 'b' : 456, 'c' : 789, 'd' : 142}
for keys, values in dict1.items() :
    print("Key : ", keys, "     value : ", values)
# Key :  a      value :  123
# Key :  b      value :  456
# Key :  c      value :  789
# Key :  d      value :  142

# pop method (method to pop the key value pair by giving the key) ----------------------------------------------------------------------------
dict1 = {'a' : 123, 'b' : 456, 'c' : 789, 'd' : 142}
var = dict1.pop('c')
print("pop value : ", var)
print("dict1after pop : ", dict1)
# pop value :  789
# dict1after pop :  {'a': 123, 'b': 456, 'd': 142}

# popitem method (pop key value pair inserted at last from dictionary) ----------------------------------------------------------------------
dict1 = {'a' : 123, 'b' : 456, 'c' : 789, 'd' : 142}
dict1.popitem()
print("dict1 after popitem : ", dict1)
# dict1 after popitem :  {'a': 123, 'b': 456, 'c': 789}

# update method (to update a dictionary with another) ----------------------------------------------------------------------------------------
dict1 = {'a' : 123, 'b' : 456, 'c' : 789, 'd' : 142}
dict2 = {'d' : 453, 'e' : 697}
dict1.update(dict2)
print("Dict1 after update : ", dict1)
# Dict1 after update :  {'a': 123, 'b': 456, 'c': 789, 'd': 453, 'e': 697}

# fromkeys method (provide multiple keys a single value) -----------------------------------------------------------
keys = ('a', 'b', 'c', 'd')
values = (123)
output = dict.fromkeys(keys, values)
print(output)
# {'a': 123, 'b': 123, 'c': 123, 'd': 123}

# setdefault method ----------------------------------------------------------------------------------------------------------------------------------------------
# (return value for specified key, if key doesnot exist, insert the key with specified value)

dict1 = {'a' : 123, 'b' : 456, 'c' : 789, 'd' : 142}
var = dict1.setdefault('c', 2345678)        # key is present so return it's value
print(var)
# 789

var = dict1.setdefault('e', 2345678)        # key is not present so insert it
print(var)
# 2345678
---------------------------------------------------------------------------------------------------------------------------------------------
# program to move elements of a dictionary to another (by popitem method)
dict11 = {'a': 1234, 'b': 345, 'c': 67, 'd': 98}
dict22 = {}
for i in range(len(dict11)) :
    var = dict11.popitem()
    dict22[var[0]] = var[1]
print("dict11 : ", dict11)
print("dict22 : ", dict22)
# dict11 :  {}
# dict22 :  {'d': 98, 'c': 67, 'b': 345, 'a': 1234}
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# program to move elements of a dictionary to another (by pop method)
dicta = {'a': 1234, 'b': 345, 'c': 67, 'd': 98}
dictcopy = dicta.copy()
dictb = {}
for key, value in dictcopy.items() :
    var = dicta.pop(key)
    dictb[key] = value
print("dicta : ", dicta)
print("dictb : ", dictb)
# dicta :  {}
# dictb :  {'a': 1234, 'b': 345, 'c': 67, 'd': 98}

# delete the dictionary ------------------------------------------------------------------------------------------------------------------------------------------
dictb =  {'a': 1234, 'b': 345, 'c': 67, 'd': 98}
del dictb
print(dictb)
# NameError: name 'dictb' is not defined. Did you mean: 'dict'?

# keys method (return list of keys of the dictionary) -----------------------------------------------------------------------------------------------------
dictb =  {'a': 1234, 'b': 345, 'c': 67, 'd': 98}
output = dictb.keys()
print("List of keys : ", output)
# List of keys :  dict_keys(['a', 'b', 'c', 'd'])

# values method (returns list of values from the dictionary) -----------------------------------------------------------------------------------------
dictb =  {'a': 1234, 'b': 345, 'c': 67, 'd': 98}
output = dictb.values()
print("List of values : ", output)
# List of values :  dict_values([1234, 345, 67, 98])


# move data from one dictionary to another dictionary
dict1 = {'a': 456, 'b' : 234, 'p': 567}
dict2 = dict1.copy()
output = {}
for key in dict2  :
    data = dict1.pop(key)
    output[key] = data
print("Original dicttionary :", dict1)
print("Output :", output)
# Original dicttionary : {}
# Output : {'a': 456, 'b': 234, 'p': 567}
-----------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a python program to provide salary increment to the employee on the basis of years of experience
if exp > 10 : 20% increment
if exp >= 5 and exp < 10 : 10% increment
if exp < 5  then : 5% increment

employee = [
    {'name': 'Vrunda', 'email': 'vrunda@gmail.com', 'experience' : '5yr', 'salary': 500000},
    {'name': 'Amit', 'email': 'Amit@gmail.com', 'experience' : '7yr', 'salary': 600000},
    {'name': 'Amar', 'email': 'Amar@gmail.com', 'experience' : '8yr', 'salary': 700000},
    {'name': 'Janardhan', 'email': 'Janardhan@gmail.com', 'experience' : '10yr', 'salary': 1000000},
    {'name': 'Vishal', 'email': 'Vishal@gmail.com', 'experience' : '4yr', 'salary': 400000},
]
for emp in employee :
    if int(emp['experience'][0]) < 5 :
        temp = emp.pop('salary')
        sal = temp + (temp * 0.05)
        emp['salary'] = sal

    elif int(emp['experience'][0]) >= 5  and int(emp['experience'][0]) < 10 :
        temp = emp.pop('salary')
        sal = temp + (temp * 0.1)
        emp['salary'] = sal

    elif int(emp['experience'][0]) > 10 :
        temp = emp.pop('salary')
        sal = temp + (temp * 0.2)
        emp['salary'] = sal

print("Updated employee list :")
for val in employee :
    print(val)
    
# Updated employee list :
# {'name': 'Vrunda', 'email': 'vrunda@gmail.com', 'experience': '5yr', 'salary': 550000.0}
# {'name': 'Amit', 'email': 'Amit@gmail.com', 'experience': '7yr', 'salary': 660000.0}
# {'name': 'Amar', 'email': 'Amar@gmail.com', 'experience': '8yr', 'salary': 770000.0}
# {'name': 'Janardhan', 'email': 'Janardhan@gmail.com', 'experience': '10yr', 'salary': 1050000.0}
# {'name': 'Vishal', 'email': 'Vishal@gmail.com', 'experience': '4yr', 'salary': 420000.0}
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
# Write a python pogram to get bill on the basis of user purchase
"""
-> apply loop on fruit_purchase dict and get fruit name quatity "for fruit, qua  in fruit_purchase.items()"
-> Get each fruit_bill = fruit_qua * fruit price : "qua*fruit_price[fruit]"
-> add each fruit bill in total amount : "total_amount = total_amount + fruit_bill"
-> update fruit_stock dict data with reduce each fruit quantity  : fruit_stock[fruit] = fruit_stock[fruit] - qua
-> add each fruit bill in output_dict
"""
'''
Output_bill_amount = {}
total_amount = 0

fruit_stock = {'apple': 20, 'banana' : 25, 'mango': 50}
fruit_price = {'apple': 50, 'banana' : 10, 'mango': 100}
fruit_purchase = {'apple': 5, 'banana' : 10, 'mango': 6}

for fruit, qua in fruit_purchase.items():
    fruit_bill = fruit_price[fruit]*qua
    total_amount = total_amount + fruit_bill
    fruit_stock[fruit] = fruit_stock[fruit] - qua
    Output_bill_amount[fruit] = fruit_bill

print("_"*50)
print("Total Amount :", total_amount)
print("Each Fruit Bill :", Output_bill_amount)
print("Remainig Stock:", fruit_stock)

print("_"*50)
for fruit, bill in Output_bill_amount.items():
    print(fruit ,":", fruit_purchase[fruit], ":", fruit_price[fruit],":", bill)

print("Total Bill :",  total_amount)
'''
print(dir(list))