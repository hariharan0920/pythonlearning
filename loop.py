#general loop statement

for i in "apple":
    print(i)

#for loop
for i in range(5):
    print(i)

# q1 print 2 table in for loop
for i in range(1,11):
    print(i,"x2=",i*2)

# q2 get input a and b print num between a and b

a=int(input("enter a num"))
b=int(input("enter a num"))
for i in range(a+1,b):
    print(i)

# q3 print even num(1,10)

for i in range(0,11,2):
    print(i)

# q4 count odd num between 1to10

count=0
for i in range(1,11):
    if(i%2==0):
        count=count+1
print(count)
    
# q5 count odd and even num between 1to 11

a=0
b=0
for i in range(1,12):
    if(i%2==0):
        a=a+1
    else:
        b=b+1
print("even",a)
print("odd",b)

# q6 count num divisble by 3and 5 range1-100

count=0
for i in range(1,101):
    if (i%3==0 and i%5==0):
        count=count+1
print(count)

# q7 sum of first 5 natural num

sum=0
for i in range  (1,6):
    sum=sum+i
print(sum)

# q8 program to read 10 num from keyboard and find their sum and average
# in print("even",i) can be printed by "," but in input ("even"+str(i)) should be used

a=[]
count=0
for i in range(10):
    b=int(input("enter num"+str(i+1))) # in print("even",i) can be printed by "," but in input ("even"+str(i)) should be used
    a.append(b)
    count=count+1
print(a)
print(count)
sum=0
for i in a:
    sum=sum+i
avg=sum/count
print("sum =",sum)
print("avg=",avg)

# q9 display n terms of natural num and their sum

n=int(input("enter a num"))
a=[]
sum=0
for i in range (1,n+1):
    a.append(i)
    sum=sum+i
print("list of num",a)
print("sum=",sum)

# q10 display the cube of the num

num=int(input("enter a num"))
for i in range(1,num+1):
    a=i*i*i
    print("num is:",i ,"cube of it is",a)

# q11 
