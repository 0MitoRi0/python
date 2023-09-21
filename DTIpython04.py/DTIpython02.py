def funcA(x, y) :
    print("AAA")
    z = x + y
    print(f" {x} + {y} ={z}")
    #ไม่มีคำสั่ง return
def funcB(x,y,z) :
    print("{:.2f} {:.4f} {:.5f}".format(x,y,z))

funcA(10, 92) #ข้อมูลที่ส่งให้ parameter เรียกว่า argument
funcA(10, 5)
funcB(10, 92 , 4)