# Write a python program to add data from list to set
# list1 = [5, 7, 2.6, 'Python', (3, 6, 2), [5, 6], {'a': 345, 'b': 123}]
# output_set = {5, 7, 2.6, (3, 6, 2), 'Python'}
"""
list1 = [5, 7, 2.6, 'Python', (3, 6, 2), [5, 6], {'a': 345, 'b': 123}]
output = set()
for val in list1 :
    if isinstance(val, list) :
        continue
    elif isinstance(val, dict) :
        continue
    else :
        output.add(val)
print("Output :", output)
# Output : {2.6, 5, 7, 'Python', (3, 6, 2)}
-------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Python Program to copy content from set to another with its square and if it is string then repeat it two times.
# set1 = {6, 2, 7, 1, 'b', 8, 23, 14, 'a'}
# output = {'square of all the popped values'}

set1 = {6, 2, 7, 1, 'b', 8, 23, 14, 'a'}
set2 = set1.copy()
output = set()
for val in set2 :
    if isinstance(val, int) : 
        temp = set1.pop()
        output.add(temp ** 2)
    elif isinstance(val, str) :
        temp = set1.pop()
        output.add(temp * 2)
print("Output :", output)
print("set1 :", set1)
# Output : {64, 1, 4, 36, 196, 'aa', 'bb', 49, 529}
# set1 : set()
-----------------------------------------------------------------------------------------------------------------------------------------------------------
"""