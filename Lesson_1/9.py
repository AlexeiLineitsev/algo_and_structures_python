# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

a = 20
b = 15
c = 12

if a==b or b==c or c==a:
    print('Присутствуют 2 одинаковых числа')
else:
    if a > b and a < c:
        print('a среднее')
    else:
        if b < c:
            print('b среднее')
        else:
            print('с среднее')
