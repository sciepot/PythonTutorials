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
    # Здесь начинается ваш код
     
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
for l, r in zip(ls, rs):
    pri