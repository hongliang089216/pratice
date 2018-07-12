height = 1.75
weight = 80.5
BMI = weight/(height*height)
print(BMI)
if BMI < 18.5:
    print('过轻')
if BMI > 18.5 and BMI < 25:
    print('正常')
if BMI > 25 and BMI < 28:
    print('肥胖')
if BMI > 32:
    print('严重肥胖')
