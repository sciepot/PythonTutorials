'''
Вам необходимо написать программу которая будет отбирать кандидатов на работу в Google.
Каждому кандидату необходимо ввести свои данные через терминал.
Отбор на работу в Google строго введется по определенным критериям:
    1. Кандиты должны совершеннолетними и младше 65 лет (включительно).
    2. Опыт работы кандита должен быть не менее 2-х лет. 
    3. Для кандит младше 20 лет (включительно) опыт работы не важен.
    4. Кандидаты должны знать такие языки программирования как Python, C++,
        a также еще один дополнительный язык Java или Javascript.
    5. Для кандидат женщин с опытом работы меньше 5-и лет существует квота,
        знание дополнительного языка не обязательна
    6. Для всех кандитов младше 22-х лет (включительно), знание С++ не обязательно
'''

age = int(input('Сколько вам лет?\n'))
exp = int(input('Какой у вас опыт работы?\n'))
isFemale = True if input('Какой ваш пол?\n') == 'ж' else False
knowsPython = True if input('Знаете ли вы Python?\n') == 'да' else False
knowsCpp = True if input('Знаете ли вы C++?\n') == 'да' else False
knowsJava = True if input('Знаете ли вы Java?\n') == 'да' else False
knowsJS = True if input('Знаете ли вы Javascript?\n') == 'да' else False

accepted = False

# Вы старше 18 и вы младше 65 и (либо опыт более 2 лет или вы младше 20 лет)
if age >= 18 and age <= 65 and (exp >= 2 or age <= 20):
    # вы женщина и опыт работы меньше 5 лет
    if isFemale and exp <= 5:
        # вы младше 22 и знаете тогда вы приняты
        if age <= 22 and knowsPython:
            accepted = True
        # вы знаете питон и с++
        elif knowsPython and knowsCpp:
            accepted = True
        else:
            accepted = False
    # вы младше 22 и знаете и (либо джаву или джаваскрипт)
    elif age <= 22 and knowsPython and (knowsJava or knowsJS):
        accepted = True
    # критерии без квоты
    elif knowsPython and knowsCpp and (knowsJava or knowsJS):
        accepted = True
    else: accepted = False
else: accepted = False

if accepted: print('Поздравляем, вы приняты!!!')
else: print('Спасибо за ваше время. Мы обязательно вам перезвоним;)')