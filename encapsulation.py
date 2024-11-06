# encapsulation -hides all the essential detail,show only unessential details
# public variable-a class variable which we normally used and it can be accessed by all
# private varible-a class variable will become private by adding(self.company=__self.company)
# by privating this variable no one can acess it,only the functions in that same class can access it
# protected variable-a class variable will become protected by adding(self.company=_self.company)
# by protecting this variable no one can acess it,only the functions in that same class and childclass  can access it


#private varible
# private varible-a class variable will become private by adding(self.company=__self.company)
# by privating this variable no one can acess it,only the functions in that same class can access it
class company():
    def __init__(self):
        self.__companyname="google"# encapsulating the variable
        print(self.__companyname)#only the functions in that same class can access it
    def com(self):
        print(self.__companyname)#only the functions in that same class can access it

c1=company()
c1.com()


#protected variable
# protected variable-a class variable will become protected by adding(self.company=_self.company)
# by protecting this variable no one can acess it,only the functions in that same class and childclass  can access it

class company():
    def __init__(self):
        self._companyname="google"# encapsulating the variable
        print(self.__companyname)#only the functions in that same class and child class can access it
class b(company):   
    def com(self):
        print(self._companyname)#only the functions in that same class and child class can access it

b1=b()
b1.com()
