# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
number = 125
# number = int(input("Ваше трехначное число "))
sum = 0
proizvedenie = 1
number1 = number

while number != 0:
    digit = number % 10
    sum = sum + digit
    proizvedenie = proizvedenie * digit
    number = int(number / 10)

print('Число ',number1)
print('Сумма = ',sum)
print('Произведение = ',proizvedenie)
