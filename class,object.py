# class  a function inside a class is called as methods
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