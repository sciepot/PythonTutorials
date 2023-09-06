'''
Вам дан список слов. Вам необходимо отсортировать слова в алфавитном
порядку
* Вам запрещено использовать функцию sort() и sorted()

Пример:
    вводные данные
    [pineapple, apple, orange, banana]

    выходные данные
    [apple, banana, orange, pineapple]

[4, 1, 3, 5]

'''

def sortAl(l):
    [1, 2, 3, 3, 5] # 5 > 3, 3 < 5
    # Здесь начинается ваш код bubble sort 
    for i in range(len(l)): # 0 1 2 3 4
        for x in range(i + 1, len(l)): # 1 2 3 4
            if l[i] > l[x]:
                temp = l[i]
                l[i] = l[x]
                l[x] = temp
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