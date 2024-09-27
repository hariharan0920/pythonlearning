# all the file a defaultly in only readable mode
# defaultly if you write in afile means the previous data will be delete automatically

# reading a file
f=open(r"H:\git\pythonlearning\text.py") # adding the file in a variable(f) .use file name(text.py).if it working use path of the file with r(r"H:\git\pythonlearning\text.py")
content=f.read() # coverting the file into a readable file and storing in a variable
print(f)# used to known about the file (read,write)
print(content) #

# writing a file
f=open(r"H:\git\pythonlearning\text.py","w") # converting the file in writable mode
print(f)

f.write("banana")
f.close()
print(f)

# reading and writing in a file
f=open(r"H:\git\pythonlearning\text.py","r+")# you can able to read and write at this it using(r+)

f.write("hi")
v=f.read()
print(v)

# appending in a file
f=open(r"H:\git\pythonlearning\text.py","a")# you can able append on file using(a)
f.write("vanakam")
print(f)
f.close()

# reading a file and printing lineby line
f=open(r"H:\git\pythonlearning\text.py","r")
print(f.readline())# it use to print the  line by line only



