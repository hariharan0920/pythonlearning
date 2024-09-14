# list is the one of the datatype that can be
# mutable,allow duplicate,ordered,allow comprehension,any kind of data can be stored,

# append a value in list
a=[1,2]
print(a)
a.append(7)         # appending a value
a.append("emc")     # allow all type of data
a.append(2)         # allow duplicate
print(a)

# append=a.append()
# insertion=a.insert(2,5)
# pop=pop(4)
# extend=a.extend(b)
# replace/modify=a[2]=5

a=[1,2,3,4,5]
b=[7,8,9]
print(a)    # the order of the list will be in insertion order
print(a[1]) # use to print the nth value in the list

a.insert(1,4) # use to insert a value in the nth place of the list
print(a)

a[0]=11  # use to replace a nth value in list
print(a)

a.pop(1) # use to remove a nth value in list
print(a)

a.extend(b)  # use to merge to list
print(a)

#tuple 
# immutable,allow duplicate,ordered,not allow comprehension,any kind of data can be stored
# mutable when it is coverted into list

a=(1,2,3,4)
print(a)
b=list(a)   # by using casting tuple can be convert into list 
b.pop()   # empty pop will remove the last element in list
print(b)

a=tuple(b) #reverse casting
print(a)

# set
# no duplicate,immutable,unordered,allow comprehension,any kind of data can be stored,
# not modifiable, but we can add or remove items 

#add=a.add()
#remove=a.remove()
#pop=a.pop()
#update=a.update()

a={1,2,3,4,5}
b={7,8}
c=[9,0]
print(a)

a.add(6) # use to add a value in set
print(a)

a.remove(4) # use to remove a value eg. if you like to remove a num 4 in set
print(a)

a.pop() 
print(a)  # use to remove a random value in set

a.update(b) # use to merge 2 set ,or with other data types (tuple,list,dict,set) and remove duplicate
a.update(c)
print(a)

#dictionary
# mutable,duplicate,ordered,allow comprehension,any kind of data can be stored,

# store elment in "keys: value" format
#key()=print(a.keys())
#value=print(a.values())
#update=a.update({"name":"ha"})  /  a["age"]=2 
#pop=a.pop("age") 
#delete=del a["colour"] 
#delete= del a 
#clear= a.clear() 


a={"name":"hari",
   "age":1,
   "num":["1,2,3,4"]} # store elment in "keys: value" format
print(a)

print(a.keys())  # use to print all the keys use in dict
print(a.values()) # use to print all the values use in dict

a["age"]=2  # modify/replace value specfic value
a["colour"]="red" # use to add a key and value
print(a)

a.update({"name":"ha"}) # modify/replace value specfic value
a.update({"loc":"ch"}) # use to add a key and value
print(a)

a.pop("age") # use to remove a element
del a["colour"] # use to remove a element
del a # use to delete a complete dict
a.clear() # use to clear the value in dict
print(a)