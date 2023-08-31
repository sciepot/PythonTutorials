'''
У вас есть список пищевых ингредиентов, и также вам дан другой список ингредиентов для
приготовления определенного блюда. Вам необходимо создать программу, которая будет
проверять, имеются ли в наличие необходимые ингредиенты.

Входные данные
    ['cheese', 'brocoli', 'dough', 'tomato', 'ham', 'noodles']
    ['cheese', 'dough', 'ham']
Выходные данные
    []

Примеры:
    входные данные
    ['cheese', 'brocoli', 'tomato', 'noodles']
    ['cheese', 'dough', 'ham']
    выходные данные
    ['dough', 'ham']
'''
def prog(l, r):
    ret = []
    # if 'cheese' in l => True/False
    
    # Здесь начинается ваш код
    for i in r: #i = 'cheese'
        if not (i in l):
            ret.append(i)
    # Здесь заканчивается ваш код
    return ret

from colorama import Fore
ls= [['cheese', 'brocoli', 'dough', 'tomato', 'ham', 'noodles'],
     ['cheese', 'brocoli', 'tomato', 'noodles'],
     ['cheese', 'brocoli', 'dough']]
rs = [['cheese', 'dough', 'ham'],
     ['cheese', 'dough', 'ham'],
     ['cheese', 'brocoli', 'dough', 'tomato']]
ans = [[],
       ['dough', 'ham'],
       ['tomato']]
for i in range(3):
    res = prog(ls[i], rs[i])
    if res == ans[i]:
        print(Fore.GREEN, f'Тест #{i + 1} пройден!')
        print(Fore.GREEN, f'Правильный вывод:{ans[i]}')
    else:
        print(Fore.RED, f'Тест #{i + 1} ПРОВАЛЕН!!!')
        print(Fore.RED, f'Полученный вывод:{res}')
        print(Fore.RED, f'Ожидаемый вывод:{ans[i]}')
    print(Fore.WHITE)