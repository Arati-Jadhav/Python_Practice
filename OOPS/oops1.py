'''
class --> blueprint of any object, where we define all properties, attribute
that we can access through object.

object --> Object is an entity through which we can access of the class.

method / class method / instance method / static method

constructor --> constructor initialize the memory of the object.
1. default constructor --> the constructor which initial the memory by default
        whenever we create object.

2. Parametrize constructor --> it accepts specific number of parameters
    to initialize the data members of the class

OOPs concepts -->
Inheritance
Polymorphism
Data Abstraction/ Data Hiding
Data Encapsulation
'''
'''
class A :
   # parametrize constructor
    def __init__(self, name, age) :
        self.user_name = name   # Instance variable
        self.user_age = age # Instance variable

    # method / object method / instance method
    def print_data(self) :
        print('hello guys !!!!')

    def show_person(self) :
        print(f'name : {self.user_name}')
        print(f'age : {self.user_age}')


if __name__ == '__main__' :
    obj = A('aditya', 28)
    obj.show_person()

# name : aditya
# age : 28
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 

# Class car -> name, company, prize, model
#       -> name method
#       -> company method
#       -> price method
#       -> model method
#       -> show all details

class car :
    def __init__(self, name, company, price, model) :
        self.car_name = name
        self.car_company = company
        self.car_price = price
        self.car_model = model

    def c_name(self, cname) :
        print('name : ', cname)

    def c_company(self, ccompany) :
        print('company : ', ccompany)

    def c_price(self, cprice) :
        print('price : ', cprice)

    def c_model(self, cmodel) :
        print('model : ', cmodel)

    def show_details(self):
        print(f'name : {self.car_name}')
        print(f'company : {self.car_company}')
        print(f'price : {self.car_price}')
        print(f'model : {self.car_model}')


class school :
        def __init__(self, name, city, address, dept) :
            self.sname = name
            self.scity = city
            self.saddress = address
            self.sdept = dept

        def school_name(self, name) :
            print('school name : ', name)

        def school_city(self, city) :
            print('school city : ', city)

        def school_address(self, address) :
            print('school address : ', address)

        def school_dept(self, dept) :
            print('school departments : ', dept)

        def show_details(self) :
            print(f'school name : {self.sname}')
            print(f'school city : {self.scity}')
            print(f'school address : {self.saddress}')
            print(f'school department : {self.sdept}')

if __name__ == '__main__' :
    #obj = car('tiago', 'Tata', 1000000, 'zx')
    #obj.show_details()
    # name : tiago
    # company : Tata
    # price : 1000000
    # model : zx

    #obj.c_name('Scorpio')
    # name :  Scorpio
    #obj.c_company('Mahindra')
    # company :  Mahindra
    #obj.c_price(900000)
    # price :  900000
    #obj.c_model('vx')
    # model :  vx
    
    
    # obj = school('RJC', 'shevgaon', 'vidyanagar', ['physics', 'chemistry', 'Biology', 'Mathematics'])
    # obj.show_details()
    # school name : RJC
    # school city : shevgaon
    # school address : vidyanagar
    # school department : ['physics', 'chemistry', 'Biology', 'Mathematics']

    # obj.school_name('Jilha Parishad')
    # school name :  Jilha Parishad
    # obj.school_city('Ahmednagar')
    # school city :  Ahmednagar
    # obj.school_address('savedi')
    # school address :  savedi
    # obj.school_dept(['physics', 'chemistry', 'Biology', 'Mathematics'])
    # school departments :  ['physics', 'chemistry', 'Biology', 'Mathematics']
'''