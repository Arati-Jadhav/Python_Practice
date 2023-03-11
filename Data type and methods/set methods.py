"""
--> Set is mutable data type. We can modify data in the set.
--> Set is unstructured data type so it does not follow any indexing.
--> Set contains only unique values. Duplicate values are not allowed.
--> We can add any data type in the set except list and dictionary.
"""
'''
set1 = {1, 2, 6, 4, 3, 9}
print(set1, type(set1))
# {1, 2, 3, 4, 6, 9} <class 'set'>

# Set methods -->
print(dir(set))
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 
# 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 
# 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

# add method (add element to set) ----------------------------------------------------------------------------------------------------------------------
input = {1, 2, 3, 4, 5}
input.add(8)
print("After adding 8 :", input)
# After adding 8 : {1, 2, 3, 4, 5, 8}

# add list to set -------------------------->
input = {1, 2, 3, 4, 5}
input.add([1, 5, 'g'])
print("After adding list : ", input)
# TypeError: unhashable type: 'list'

# add dictionary to set ---------------------->
input = {1, 2, 3, 4, 5}
input.add({'a' : 123})
print("After adding ditionary :", input)
# TypeError: unhashable type: 'dict'

# update method (update data from one set to another) ------------------------------------------------------------------------------------------
input = {1, 2, 3, 4, 5}
set2 = {7, 8, 9}
input.update(set2)
print("After update : ", input)
# After update :  {1, 2, 3, 4, 5, 7, 8, 9}

# Remove method (remove data from set by giving element) -----------------------------------------------------------------------------------
input = {1, 2, 3, 4, 5}
input.remove(3)
print("After removing 3 :", input)
# After removing 3 : {1, 2, 4, 5}

# pop method (remove data from set randomly) ---------------------------------------------------------------------------------------------------
input = {1, 2, 3, 4, 5}
input.pop()     # pop doesn't take any arguments in set method
print("After popping random element : ", input)
# After popping random element :  {2, 3, 4, 5}

# clear method (clear the content of the set) ------------------------------------------------------------------------------------------------------
input = {1, 2, 3, 4, 5}
input.clear()
print("After clearing :", input)
# After clearing : set()

# shallow copy method (both variables point to single meory area) -----------------------------------------------------------------------
input = {1, 2, 3, 4, 5}
set1 = input
print("set1 : ", set1)
print("input :", input)
# set1 :  {1, 2, 3, 4, 5}
# input : {1, 2, 3, 4, 5}

# make change in set1 --->
set1.add(45)
print("set1 : ", set1)
print("input :", input)
# set1 :  {1, 2, 3, 4, 5, 45}
# input : {1, 2, 3, 4, 5, 45}

# deep copy method (separate memory area) ----------------------------------------------------------------------------------------------------------------
input = {1, 2, 3, 4, 5}
set1 = input.copy()
print("set1 :", set1)
print("input :", input)
# set1 : {1, 2, 3, 4, 5}
# input : {1, 2, 3, 4, 5}

set1.add(45)
print("set1 :", set1)
print("input :", input)
# set1 : {1, 2, 3, 4, 5, 45}
# input : {1, 2, 3, 4, 5}

# union method (union of 2 sets) -------------------------------------------------------------------------------------------------------------------------
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
output = set1.union(set2)
print('Union of 2 sets : ', output)
# Union of 2 sets :  {1, 2, 3, 4, 5, 6, 7}

# difference between 2 sets (uncommon elements from the set written at the left) ----------------------------------------------------
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
output = set1.difference(set2)      # uncommon from set1
print('set1 - set2 :', output) 
# set1 - set2 : {1, 2}

out = set2.difference(set1)     # uncommon from set2
print('set2 - set1 :', out)
# set2 - set1 : {6, 7}
'''

a=4
print(type(a))