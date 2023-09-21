#คำนวนเงินที่จะแชร์กัน ป้อนเงิน ป้อนคน แสดงเงินที่แฃร์กันนทางหน้าจอ
#โดยเขียนเป็นฟังก์ฃัน 2 ฟังก์ชัน

#รับค่า
def inputmoneyPerson() :
    money = float(input("ป้อนเงิน :"))
    person = int(input("จำนวนคน :"))
    return money, person

#คำนวณ แสดงผล
def calAndshareMoneyShow(money, person) :
    doublefloatMoney = format(money, ".2f")
    print(f"จำนวนเงิน {money:.2f} บาท {person} คน แชร์กันคนละ  {round(money/person)} บาท")
    print("จำนวนเงิน",("%.2f" % money),"บาท",person,"คน แชร์กันคนละ",round(money/person),"บาท")  #,
    print("จำนวนเงิน "+str("%.2f" % money)+ " บาท " + str(person) + " คน แชร์กันคนละ "+str(round(money/person)) + " บาท")#+
    print("จำนวนเงิน {} บาท {} คน แชร์กันคนละ {} บาท".format(doublefloatMoney, person, round(money/person)))# format
    print("จำนวนเงิน %s บาท %d คน แชร์กันคนละ %d บาท" %(doublefloatMoney, person, round(money / person)))# %2

money, person = inputmoneyPerson( )
calAndshareMoneyShow(money, person )