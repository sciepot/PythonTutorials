'''
Задать
Вам необходимо написать прграмму, которая записывает цифры в числе в обратном порядке

Пример:
    входные данные
    12345

    выходные данные
    54321
'''

def reverseNum(num):
    # Здесь начинается ваш код
    
    # Здесь заканчиваеся ваш код
    return num



from colorama import Fore
testcases = [4321, 2340, 1200, 100]
trueres = [1234, 432, 21, 1]


for i, test in enumerate(testcases):
    res = reverseNum(test)
    if res == trueres[i]:
        print(Fore.GREEN, f'Тест #{i + 1} пройден!')
    else:
        print(Fore.RED, f'Тест #{i + 1} ПРОВАЛЕН!!!')
        print(Fore.RED, f'Ваш ответ:\n{res}')
        print(Fore.RED, f'Правильный ответ:\n{trueres[i]}')
    print(Fore.WHITE)