import pandas as pd
'''
list1 = [43, 6, 2, 'x', 'y', 'z']
sr = pd.Series(list1)
print(sr)
# 0    43
# 1     6
# 2     2
# 3     x
# 4     y
# 5     z
# dtype: object

print(sr[0])
# 43

sr2 = pd.Series(list1, index = ['a','b','c','d','e','f'])
print(sr2)
# a    43
# b     6
# c     2
# d     x
# e     y
# f     z
# dtype: object

print(sr2['e'])
# y

# Create series with dictionary
dict1 = {'name': ['Rahul', 'mohit', 'akash'], 'age': [19, 23, 24], 'salary': [70000, 50000, 30000]}
sr3 = pd.Series(dict1)
print(sr3)
# name      [Rahul, mohit, akash]
# age                [19, 23, 24]
# salary    [70000, 50000, 30000]
# dtype: object

# Create Series with tuple
tup1 = (1,2,3,4,5)
sr4 = pd.Series(tup1)
print(sr4)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

# Create a series with set --> not allowed
set1 = {1,2,3,4}
#sr5 = pd.Series(set1)
#  raise TypeError(f"'{type(data).__name__}' type is unordered")
# TypeError: 'set' type is unordered

# Get unique data from series
list1 = [1,2,3,1,2,4,2,3]
sr = pd.Series(list1)
print(sr.unique())
# [1 2 3 4]
'''
############################################# Data Frame ###############################

dict1 = {
        'name':['amit', 'sanket','yogesh','mohit'],
        'age':[20,21,23,None],
        'address':['pune','mumbai','kolkata','banglore']
        }

df = pd.DataFrame(dict1, index=['a','b','c','d'])
'''
print(df)
#      name   age   address
# a    amit  20.0      pune
# b  sanket  21.0    mumbai
# c  yogesh  23.0   kolkata
# d   mohit   NaN  banglore

print(df['age'][0])
# 20.0

df['salary'] = [50000,30000,54000,70000]
print(df)
#      name   age   address  salary
# a    amit  20.0      pune   50000
# b  sanket  21.0    mumbai   30000
# c  yogesh  23.0   kolkata   54000
# d   mohit   NaN  banglore   70000

# delete any specific column from the data frame
del df['age']
print(df)
#      name   address  salary
# a    amit      pune   50000
# b  sanket    mumbai   30000
# c  yogesh   kolkata   54000
# d   mohit  banglore   70000

# update any specific data in the frame
df['salary']['a'] = 10000
#print(df)
# a    amit      pune   10000
# b  sanket    mumbai   30000
# c  yogesh   kolkata   54000
# d   mohit  banglore   70000

for data in df.iterrows():
    print(data)
# ('a', name       amit
# age        20.0
# address    pune
# Name: a, dtype: object)
# ('b', name       sanket
# age          21.0
# address    mumbai
# Name: b, dtype: object)
# ('c', name        yogesh
# age           23.0
# address    kolkata
# Name: c, dtype: object)
# ('d', name          mohit
# age             NaN
# address    banglore
# Name: d, dtype: object)

per_name = 'mohit'

for data in df.iterrows():
    print(data[1]['name'], data[1]['age'], data[1]['address'])
# amit 20.0 pune
# sanket 21.0 mumbai
# yogesh 23.0 kolkata
# mohit nan banglore
###################################################################################

import numpy as np

dict1 = {'bill' : [400, 700, 5000], 'grocery' : [6000, 8000, 7000]}

df = pd.DataFrame(dict1, index = ['Jan','Feb','Mar'])
df['total'] = df['bill'] + df['grocery']

print(df)
#      bill  grocery  total
# Jan   400     6000   6400
# Feb   700     8000   8700
# Mar  5000     7000  12000
'''
###############################################################################################
student1 = { 'name':['shivam','swanand','amit'],
            'age':[24,23,22],
            'address':['satara','pune','nagar']
          }

student2 = { 'name':['vrunda','swapnil','arati'],
            'age':[24,29,28],
            'address':['marunji','vimannagar','punawale']
          }

df1 = pd.DataFrame(student1)
df2 = pd.DataFrame(student2)
# print(df1)
# print(df2)

output = df1.append(df2, ignore_index = True)
#print(output)
'''
#print(output['name'])
list1 = []
for data in output.iterrows():
        list1.append(data[1]['age']*5)

output['age*5'] = list1

csv_data = output.to_csv()

with open('student.csv', 'a') as file:
        file.write(csv_data)
'''
# loc function to apply filter
data = output.loc[2, 'age']
print(data)
# 22

# get details with city name
data2 = output.loc[(output.address == 'pune') | (output.address == 'amit')]
print(data2)
# 1  swanand   23    pune

# get all whose age greater than 30
data3 = output.loc[(output.age >= 20)]
print(data3)
#       name  age     address
# 0   shivam   24      satara
# 1  swanand   23        pune
# 2     amit   22       nagar
# 3   vrunda   24     marunji
# 4  swapnil   29  vimannagar
# 5    arati   28    punawale

# get data on the basis of index
data5 = output.iloc[0:5]
print(data5)
#     name  age     address
# 0   shivam   24      satara
# 1  swanand   23        pune
# 2     amit   22       nagar
# 3   vrunda   24     marunji
# 4  swapnil   29  vimannagar

# read excel data with pandas
import openpyxl
excel_data = pd.read_excel('student.csv', sheet_name = 'student')
print(excel_data)