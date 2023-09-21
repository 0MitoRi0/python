def d1() :
    print(111)
    print(222)
    a,b,c = d2()
    print(f'hi {b} age {a} and {c}')
    return 999
    

def  d2() :
    print(333)
    return 10+20 , "somchai" , True
    
print(d1())
x = d1()
y = d1() + 111 + 222
print('---------------------------') 