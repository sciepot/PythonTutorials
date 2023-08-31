'''
Вам необходимо написать прграмму, которая записывает элементы в списке в обратном порядке

Пример:
    входные данные
    [1, 2, 3, ..., 4, 5]

    выходные данные
    [5, 4, 3, 2, 1]
'''
'''
for -1 -2 -3 -4 -5
reversed = []
reversed.append(l[-1]) [5]
reversed.append(l[-2]) [5, 4, 3, 2, 1]
reversed.append(l[-3])

'''
l = [1, 2, 3, 4, 5]
r = []
for i in range(1, len(l)+1): # -1, -2, -3, -4, -5 
    r.append(l[-i])
print(r)
p= []

for i in range(len(l) - 1, -1, -1): # 4, 3, 2, 1, 0
    p.append(l[i])
print(p)