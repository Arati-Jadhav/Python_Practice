'''
def original_fun(ori_msg):
    output = ori_msg + '!!!!!!!'
    return output

def deco(f):
    print('in the decorator')
    out = original_fun('I am learning python')
    print(out)
    print('exiting the decorator')

deco(original_fun)


def greeting2(f):
    def inner(msg):
        print('in the decorator')
        out = f(msg)
        print(out)
        print('exiting the decorator')
    return inner

@greeting2
def ori(msg):
    output = msg + '!!!!!!!'
    return output

ori('I am learning python')
'''

import os
from faker import Faker
fk = Faker()

def create_fake_data():    # function to generate data
    file_name = 'data.txt'
    with open(file_name, 'w') as file:
        for i in range(10):
            fname = fk.first_name()
            lname = fk.last_name()
            email = fk.email()
            line = f"{fname}, {lname}, {email} \n"
            file.write(line)
    print('in the generator')
    return file_name

def generate_fake_data(fun):    # main decorator
    def inner(*args):
        print('in the decorator')
        filen = create_fake_data()
        fun(filen)
        os.remove(filen)
        print('exiting decorator')
    return inner

@generate_fake_data
def show_data(filen):   # function to show data but called by the decorator
    print('in the show function')
    with open(filen, 'r') as file:
        all_lines = file.readlines()
        for line in all_lines:
            print(line)

show_data()
# after calling this function first the decorator get called and
# execution sequence of all functions is decided by decorator and it's inner function

# execution sequence for this whole process -->
# 1. generate_fake_data()
# 2. inner() function of generate_fake_data
# 3. create_fake_data()
# 4. show_data()
##############################################################################################

# output -->
# in the decorator
# in the generator
# in the show function
# Dennis, Mcintosh, garciacassandra@example.org
# Brandon, Price, william72@example.net
# Ann, Moore, jenniferwerner@example.net
# James, Santos, kenneth47@example.com
# Jennifer, Jones, mitchellrobert@example.org
# Larry, Taylor, reyesjeffrey@example.com
# Tyler, Lee, ariasnicole@example.net
# Nathaniel, Dennis, maysdavid@example.net
# John, Parker, mcooper@example.net
# Annette, Rodriguez, zacharyfarley@example.net
# exiting decorator