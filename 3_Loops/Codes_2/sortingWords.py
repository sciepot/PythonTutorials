'''
Вам дан список слов. Вам необходимо отсортировать слова в алфавитном
порядку
* Вам запрещено использовать функцию sort() и sorted()

Пример:
    вводные данные
    [pineapple, apple, orange, banana]

    выходные данные
    [apple, banana, orange, pineapple]
'''

def sortAl(l):
    # Здесь начинается ваш код
    for i in range(len(l)):
        for x in range(i + 1, len(l)):
            if l[i] > l[x]:
                temp = l[x]
                l[x] = l[i]
                l[i] = temp
    # Здесь заканчиваеся ваш код
    return l



from colorama import Fore
testcases = [['pineapple', 'apple', 'orange', 'banana'],
             ['pineapple', 'apple', 'orange', 'apple'],
             ['pineapple', 'pear', 'banana', 'apple']]


iError = False
dError = False
iCount = 0
dCount = 0
for i, test in enumerate(testcases):
    res = sortAl(test.copy())
    sorted = test.copy()
    sorted.sort()
    if res == sorted:
        print(Fore.GREEN, f'Тест #{i + 1} пройден!')
        iCount += 1
    else:
        print(Fore.RED, f'Тест #{i + 1} ПРОВАЛЕН!!!')
        print(Fore.RED, f'Ваш ответ:\n{res}')
        print(Fore.RED, f'Правильный ответ:\n{sorted}')
    print(Fore.WHITE)