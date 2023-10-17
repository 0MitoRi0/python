#oop
#Camel case / Pascal case,Snake case
class DtiTeam:
    #data/property mamber
    stu_name=''
    score=0
    gpa=0

#method member คือการทำงาน(เขียนแบบฟังชัน เพียงแต่ว่ามันอยู่ใน )
    def hiStudent(self):
        print(f'สวัสดี{self.stu_name}')

    def showScoreAndGrade(self):
        print(f'คะเนน{self.score}ได้เกรด{self.gpa}')
#สร้าง object
object01=DtiTeam()#ชื่อคลาสที่มี()เราเรียกว่าเป็นการสั่งให้ constructor ขแงคลาสทำงาน
object02=DtiTeam()

object01.stu_name='สมชาย'
object01.hiStudent()
object02.stu_name='สมหญิง'
object02.score=99
object02.gpa=3.99