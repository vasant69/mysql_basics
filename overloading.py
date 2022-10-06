class A:
    def __init__(self):
        self.a= "mango"
        self.b="apple"
        self.c="chhota aaple"

class B(A):
    a="bada mango"
    def __init__(self):
        self.a="papita"

aa = A()
bb = B()
#print(aa.a)
print(bb.a)
print(bb.c)
print(bb.b)

# instance variable has highest proriority. so it print value of instane variable.