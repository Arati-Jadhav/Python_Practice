'''
input = [{'a' :12}, {'b' : 34}, {'c' : 23}, {'d' : 11}, {'e' : 15}]
k = []
v = []
for val in input :
    for key, values in val.items() :
        k.append(key)
        v.append(values)
print(k)
print(v)
--------------------------------------
list1 = []
for i in range(4) :
    temp = []
    for j in range(1, 6, 1) :
        temp.append(5 * i + j)
    list1.append(temp)
print(list1)
--------------------------------------
input = [3, 5, 7, 8]
output = []
for val in input :
    output.append('a')
    output.append(val)
print(output)
'''
