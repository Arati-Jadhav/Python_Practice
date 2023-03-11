class employee :
    # class variable
    city = 'Mumbai'
    _address = 'Borivali street'
    __country = 'India'

    # Instance method (constructor)
    def __init__(self, name, company, salary):
        # Instance variable
        self.name = name
        self._company = company
        self.__salary = salary

    # Instance method
    def show_emp_name(self):
        print('Employee name :', self.name)

    # Instance method
    def _show_company(self):
        print('Employee working in company :', self._company)

    # Instance method
    def __show_salary(self):
        print('Employee salary is :', self.__salary)

    # class method
    @classmethod
    def show_employee_general(cls):
        print('City : ', cls.city)
        print('Address :', cls._address)
        print('Country :', cls.__country)
        # print("Name :", cls.name) we can not access instance variable in the class method
        # cls.show_emp_name() # we can not access instance method in the class method

    @staticmethod
    def static_method_get_factorial(num):
        fact = 1
        for i in range(num, 0, -1) :
            fact *= i

        return fact

if __name__ == '__main__' :
    obj = employee('Rahul', 'Facebook', '50Lac')

    obj.show_employee_general() # class method call, we only access class variable and class method
    # City :  Mumbai
    # Address : Borivali street
    # Country : India

    #print(obj.static_method_get_factorial(5))
    # 120

    output = employee.static_method_get_factorial(6) # we can call static method without creating or taking help from object
    print(output)
    # 720