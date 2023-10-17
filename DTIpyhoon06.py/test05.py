#selt เปรี่ยบเสมื่อนสิ่งที่ใช้แทนคลาสตัวเอง เพื่อที่จะสามารถเรียกใช้ member ในคลาสตัวเองได้
class Test05:
    data1=10

    #constructor
    def __init__(self,data2,data3):
        self.data2=data2
        self.data3=data3
        pass
    #method member
    def showSumdata(self):
        print(self.data1+self.data2+self.data3)
        self.showWow()

    def showWow(self):
        print('Wow wow wow...')

objectA=Test05(20,30)
objectB=Test05(10,20)
objectC=Test05(20,100)
objectD=Test05(20,30)