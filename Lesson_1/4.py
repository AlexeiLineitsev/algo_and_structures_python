"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

import random

print('Случайное целое число в диапазоне от А до B')
a = int(input('A = '))
b = int(input('B = '))

print("Ваше число",random.randint(a,b))


print('Вещественное целое число в диапазоне от А до B')
a = float(input('A = '))
b = float(input('B = '))

print("Ваше число %.2f" % random.uniform(a,b))


print('Cлучайный символ число в диапазоне от А до B')
a = ord(input('A = '))
b = ord(input('B = '))

print("Cлучайный символ ", chr(random.randint(a,b)))

