#
my_list=[10,20,10,'hi',True,[20,'Hello']]
print=(my_list)
print=len(my_list)
#
my_tuple=(10,20,10,'Hi',True,[20,'Hello'])
#
my_set={10,20,10,'Hi',True,(10,20)}
#dictionay key;value/key->String-Number/Value->Everthing
                #key:คือ associative คือ ตัวชี้ที่อ้างอิงไปยัง Value
                #Value:คือ ค่าข้อมูลที่สามารถเอาไปใช้งาน
my_dict={'k':'สมชาย','age':20,555:999,'flag':True}
print(my_dict['k'])
print(my_dict['age']+my_dict[555])
my_dict['name']='ppp'
print(my_dict)

for data in my_dict:
    pass
for data in my_dict.keys:
    print(data,end='')
for data in my_dict.values:
    print(data,end='')

my_dict1={'a':10,'b':20,'c':30}
my_dict2=my_dict1
my_dict3=my_dict1.copy
print()
print(my_dict2)
print(my_dict3)
my_dict2['a']=999
my_dict3['a']=888
print(my_dict1)
print(my_dict2)
print(my_dict3)