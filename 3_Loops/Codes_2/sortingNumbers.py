'''
Вам дан список чисел от 1 до 100. Вам необходимо написать две программы:
Первая сортирует список в порядке убывания,
Вторая сортирует список в порядке возрастания.
* Вам запрещено использовать функцию sort() и sorted()

Пример:
    вводные данные
    [3, 1, 2, 4]

    выходные данные
    Первая программа: [1, 2, 3, 4]
    Вторая программа: [4, 3, 2, 1]
'''

def increaseSort(l): # В порядке возрастания 1 2 3 4
    # Здесь начинается ваш код
    # Здесь заканчиваеся ваш код
    return l

def decreaseSort(l): # В порядке убывания 4 3 2 1
    # Здесь начинается ваш код
    # Здесь заканчиваеся ваш код
    return l

from colorama import Fore
testcases = [[3, 2, 1, 4, 5],
             [1, 2, 3, 4, 5],
             [2, 3, 1, 2, 4],
             [5, 4, 3, 2, 1],
             [1, 2, 1, 2, 1]]


iError = False
dError = False
iCount = 0
dCount = 0
print('Тест на сортировку в порядке возрастания')
for i, test in enumerate(testcases):
    res = increaseSort(test.copy())
    sorted = test.copy()
    sorted.sort()
    if res == sorted:
        print(Fore.GREEN, f'Тест #{i + 1} пройден!')
        iCount += 1
    else:
        print(Fore.RED, f'Тест #{i + 1} ПРОВАЛЕН!!!')
        print(Fore.RED, f'Ваш ответ:\n{res}')
        print(Fore.RED, f'Правильный ответ:\n{sorted}')
    print()

print(Fore.WHITE, 'Тест на сортировку в порядке убывания')
for i, test in enumerate(testcases):
    res = decreaseSort(test.copy())
    sorted = test.copy()
    sorted.sort(reverse=True)
    if res == sorted:
        print(Fore.GREEN, f'Тест #{i + 1} пройден!')
        iCount += 1
    else:
        print(Fore.RED, f'Тест #{i + 1} ПРОВАЛЕН!!!')
        print(Fore.RED, f'Ваш ответ:\n{res}')
        print(Fore.RED, f'Правильный ответ:\n{sorted}')
    print()
print(Fore.WHITE)
