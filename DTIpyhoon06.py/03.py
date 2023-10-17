#
my_list=('a','b','c','Hi','k',['d','Hello'])
print=(my_list)
print=(len(my_list))
my_tuple=('a','b','c','Hi','k',['d','Hello'])
print(my_tuple)
my_set=('a','b','c','Hi','k',['d','Hello'])
print(my_set)
#dictionay key;value/key->String-Number/Value->Everthing
                #key:คือ associative คือ ตัวชี้ที่อ้างอิงไปยัง Value
                #Value:คือ ค่าข้อมูลที่สามารถเอาไปใช้งาน

my_dict = {'name' : 'k' , 'age' :20 , 100:555 , 'flag':True}
print(my_dict['name'])


for data in my_dict:
    pass
for data in my_dict.keys:
    print(data,end='')
for data in my_dict.values:
    print(data,end='')