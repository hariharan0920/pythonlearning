# inheritance a subclass derived from superclass
# childclass will able to access the functions parent class
# type of inheritance single,multiple,multiplelevel
# single inheritance- 1 childclass inherit from 1 parent class
# multiple inheritance- 1 childclass inherit from 2 parent class
# multilevel inheritance- 1 childclass inherit from 2 parent class
# heirarchy inheritance-2 or more childclass inherited from a single parentclass
#hybrid inheritance - combination 2 or more inheritance


#single inheritance
class dad:
    def phone(self):
        print("dad phone")

class son(dad):#single- inheriting a childclass from parentclass
    def laptop(self,):
        print("son laptop")

ram=son()
ram.phone()

# multiple inheritance
class dad:
    def phone(self):
        print("dad phone")

class mom:
    def sweet(self):
        print("mom sweet")

class son(dad,mom):#multiple- inheriting a 1 childclass from 2 parentclass
    def laptop(self,):
        print("son laptop")

ram=son()
ram.phone()
ram.sweet()

# multilevel inheritance
# inheriting multilevel of child class from parent class
class grandpa:
    def phone(self):
        print("grandpa phone")

class dad(grandpa):# inheriting
    def money(self):
        print("dad money")

class son(dad):#multilevel- inheriting a 1 childclass from  parentclass
    def laptop(self,):
        print("son laptop")

ram=son()
ram.phone()
ram.money()
ram.laptop()
d1=dad()
d1.phone()

# heirarchy inheritance
# 2 or more childclass inherited from a single parentclass
class dad():
    def money(self):
        print("dad money")

class son1(dad):
    pass
class son2(dad):
    pass
class son3(dad):
    pass
s2=son2()
s2.money()

#hybrid inheritance
# combination 2 or more inheritance
class dad():
    def money(self):
        print("dad money")

class land():
    def important(self):
        print("important land")

class son1(dad):
    pass
class son2(dad,land):
    pass
class son3(dad):
    pass
s2=son2()
s2.money()
s2.important()


# if a childclass is inherited from parent class,if u create the object for the childclass the constructor of childcall will be executed,if these is no constructor in childclass the constructor of parentclass will be executed
# but if you like to call the const in parentclass by creating a object in child class. for this scenario "superkeyword" is used(super().__init__())
class a():
    def __init__(self):
        print("a")
    def display(self):
        print("class a")

class b(a):
    def __init__(self):
        super().__init__()# superkeyword
        print("b")
    def display(self):
        print("class b")

ob1=b()

 # eg 2 superkeyword with multipleinheritance        
class a():
    def __init__(self):
        print("a")
    def display(self):
        print("class a")

class b():
    def __init__(self):
        super().__init__()# superkeyword
        print("b")
    def display(self):
        print("class b")

class c(a,b):
    def __init__(self):
        super().__init__()# superkeyword
        print("c")
    def display(self):
        print("class c")



ob1=c()
