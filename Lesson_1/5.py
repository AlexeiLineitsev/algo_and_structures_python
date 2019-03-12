#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

first_chr = 'a'
second_chr = 'k'

# Или может пользователь
# first_chr = str(input('Первая буква - '))
# second_chr = str(input('Вторая буква - '))

print(first_chr,'Стоит на месте - ',ord(first_chr) - ord('a') + 1)
print(second_chr,'Стоит на месте - ',ord(second_chr) - ord('a') + 1)
print('Между ними букв - ',ord(second_chr) - ord(first_chr) - 1)
