'''
Вам нужно отобразить цифры в числе в виде списка
Пример:
    входные данные
    31415

    выходные данные
    [3, 1, 4, 1, 5]
'''

'''12342 mod 10 = 2
   n   % i  =  element  // j
31415 % 10 = 5 // 1 = 5# 1 i *= 10, j *= 10 [5]
31415 % 100 = 15 // 10 = 1 # 2  [5, 1]
31415 % 1000 = 415 // 100 = 4 # 3 [5, 1, 4]
31415 % 10000 = 1415 // 1000 = 1 # 4 [5, 1, 4, 1, 3]
...
31415 % 100000 = 31415 // 10000 = 3 #
31415 % 1000000 = 31415 // 100000 = 0 # break
'''

n = 31415

l = []
i = 10
j = 1
while True:
    ostatok = n % i 
    element = ostatok // j
    if element <= 0:
        break
    l.insert(0, element)
    i *= 10
    j *= 10
print(l)
