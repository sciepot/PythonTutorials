'''
Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов,
после чего дробная часть копеек отбрасывается. Каждый год сумма вклада становится
больше. Определите, через сколько лет вклад составит не менее y рублей.

Входные данные
    Программа получает на вход три натуральных числа: x, p, y.

Выходные данные
    Программа должна вывести одно целое число.

Примеры
    входные данные
    100
    10
    200
    выходные данные
    8 
'''
x = 100
p = 10
y = 200

i = 0

while x <= y:
    i += 1 # 1, 2, 3, 4 5,
    x += (x * (p/100)) # 133.1
    x = int(x) # x = int(133.1) = 133

print(i)
    # 100 + 100 p/100 = 110
    # 110 + 110 p/100 = 110 + 11 = 121
    # 121 + 121 p/10 = 121 + 12.1 = 133.1 int(133.1) = 133
