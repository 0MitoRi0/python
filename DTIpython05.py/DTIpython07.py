#break กับ contioue
for x in range(5):
    if x==3:
        break; #break ทำงานเมื่อไหร่จบ loop  ทันที
    print(f'SAU.......{x}')

print('....................')

for y in range(5):
    if y==3:
        continue; #break ทำงานเมื่อไหร่รอบนั้นไปรอบต่อไปทันที
    print(f'DTI.......{y}')