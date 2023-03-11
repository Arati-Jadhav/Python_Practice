'''
single underscore as prefix '_'
-> If we declare any variable or method with single underscore
    then it does visible suggestion list.

Double underscore as prefix '__'
->
'''

class employee:
    #class variable
    city = 'Mumbai'
    _address = 'Borivali Street'
    __country = 'India'

    def __init__(self, name, company, salary):
        # Instance variable
        self.name = name
        self._company = company
        self.__salary = salary

    # Instance method
    def show_emp_name(self):
        print('Employee name : ', self.name)

    def _show_company(self):
        print('Employee company name : ', self._company)

    def __show_salary(self):
        print('Salary is : ', self.__salary)

if __name__ == '__main__' :
    obj= employee('Amit', 'Blackrock', '80Lac')
    print(obj._address)
    # Borivali Street

    obj._show_company()
    # Employee company name :  Blackrock

    print(obj._company)
    # Blackrock

    # access class members with 'ObjectName._ClassName__variable/method'
    print(obj._employee__country)
    # India

    obj._employee__show_salary()
    # Salary is :  80Lac

    print(dir(obj))
    # '_address', '_company', '_employee__country', '_employee__salary',
    # '_employee__show_salary', '_show_company', 'city', 'name', 'show_emp_name'