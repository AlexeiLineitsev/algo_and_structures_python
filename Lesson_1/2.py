# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др.
# над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака.


a = 5     # 0b101
b = 6     # 0b110

print("a bin = ", bin(a))
print("b bin = ", bin(b))
print("И - ", a & b)
print("ИЛИ - ", a | b)
print("5 побитовый сдвиг вправо = ", a >> 2)
print("влево на два знака = ", a << 2)
print("Побитовое исключающее или = ", a ^ b)