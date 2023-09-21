def  example1() :
    print(111)
    print(222)
    return
    print(333)
    print(444)
    return

# Default Parameter
def dtiTest(x,y,z = 20,a = 10):
    print(f"{x} + {y} + {z} + {a}={x+y+z+a}")

dtiTest(5,100)

dtiTest(9,8,10)

example1()