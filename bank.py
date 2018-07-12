username = int(input('请输入您的账号：'))
userpasswd = int(input('请输入密码：'))
money = input()
if username ==3000 and userpasswd == 123:
    print('输入取钱金额')
    if money >= 3000:
        print('取了%s元，还剩%s元'%(money,(6000-3000)))
    else:
        print('没钱取毛线')
else:
    print('非法账户') 
    
