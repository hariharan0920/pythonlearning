class a():
    def __init__(self):
        print("a")
    def display(self):
        print("class a")

class b():
    def __init__(self):
        super().__init__()# superkeyword
        print("b")
    def display(self):
        print("class b")

class c(a,b): # in multiple inheritance the piriorty is given to lefttoright. so it will give preference to the "class a"
    def __init__(self):
        super().__init__()# superkeyword
        print("c")
    def display(self):
        print("class c")



ob1=c()

