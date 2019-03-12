# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

number_chr = int(input('Номер буквы - '))

# number_chr = 97

if number_chr >= 97 and number_chr <= 122:
    print('Это буква - ', chr(number_chr))
else:
    print('Только для английского алфавита')
