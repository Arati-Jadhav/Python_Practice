'''
Polymorphism -> when a single entity perform multiple task is know as polymorphism

-> Method Overriding -> when we have inheritance between 2 classes and have
same method name, then child class method will preference when its object is being created
parent class method will be overwritten by child class method.

-> Method Overloading -> when one class have 2 method with same name with different functionality,
then it is known as method overloading, but python does not support this feature.
If we defined 2 methods with same name, then it will consider latest defined method

-> Operator Overloading ->
'''
'''
class company:
    def __init__(self, company_name):
        self.company_name = company_name

    def welcome_msg(self):
        print('We are in company class')

    def show_company(self):
        print('we are in company class')
        print('company name : ', self.company)

class employee(company):
    def __init__(self, name, designation, salary, company):
        super().__init__(company)
        self.name = name
        self.designation = designation
        self.salary = salary

    def show_employee_details(self):
        print(f'Employee name : {self.name}\n'
              f'Employee designation : {self.designation}\n'
              f'Employee salary : {self.salary}')

    # this method will not consider to execute
    def show_company_working_hour(self):
        print('Total 8 hr/day employee has to work')

    def show_company_working_hour(self, hour):
        print(f'Total {hour} hr/day employee has to work')

    def show_company(self):
        print('we are in employee class')
        print('company name : ', self.company)
        self.show_employee_details()

if __name__ == '__main__' :
    obj = employee('Shivam', 'Data analyst', '20 Lac', 'Datamatica')
    #obj.show_company()
    # AttributeError: 'employee' object has no attribute 'company'

    obj.show_employee_details()
    # Employee name : Shivam
    # Employee designation : Data analyst
    # Employee salary : 20 Lac
'''
'''
# operator overloading
num1 = 50
num2 = 30

print(num1 + num2)
# 80

print(num1.__divmod__(num2))
# (1, 20)

print(num1.__mod__(num2))
# 20

print(num1.__eq__(num2))
# False

print(num1.__mul__(num2))
# 1500

print(num1.__sub__(num2))
# 20

num3 = 2
print(num1.__pow__(num3))
# 2500

print(num1.__and__(num2))
# 18

print(num1.__or__(num2))
# 62

num4 = 45678.8765
print(num4.__round__(2))
# 45678.88

print(num4.__trunc__())
# 45678
'''