from Codes.Assignment_oops.String_class import String

class Dictionary(String) :
    def add_element(self, dict1, key, value):
        dict1[key] = value
        return dict1

    def move_dict(self, dict1, dict2):
        dict3 = dict1.copy()
        for val in dict3:
            temp = dict1.pop(val)
            dict2[val] = temp

        return dict2

    def dict_update(self, dict1, dict2):
        dict1 = {'Name': 'Harry', 'Rollno': 345, 'Address': 'Jordan'}
        dict2 = {'Age': 25, 'salary': '$25k'}
        dict1.update(dict2)

        return dict1

    def even_odd_dict(self, dict1):
        even = []
        odd = []
        for key, value in dict1.items():
            if key % 2 == 0:
                even.append([key, value])
            else:
                odd.append([key, value])
        print("Even list : ", even)
        print("Odd list : ", odd)

    def make_dict_from_list(self, list1, list2):
        list1 = ['a', 'b', 'c', 'd', 'e']
        list2 = [12, 23, 24, 25, 15, 16]
        output = {}
        for i in range(len(list1)):
            output[list1[i]] = list2[i]

        return output
