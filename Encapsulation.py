class Employee:
    # class variable
    city = 'mumbai'
    _address = 'Boravali_street'
    __country = 'Mumbai'

    def __init__(self,name,company,salary):
        # Instance variable
        self.name = name
        self._company = company
        self.__salary = salary

    def show_employee_name(self):
        print("employee name :",self.name)

    def _show_compamy(self):
        print("employee company :",self._company)

    def __show_salary(self):
        print("employee salary :",self.__salary)


if __name__ == '__main__':
    obj = Employee('Amit','Google','50l')
    # obj.show_all_employee_details()
    print(obj._address)
    obj._show_compamy()


