from Codes.Assignment_oops.Dict_class import Dictionary

class List(Dictionary) :

    def print_square(self, list1):
        result = [x ** 2 for x in list1]
        return result

    def sum_elements(self, list1):
        sum = 0
        for var in list1:
            sum = sum + var

        return sum

    def list_element_product(self, list1):
        pro = 1
        for var in list1:
            pro = pro * var

        return pro

    def small_large_list(self, list1):
        small = list1[0]
        large = 0
        output = {}
        for var in list1:
            if var > large:
                large = var
            if var < small:
                small = var
        output['smallest element'] = small
        output['Largest element'] = large

        return output

    def list_element_reverse(self, list1):
        output = []
        for val in list1:
            output.append(val[:: -1])

        return output