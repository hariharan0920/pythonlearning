
class goa:
    name="hari" # if you not decalre name below ,it will take the name in this line
    drink="no"   # known as variable
    def party(self): #self should be writen here when you create afunction inside a class
        print(self.name)
    def beach(self):
        print(self.drink)

ramesh=goa()  #creating object for class
suresh=goa()

ramesh.name="ram"  # assign a value for the variable "name" for class's object
suresh.name="sur"

ramesh.drink="yes"
suresh.drink="no"



ramesh.party() # calling the function inside the class using object
suresh.beach()
