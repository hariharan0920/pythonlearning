# comparison operator used to compare 2 variables
# boolean value means true or false 

rcb="win"
if(rcb=="win"):
    print("cup for rcb")
else:
    print("no cup")

#Q1 get input for variable megna make a if statement

megna=input("megna died or alive")
if(megna=="died"):
    print("surya meets priya")
else:
    print("surya weds megna")


#q2 get input for variable mark  mark>30 then print pass

mark=int(input())
if(mark>30):
    print("pass")
else:
    print("fail")

#binary operator and or not
#q3 get a variable input check whether it is divisible by both 2 and 3

a=int(input())
if(a%2==0 and a%3==0):
    print("num is divisible by 2 and 3")
else:
    print("not divisble by 2 and 3")

# q4 get a input and check it is even or odd

a=int(input("enter a number:"))
if(a%2==0):
    print("even")
else:
    print("odd")

#q5 get mark input if mark <30 print poor, 30<mark>70 avg,mark>70 good
# we can use multiply if without else statement
    
mark=int(input("enter mark"))
if(mark<30):
    print("poor")
if(30<mark<70):
    print("avg")
if(mark>70):
    print("good")

# elif

# another  effcient method using elif

mark=int(input("enter mark"))
if(mark<30):
    print("poor")
elif(30<mark and mark<70):
    print("avg")
else:
    print("good")

#

mark=int(input("enter mark"))
if(mark<30):
    print("poor")
elif(30<mark and mark<70):
    print("avg")
elif(mark>70 and mark<100):
    print("good")
else:
    print("invalid input")

#q6 mini calulator get input for 2 number, input for add/sub/multi/div
a=int(input("enter a num a"))
b=int(input("enter a num b"))
c=(input("add/sub/multi/div"))
if(c=="add"):
    print(a+b)
elif(c=="sub"):
    print(a-b)
elif(c=="multi"):
    print(a*b)
elif(c=="div"):
    print(a/b)
else:
    print("invalid input")

# get input mark , mark>70 get input name,dept eligible

mark=int(input("enter mark"))
if(mark>70):
    name=input("enter name")
    dep=input("enter dept")
    print("eligible")
else:
    print("not eligible")

# nestedif

    # get input for salary and age, if sal>or=20000  or age<25 get input for loan amount or print not eligible
    # if req amount <or=50000 print eligible  ,if not print max amount is 50000

sal=int(input("enter sal"))
age=int(input("enter age"))
if(sal>=20000 or age<=25):
    loanamount=int(input("enter loan amount"))
    if(loanamount<=50000):
        print("print elgible")
    else:
        print("max amount is 50000")
else:
    print("not eligible")

    # get input for 5 sub marks ,find avg ,if avg >30 print good, else print bad

a=int(input("enter mark of eng"))
b=int(input("enter mark of tamil"))
c=int(input("enter mark of maths"))
d=int(input("enter mark of science"))
e=int(input("enter mark of social"))
avg=a+b+c+d+e/5
if(avg>=30):
    print("good")
else:
    print("bad")

# given a int n, if n is odd printweird ,if n is even and inclusive range of 2to5 print not weird
#if n is even and inclusive range 6to 20 print weird, if n is even >20 print not weird

n=int(input())
if(n%2==0):
    if(n>=2 and n<=5):
        print("evennot weird")
    elif( n>=6 and n<=20):
        print("evenweird")
    elif(n%2==0 and n>20):
        print("evennnnot weird")
else:
    print("oddweird")






    








