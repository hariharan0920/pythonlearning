#polymorphism  means having many forms.polymorphism means the same function name (but different signatures) being used for different types.
# using of same function name but difference is the datatypes and number of arguments used in fuction
def add(a,b,c=0):
    print(a+b+c)

add(1,2)
add(1,2,3)


# method overrides
# Create class Animal with method sound,prints "Animal makes a sound."Create derived class Dog,inheritsfrom Animal and overrides the sound()method to print "Dog barks." Create anotherderived class called Bird that inherits fromAnimal and overrides the sound () method toprint "Birds Sing."
class animal():
    def sound(self):
        print("animal makes a sound")
class dog(animal):
    def sound(self):
        print("dog barks")
class bird(animal):
    def sound(self):
        print("birds sings")

a1=animal()
a1.sound()

 # Create a base class called Shape with a methodarea() that returns 0. Create a derived classcalled Rectangle that inherits from Shapeand overrides the area() method to calculateand return the area of a rectangle.
# polymorphism is 2 or more class using same function and each class overrides the function .classes are inherited
class shape():
    def area(self):
        return 0 
class rectangle(shape):# inheritance
    def area(self):#polymorphism
        l=10
        b=20
        return(l*b)
        
s1=shape()
print(s1.area())
r1=rectangle()
print(r1.area())

#Create a base class called Person with aconstructor that takes a name as a parameterCreate a derived class called Student thatinherits from Person and has a constructorthat takes a parameter called grade. Write amethod in Student to display the name and grade of the student. Use Super Keyword toachieve this.

class person():
    def __init__(self,name):
        self.name=name
       

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)# using superkeyword we are passing the parameter name to the base class
        self.grade=grade
    def display(self):
        print(self.name)
        print(self.grade)


s1=student("hari","a")# we passing parameter values of both base class and childclass , are passed to childclass
s1.display()

# 3.Create a base class called Vehicle with amethod start() that prints "Vehicle started."Create a derived class called Car that inheritsfrom Vehicle and overrides the start()method to print "Car started."
class vehicle():
    def start(self):
        print("vehicle started")

class car(vehicle):
    def start(self):
        print("started")

c1=car()
c1.start()

#4.create a base class called Employee withproperties name and salary. Create a derivedclass called Manager that inherits fromEmployee and adds a property department.Write a method in Manager to display thename, salary, and department of the manager.


class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept=dept
    def display(self):
        print(self.name,self.salary,self.dept)

m1=manager("hari","10","comp")
m1.display()




