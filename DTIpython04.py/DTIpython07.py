#build-in function 
#about string
#ตัวเลข
import math
#inputradius
def inputradius() :
    #radius = input("ป้อนรัศมี :")
    #return r
    #r = float(input("ป้อนรัศมี :"))
    #return r
    #return input("ป้อนรัศมี :") 
    return float(input("ป้อนรัศมี :"))
    #return r

#calAreaCircle
def calAreaCircle( r ) :
    area = math.pi * r ** 2  
    # area = math.pi * r * r  
    # area = math.pi * math.pow(r, 2)  
    return math.pi * math.pow(r, 2)
    #return area


#calRoundCircle 2 * PI * r
def calRoundCircle (r) : 
    return 2 * math.pi * r
    

#calCubeCircle 4 / 3 * PI * r * r * r 
def  calCubeCircle (r) :
    return 4/3 * math.pi * r * r * r 
    

#showResult ทศนิยม 4 ตำแหน่ง
#พื้นที่วงกลมเป็น .... เส้นรอบวงเป็น .... ปริมาตรทรงกลมเป็น
def showresualt():
    radius = inputradius()
    area = calAreaCircle(radius)
    parameter = calRoundCircle(radius)
    volume = calCubeCircle(radius)
    print("Radius","%.4f" % radius)
    print("Area","%.4f" % area)
    print("Paramwter","%.4f" % parameter)
    print("Volume","%.4f" % volume)

showresualt()
