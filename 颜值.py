print('请输入身高：')
height = int(input())
print('请输入身价：')
price = int(input())
print('请输入颜值分:')
yanzhi = int(input())
if height > 180 and price > 1000000 and yanzhi > 99:
    print('高富帅')
if yanzhi > 99:
    print('帅')
if height < 160 and price < 100 and yanzhi < 60:
    print('矮穷矬')
