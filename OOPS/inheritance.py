'''
Inheritance :
1. Single inheritance : Class A --> Class B (Father and son relationship)
2. Multi Level Inheitance : Class A --> Class B --> class C (Grandfather --> Father --> Son)
3. Multiple Inheitance : Class A --> Class B,  Class C --> Class B (Father --> Son,  Mother --> Son)
'''
'''
############################################ single inheritance ############################################
class father :
    def __init__ (self,  f_house, f_car, f_business) :
        self.father_home = f_house
        self.father_car = f_car
        self.father_business = f_business

    def show_father_house(self,):
        print('Father house : ', self.father_home)

    def show_father_car(self):
        print('Father car : ', self.father_car)

    def show_father_business(self):
        print('Father business : ', self.father_business)

    def show_father_details(self):
        self.show_father_house()
        self.show_father_car()
        self.show_father_business()

# super method helps to initiate the constructor of parent class in the child class  constructor #############################3
class son(father) :
    def __init__(self, name, f_house, f_car, f_business) :
        super().__init__(f_house, f_car, f_business)
        self.name = name

    def show_son_name(self):
        print('My name is : ', self.name)

if __name__ == '__main__' :
    obj = son('Jerry', 'Banglow', 'Audi', 'Construction')
    obj.show_father_details()
    # Father house :  Banglow
    # Father car :  Audi
    # Father business :  Construction
'''
'''
########################################## Multilevel Inheritance ##################################
# Multilevel Inheritance
class grandfather :
    def __init__(self, property):
        self.grandfather_property = property

    def show_grandfather_property(self):
        print('Grandfather property : ', self.grandfather_property)

class father(grandfather) :
    def __init__(self, f_house, f_car, f_business, gfproperty):
        super().__init__(gfproperty)
        self.father_home = f_house
        self.father_car = f_car
        self.father_business = f_business

    def show_father_house(self):
        print('Father house : ', self.father_home)

    def show_father_car(self):
        print('Father car : ', self.father_car)

    def show_father_business(self):
        print('Father business : ', self.father_business)

    def show_father_details(self):
        self.show_father_house()
        self.show_father_car()
        self.show_father_business()
        self.show_grandfather_property()

# super method helps to initiate the constructor of parent class in the child class constructor ################################
class son(father)  :
    def __init__(self, name, f_house, f_car, f_business, gfproperty):
        super().__init__(f_house, f_car, f_business, gfproperty)
        self.name = name

    def show_son_name(self):
        print('My name is : ', self.name)

if __name__ == '__main__' :
    obj = son('Jerry', 'Bunglow', 'Audi', 'Construction', '200 Acr')
    obj.show_father_details()
    obj.show_son_name()
    # Father house :  Bunglow
    # Father car :  Audi
    # Father business :  Construction
    # Grandfather property :  200 Acr
    # My name is :  Jerry
'''
'''
####################################### Multiple Inheritance #####################################
class mother :
    def __init__(self, mcar, mhouse, mbusiness):
        self.mother_home = mhouse
        self.mother_car = mcar
        self.mother_business = mbusiness

    def show_mother_details(self):
        print('Mother car : ', self.mother_car)
        print('Mother house : ', self.mother_home)
        print('Mother business : ', self.mother_business)

class father :
    def __init__(self, fhouse, fcar, fbusiness):
        self.father_home = fhouse
        self.father_car = fcar
        self.father_business = fbusiness

    def show_father_house(self):
        print('Father house : ', self.father_home)

    def show_father_car(self):
        print('Father car : ', self.father_car)

    def show_father_business(self):
        print('Father business : ', self.father_business)

    def show_father_details(self):
        self.show_father_house()
        self.show_father_car()
        self.show_father_business()

#################################################################################
# super method helps to initiate the constructor of parent class in the child class constructor
#  MRO : Method Resolution Order : priority of calling class will decide whoch method we can access
# sequence of class name will call, will decide the order.
#################################################################################

class son(father, mother) :
    def __init__(self, name, fhouse, fcar, fbusiness, mcar, mhouse, mbusiness):
        super().__init__(fhouse, fcar, fbusiness)
        self.name = name
        self.mobj = mother(mhouse, mcar, mbusiness)

    def show_son_name(self):
        print('Son name : ', self.name)

if __name__ == '__main__' :
    obj = son('John', 'BeachHouse', 'Audi', 'Construction', 'BMW', '4BHK',  'Beauty Products')

    #obj.show_father_details()      # priority --> father
    # Father house :  BeachHouse
    # Father car :  Audi
    # Father business :  Construction

    #obj.show_mother_details()      # priority --> mother
    # Mother car :  BeachHouse
    # Mother house :  Audi
    # Mother business :  Construction

    #obj.mobj.show_mother_details()
    # Mother car :  4BHK
    # Mother house :  BMW
    # Mother business :  Beauty Products
'''