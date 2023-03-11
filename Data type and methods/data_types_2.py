"""
Python data types
1) Numbers :
        a) Integer
        b) Float
        c) Imaginary

2) Sequence :
        a) String
        b) List
        c) Tuple

3) Dictionary
    a) Sets
    b) Boolean
"""
"""
# b) List
list1 = [1, 3, 'amit', 'vrunda', 2.3]
print(list1)
# [1, 3, 'amit', 'vrunda', 2.3]

list2 = [3, 7, 1, 6, 6.8, 7.22, ['vrunda', 'arati']]
print(list2)
# [3, 7, 1, 6, 6.8, 7.22, ['vrunda', 'arati']]

# append
list2.append(4)
print(list2)
# [3, 7, 1, 6, 6.8, 7.22, ['vrunda', 'arati'], 4]

# extend
list2.extend([4, 5, 6])
print(list2)
# [3, 7, 1, 6, 6.8, 7.22, ['vrunda', 'arati'], 4, 4, 5, 6]

# remove
list2.remove(7.22)
print(list2)
# [3, 7, 1, 6, 6.8, ['vrunda', 'arati'], 4, 4, 5, 6]

list2.remove(['vrunda', 'arati'])
print(list2)

# indexing
print(list2[5])

# slicing
print(list2[2:5])

# length
print(len(list2))

# c) tuple
tup1 = ()
print(tup1)
# []

tup2 = (3, 4, 5.7, 'amit')
print(tup2, type(tup2))
# (3, 4, 5.7, 'amit') <class 'tuple'>

tup3 = (9, 5, 'adi')
tup4 = tup2 + tup3
print(tup4)
# (3, 4, 5.7, 'amit', 9)

# indexing
print(tup2[4])
"""
"""
############################# 3) Dictionary ####################################
dict1  ={'name' : 'amit'}
print(dict1, type(dict))
# {'name': 'amit'} <class 'type'>

dict1[9] = 'jadhav'
print(dict1)
# {'name': 'amit', 9: 'jadhav'}

dict1[8] = 6
print(dict1)
# {'name': 'amit', 9: 'jadhav', 8 : 6}

dict1['ait'] = (1, 4, 7, 'omkar')
print(dict1)
"""
# a) Set
set1 = {1, 4, 'amit'}
print(set1, type(set1))
# {1, 4, 'amit'} <class 'set'>

set2 = {1,1,1,1,1,1}
print(set2)
# {1}

# b) Boolean
a = 7
b = 8
print(a == b)
# False

c = d = 12
print(c == d)
# True