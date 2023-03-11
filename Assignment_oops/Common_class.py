from Codes.Assignment_oops.List_class import List

class common(List) :
    def __init__(self, name):
        self.username = name

if __name__ == '__main__':
    cobj = common('amit')

    print('first 2 char + last 2 char :', cobj.first2_last2('shivamjagtap'))
    # first 2 char + last 2 char : shap

    str1 = "My name is Amit Devadhe"
    print('Longest word from the string :', cobj.max_len_word(str1))
    # Longest word from the string : Devadhe

    str1 = 'jahaj'
    print('Palindrome result :', cobj.check_palindrome(str1))
    # Palindrome result : True

    str2 = "My name is Amit Devadhe"
    print(cobj.smallest_longest_word(str2))
    # {'smallest_word': 'is', 'longest_word': 'Devadhe'}

    str11 = 'swanandchavan'
    print('Length of string :', cobj.str_len(str11))
    # Length of string : 13

################################################## Dictionary #################################################

    dict1 = {'a' : 123}
    print(cobj.add_element(dict1, 'b', 456))
    # {'a': 123, 'b': 456}

    dict1 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}
    dict2 = {}
    print('New dictionary after moving :', cobj.move_dict(dict1, dict2))
    # New dictionary after moving : {'name': 'john', 'city': 'Landon', 'country': 'UK'}

    dict1 = {'Name': 'Harry', 'Rollno':345, 'Address': 'Jordan'}
    dict2 = {'Age' : 25, 'salary': '$25k'}
    print('Updated dict :', cobj.dict_update(dict1, dict2))
    # Updated dict : {'Name': 'Harry', 'Rollno': 345, 'Address': 'Jordan', 'Age': 25, 'salary': '$25k'}

    dict11 = {1: 25, 5: 'abc', 8: 'pqr', 21: 'xyz', 12: 'def', 2: 'utv'}
    cobj.even_odd_dict(dict11)
    # Even list :  [[8, 'pqr'], [12, 'def'], [2, 'utv']]
    # Odd list :  [[1, 25], [5, 'abc'], [21, 'xyz']]

    list1 = ['a', 'b', 'c', 'd', 'e']
    list2 = [12, 23, 24, 25, 15, 16]
    print('Combining dictionary :', cobj.make_dict_from_list(list1, list2))
    # Combining dictionary : {'a': 12, 'b': 23, 'c': 24, 'd': 25, 'e': 15}

############################################## List #####################################################

    list1 = [1, 2, 3, 4, 5]
    output = cobj.print_square(list1)
    print(output)
    # [1, 4, 9, 16, 25]

    list1 = [1, 2, 3, 4, 5, 6]
    print('sum of list elements :', cobj.sum_elements(list1))
    # sum of list elements : 21

    list1 = [1, 2, 3, 4, 5, 6]
    print('Product of list elements :', cobj.list_element_product(list1))
    # Product of list elements : 720

    list2 = [3, 5, 2, 7, 1]
    print(cobj.small_large_list(list1))
    # {'smallest element': 1, 'Largest element': 7}

    input = ['Sqa', 'Tools', 'Online', 'Learning', 'Platform']
    print('reversed elements :', cobj.list_element_reverse(input))
    # reversed elements : ['aqS', 'slooT', 'enilnO', 'gninraeL', 'mroftalP']