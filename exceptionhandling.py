#compile time error
#syntax error
# the error that found while compiling the code(generally it will be a spelling mistake,syntax error)
print("hi")
printt("hiiii")# compile error

# logical error
a=10
b=20
print(a+a)# logical error

#runtime error 
# error araises after compiling the code while running the code
#value error 
a=int(input()) # input 2
b=int(input()) # input hi
print(a+b)# in this code if you enter the str value as ainput means the error araises because the code needs int value

# exception handling
try:
    a=int(input()) # input 2 
    b=int(input()) # input hi
    print(a+b)
except Exception as e:
    print("something",e)# if error araises in try block then it will move to except block

# exception handling 
try:
    a=int(input()) # input 2 
    b=int(input()) # input 4
    c=input()# input 4 # forvalue error
    print(c/a) # type error
    print(d) # name error
except ValueError as e:
    print("value error",e)# if error is valueerror this exception will work
except TypeError as e:
    print("typeerror",e)# if error is typeerror this exception will work
except exception: # it will work when the above mentioned errors are not araised but there is a error in the blockofcode 
    print("something wrong")# all type of errors will come under exception
finally:# finally will work as a last block of code.if there is a error or not but this code will be executed in last.it is used to known that code is completly runed
    print("done")

