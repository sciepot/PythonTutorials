'''
Вам дан список учеников и их среднегодовая оценка по предмету представлены
в виде библиотеки, где имена учеников - это ключи, а оценки - значения.
Вам необходимо написать две функции: первая будет расчитывать среднегодовую оценку
по этому предмету, а вторая будет выводить имена учеников, которые получили определенную оценку.
'''

def avgGrade(grades):
    avg = 0
    # Здесь начинается ваш код
    
    # Здесь заканчивается ваш код
    return avg

def students(grades, n):
    students = []
    # Здесь начинается ваш код
    # Здесь заканчивается ваш код
    return students

from colorama import Fore
grades= {'John': 4, 'Steven': 5, 'George': 3, 'Kate': 4, 'Alice': 3, 'Michelle' : 5}
ans = (['George', 'Alice'],
       ['John', 'Kate'],
       ['Steven', 'Michelle'])
res = avgGrade(grades)
if res == 4:
    print(Fore.GREEN, f'Тест на среднегодовую оценке пройден!')
    print(Fore.GREEN, f'Правильный вывод: 4')
else:
    print(Fore.RED, f'Тест на среднегодовую оценке ПРОВАЛЕН!!!')
    print(Fore.RED, f'Правильный вывод: 4')
print()

for i in range(3):
    res = students(grades, i+3)
    if res == ans[i]:
        print(Fore.GREEN, f'Тест #{i + 1} пройден!')
        print(Fore.GREEN, f'Правильный вывод:{ans[i]}')
    else:
        print(Fore.RED, f'Тест #{i + 1} ПРОВАЛЕН!!!')
        print(Fore.RED, f'Полученный вывод:{res}')
        print(Fore.RED, f'Ожидаемый вывод:{ans[i]}')
    print(Fore.WHITE)