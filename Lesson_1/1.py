# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
number = 122
# number = int(input("Ваше трехначное число "))
sum = 0
proizvedenie = 1

while number != 0:
    digit = number % 10
    sum = sum + digit
    proizvedenie = proizvedenie * digit
    number = int(number / 10)

print(sum)
print(proizvedenie)
