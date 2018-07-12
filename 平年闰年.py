print('请输入要计算的年份：')
year = int(input())
if year%4 == 0 and year%100 !=0 or year%400 == 0:
    print('%d是闰年'%year)
else:
    print('%d是平年'%year)
