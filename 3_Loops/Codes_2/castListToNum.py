'''
Вам нужно из списка цифр составить число
Пример:
    входные данные
    [3, 1, 4, 1, 5]

    выходные данные
    31415
'''

def castListToNum(l):
    num = 0
    # Здесь начинается ваш код
    
    # Здесь заканчиваеся ваш код
    return num



from colorama import Fore
testcases = [[3, 1, 4, 1, 5],
             [0, 1, 2, 3],
             [5, 3, 1, 4, 1, 5]]

truenum = [31415, 123, 531415]

for i, test in enumerate(testcases):
    res = castListToNum(test)
    if res == truenum[i]:
        print(Fore.GREEN, f'Тест #{i + 1} пройден!')
    else:
        print(Fore.RED, f'Тест #{i + 1} ПРОВАЛЕН!!!')
        print(Fore.RED, f'Ваш ответ:\n{res}')
        print(Fore.RED, f'Правильный ответ:\n{truenum[i]}')
    print(Fore.WHITE)