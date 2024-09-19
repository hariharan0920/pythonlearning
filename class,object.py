# class object methods function constructor selfkeyword pass keyword
# decorator, classmethod,staticmethod  accessing class variable


# class  a function inside a class is called as methods
#Declaring Variables Outside a Constructor (Class Variables)
# Declaring Variables Inside a Constructor (Instance Variables)
class goa:
    name="hari" # if you not decalre name below ,it will take the name in this line
    drink="no"   # known as variable
    def party(self): #self should be writen here when you create afunction inside a class
        print("party")
    def beach(self):
        print("beach")

ramesh=goa()  #creating object for class
suresh=goa()

ramesh.name="ram"  # assign a value for the variable "name" for class's object
suresh.name="sur"

ramesh.drink="yes"
suresh.drink="no"

print(ramesh.name) #printing the variable of class's object
print(suresh.name)
print(ramesh.drink)
print(suresh.drink)

ramesh.party() # calling the function inside the class using object
suresh.beach()

# Q2 create class laptop,variable-price,ram,processor.create object-hp,dell

class laptop:
    price=""
    processor=""
    ram=""

hp=laptop()
dell=laptop()


hp.price=1
hp.processor="intel"
hp.ram=4

dell.price=2
dell.processor="amd"
dell.ram=8

print(hp.price)
print(hp.processor)
print(hp.ram)

# q3
# constructor
# constructor is unique function that get called automatically when the object is created
 # use to initialize or assign values to the data members of the classes(variable) 
 #  self keyword is used to call or denotes the current object      
class laptop:
    def __init__(self): # constructor
        self.price=""
        self.ram=""
        
        print("demo")
    
    def display(self):
        print("display")
        print("price:",self.price) # self keyword is used to call or denotes the current object
        print("ram:",self.ram)



hp=laptop()

hp.price=50
hp.ram="4"

dell.ram="8"
dell.price="100"


hp.display()

# pass keyword means no operation, use to pass the work to nextline of code ,use to create a blank space 
class hi:
    pass 


#q1 create a class student, variable=name registernum using constructor.create afunction display to display name,reg number

class student:
    def __init__(self):
        self.name="summa"
        self.regno="54"
    def display(self):
        print("name",self.name)
        print("regno",self.regno)


s1=student()
s2=student()

s1.name="hari"
s1.regno="1"

s2.name="siva"
s2.regno="2"


s1.display() 
s2.display()  

# create class fruit, variable colour using constructor,create aobject apple pass the object colour as parameter through object.
# passing a argument of variable value  through object
#default ly the apple it self a argument passes "apple=fruit(apple)"
# so we have use ","
#  
class fruit:
    def __init__(self,col):#so we have use ","
        self.colour=col


apple=fruit("red") # default ly the apple it self a argument passes "apple=fruit(apple)"

print(apple.colour)

# create class teacher,variable=name,regnousing constructor.create function display to display name,regno.create object t1,t2object pass name,regno value through object 
class teacher:
    def __init__(self,name,reg):# receving the passed the variable value
        self.name=name # assigning the passed value to the object variable
        self.regno=reg

    def display(self):
        print(self.name)
        print(self.regno)


t1=teacher("hari","2") #passing the variable value through object as argument
t2=teacher("siva","3")


t1.display()
t2.display()

#q4 create class calculator.create variable a,b.create function called add,sub,mul,div all function should take 2 variable as parameter.pass the a,b value through object()
class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def add(self):
        print(self.a+self.b)

    def sub(self):
        print(self.a-self.b)

    def mul(self):
        print(self.a*self.b)

    def div(self):
        print(self.a/self.b)


n1=int(input("enter a num"))
n2=int(input("enter a num"))

cal=calculator(n1,n2)

cal.add()
cal.sub()
cal.mul()
cal.div() 

#  class variable    instance varaiable
# class variable is a variable that is common for all the objects in the class
# instance variable is a variable that is unique for each object


class phone:
    chargertype="c-type" # class variable
    def __init__(self,brand,price):
        self.brand=brand # instance variable
        self.price=price
        
    def display(self):
        print("brand:",self.brand)
        print("price:",self.price)
        print("chargertype:",self.chargertype)

phone.chargertype="b-type" # changing the class variable's value
samsung=phone("samsung","10")
samsung.display()

redmi=phone("redmi","20")
redmi.display()

# type of class methods
# decorator, classmethod,staticmethod  accessing class variable
#  using a function changing class variable
# but calling class method we have to pass theclassname as argument
# self used to accessing a objects variable and changing it
# cls used to accessing a class variable and changing it
# method 2 using "decoractor" we can able access the class variable without passing the class name


class laptop:
    chargertype="c-type"
    design="modern"
    
    def __init__(self):
        self.brand=""
        self.price=34
    def setprice(self,price):# self used to accessing a objects variable and changing it
        self.price=price

    def getprice(self):
        print(self.price)

    def setchargertype(cls):# cls used to accessing a class variable and changing it
        cls.chargertype="b-type"
        print(cls.chargertype)


    @classmethod# method 2 using "decoractor" we can able access the class variable without passing the class name
    def design(cls):
        cls.design="classic"
        print(cls.design)

    @staticmethod #staticmethod if you not using the class variable and instance variable for a function
    def info():
        print("this is laptop")


hp=laptop()
hp.setprice(20)#calling a function and passing object value argument
hp.getprice()
laptop.setchargertype(laptop)# but calling class method we have to pass theclassname as argument
laptop.design()
hp.info()# calling function using static method