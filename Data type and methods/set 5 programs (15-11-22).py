'''
# Program1 :Write a python program to find out common values between two list
# list1 = [5, 7, 2, 8, 1]
# list2 = [3, 6, 2, 7, 1, 9]
# output = [7, 2, 1]

list1 = [5, 7, 2, 8, 1]
list2 = [3, 6, 2, 7, 1, 9]
set1 = set(list1)
set2 = set(list2)
output = set1.intersection(set2)
print("Intersection : ", output)
# Intersection :  {1, 2, 7}

Alternative approach -----------------------------------------------------------
list1 = [5, 7, 2, 8, 1]
list2 = [3, 6, 2, 7, 1, 9]
output = []
for val in list1 :
    if val in list2 :
        output.append(val)
print('Intersection :', output)
# Intersection : [7, 2, 1]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Program2 : Find out all the uncommon values between two tuples.
# tup1 = (5, 7, 2, 8, 1)
# tup2 = (1, 7, 12, 56, 8)
# output = (5,  12, 56, 2)

tup1 = (5, 7, 2, 8, 1)
tup2 = (1, 7, 12, 56, 8)
set1 = set(tup1)
set2 = set(tup2)
output = set1.symmetric_difference(set2)
print("Symmetric difference :", output)
# Symmetric difference : {2, 5, 56, 12}

Alternative approach -----------------------------------------------------------
tup1 = (5, 7, 2, 8, 1)
tup2 = (1, 7, 12, 56, 8)
output = []
list1 = list(tup1)
list2 = list(tup2)
for val in list1 :
    if val not in list2 :
        output.append(val)
for v in list2 :
    if v not in list1 :
        output.append(v)
out = tuple(output)
print('Symmetric difference : ', out)
# Symmetric difference :  (5, 2, 12, 56)
----------------------------------------------------------------------------------------------------------------------------------------------------
# Program3 : Find out all the uncommon values between two dict values
# dict1 = {'a' : [4, 7, 8, 2, 8], 'b': [3, 6, 1, 8], 'c': [2, 5, 1, 7, 9]}
# dict2 = {'a' : [14, 17, 8, 2, 18], 'b': [13, 6, 1, 88], 'e': [2, 5, 1, 7, 9]}
# output_dict = {'a' : [14, 17, 4, 7], 'b': [3, 13, 88]}

dict1 = {'a' : [4, 7, 8, 2, 8], 'b': [3, 6, 1, 8], 'c': [2, 5, 1, 7, 9]}
dict2 = {'a' : [14, 17, 8, 2, 18], 'b': [13, 6, 1, 88], 'e': [2, 5, 1, 7, 9]}
output = {}
for k1, v1 in dict1.items() :
    for k2, v2 in dict2.items() :
        if k1 == k2 :
            set1 = set(v1)
            set2 = set(v2)
            out = set1.symmetric_difference(set2)
            temp = list(out)
            output[k1] = temp
        else :
            continue
print("Output :", output)
# Output : {'a': [17, 18, 4, 7, 14], 'b': [3, 8, 13, 88]}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Program 4 : Write a python program to calculate factorial of all prime number
# list1= [1, 2, 4, 6, 7, 14, 13]
# output4 = [(1, 1), (2, 2), (7, 5040), (13, 6227020800)]

list1= [1, 2, 4, 6, 7, 14, 13]
output = []
for val in list1:
        prime = True
        for i in range(2, val):
                if val % i == 0:
                        prime = False
                        break
        if prime:
            temp = 1
            for i in range(1, val + 1, 1):
                temp *= i
            output.append((val, temp))
print("Output :", output)
# Output : [(1, 1), (2, 2), (7, 5040), (13, 6227020800)]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Program 5 : Write a python manipulate the string
# re-arrange the string where odd index words will come first and even index words will come last.
# input = "Hey very good Morning"
# Output = "very Morning Hey Good"

output = ''
s = ''
input = "Hey very good Morning"
mid = input.split(" ")
for i in range(len(mid)) :
    if i % 2 == 0 :
        output = output + mid[i]
        output = output + ' '
    else :
        s = s+ mid[i]
        s = s + ' '
s = s + output
print("Output :", s)
# Output : very Morning Hey good
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''