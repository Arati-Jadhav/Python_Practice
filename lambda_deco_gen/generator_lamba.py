'''
lambda is used to write anonymous functions
'''
from functools import reduce
'''
result = lambda x, y : x+y
print(result(52,18))
# 70

# map, reduce, filter

# map -> run the given function for each value from the bulk data

def fact_get(n):
    fact = 1
    for i in range(n,0,-1):
        fact *= i
    return fact

list1 = [1,2,6,3]
result = list(map(fact_get, list1))
print(result)
# [1, 2, 720, 6]

square = list(map(lambda x:x**2, list1))
print(square)
# [1, 4, 36, 9]

# filter -> to filter the data of output
even_val = list(filter(lambda x : x%2==0, list1))
print(even_val)
# [2, 6]

# reduce -> used to get data one by one
output = reduce(lambda x,y:x+y, list1)
print('addition :', output)
# addition : 12
'''

# generator

def print_msg():
    return 'Good morning'
    return 'hello how are you'

output = print_msg()
#print(output)
# Good morning

def gen_print_msg():
    yield 'hello 1'
    yield 'hello 2'
    yield 'hello 3'

gen_data = gen_print_msg()
print(gen_data)
print(next(gen_data))
print(next(gen_data))
print(next(gen_data))
# hello 1
# hello 2
# hello 3

list1 = [3,6,2,9]
def get_square_all_numbers(list1):
    for data in list1:
        yield data**2

gen_obj = get_square_all_numbers(list1)

for val in gen_obj:
    print(val)
# 9
# 36
# 4
# 81

