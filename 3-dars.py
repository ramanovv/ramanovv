son = int(input('juft son kiriting: '))
if son %2==0:
    print('raxmat! ')
else:
    print('bu juft son emas')

yosh = int(input('yoshingiz nechida? '))
if yosh < 4 or yosh >=60:
    price = 0
elif yosh <= 18:
    price = 10000
else:
    price = 20000
print(f'sizga kirish {price} so`m ')