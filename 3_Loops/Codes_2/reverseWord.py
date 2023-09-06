'''
Задать
Вам необходимо написать прграмму, которая записывает буквы в слове в обратном порядке

Пример:
    входные данные
    'apple'

    выходные данные
    'elppa'
'''

def reverseWord(word):
    reversed = ''
    # Здесь начинается ваш код
    
    # Здесь заканчиваеся ваш код
    return reversed



from colorama import Fore
testcases = ['apple', 'banana', 'abba']
trueres = ['elppa', 'ananab', 'abba']


for i, test in enumerate(testcases):
    res = reverseWord(test)
    if res == trueres[i]:
        print(Fore.GREEN, f'Тест #{i + 1} пройден!')
    else:
        print(Fore.RED, f'Тест #{i + 1} ПРОВАЛЕН!!!')
        print(Fore.RED, f'Ваш ответ:\n{res}')
        print(Fore.RED, f'Правильный ответ:\n{trueres[i]}')
    print(Fore.WHITE)