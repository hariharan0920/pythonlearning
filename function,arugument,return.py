# function
def painter():
    print("painting")

painter()

# creating function
# q1 create a function called add(),sub,mul,div ,get input for a and b inside every function  print result



def add(): 
    print("addition")
    a=int(input("enter a num"))
    b=int(input("enter a num"))
    print(a+b)

add()  # calling a function

#  passing arugument in the function
# q2 get input and pass it to function called findevenorodd().print the num is even or odd

def evenorodd(num):
    if(num%2==0):
        print("even")
    else:
        print("odd")

a=int(input("enter a num"))
evenorodd(a) # passing a arugument

# q3 get a input and passs it to the function passorfail().print the num is pass or fail

def passorfail(num):
    if(num>30):
        print("pass")
    else:
        print("fail")
    
a=int(input("enter a num"))
passorfail(a)

#get get input a and b pass it to the function called printrange(),print num a and b



#    return keyword
# it same as a function instead of print there will be return calling the function use print(functionname)


def painter():
    return "i am painter"  #using return "msg to be printed" instead of print

msg=painter()
print(msg)   # calling a function by print(funname)

#  set uname=emc upassword=123 get input name and password create a function validate() ,if name and password matches return true else false

uname="emc"
upassword=123

def validate(name,password):
    if(name==uname and password==upassword):
        return True
    else:
        return False

a=input("enter name")
b=int(input("enter password"))
print(validate(a,b))

# get input for a,b,c function add().it return sum a+b then multiply sum with c
#  for geting a return value and doing a operation with it

def add(a,b):
    return a+b

a=int(input("enter a num"))
b=int(input("enter a num"))
c=int(input("enter a num"))
d=add(a,b) # assign a variable to function ,the return value will be stored in variable
e=d*c   # assign another variable return value of function and operation
print(e) # calling another variable