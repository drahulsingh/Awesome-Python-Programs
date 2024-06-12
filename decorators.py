def fd(f):
    def mfun(*a):
        print("Welcome")
        f(*a)
        print("TY")
    return mfun

@fd
def fun1():
    print("Wipro session")

@fd  
def fun2():
    print("Python session")

@fd
def fun3(a, b):
    print(a + b)

fun1()
fun2()
fun3(10, 29)