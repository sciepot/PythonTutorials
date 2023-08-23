'''
Вам необходимо написать программу которая будет отбирать абитуриентов в MIT.
Каждому абитуриенту необходимо ввести свои данные через терминал.
Отбор студентов строго введется по определенным критериям:
    1. Абитуриент старше 16 лет (включительно) и младше 30 лет (включительно).
    2. IELTS абитуриента выше 7 баллов (включительно).
    3. SAT выше 1400 баллов
    4. Если SAT выше 1500 баллов, то результаты IELTS не важны.
    5. Если у абитуриента имеются олимпиадные грамоты, то результаты SAT и IELTS не важны.

Подсказки:
    Для начала отсейте всех кандидатов не подходящих по возрасту.
    Сначала рассмотрите 4 и 5 критерии: вначале примите всех олимпиадников,
    а затем тех у кого SAT выше 1500 (для этой группы результат IELTS не важен).
    Затем расмотрите абитуриентов без квот по критериям 2 и 3.

Пример:
    Сколько вам лет?
    18
    Какой у вас результат IELTS?
    7.5
    Какой у вас результат SAT?
    1420
    Есть ли у вас олимпиадные грамоты?
    нет
    Поздравляем, вы приняты!!!

    Сколько вам лет?
    16
    Какой у вас результат IELTS?
    5.5
    Какой у вас результат SAT?
    1490
    Есть ли у вас олимпиадные грамоты?
    нет
    Спасибо за ваше внимание. Мы обязательно вам позвоним;)
'''

age = int(input('Сколько вам лет?\n'))
ielts = int(input('Какой у вас результат IELTS?\n'))
sat = int(input('Какой у вас результат SAT?\n'))
isMedalist = True if input('Есть ли у вас олимпиадные грамоты?\n') == 'да' else False

accepted = False

# Здесь начинается ваш код

# Здесь заканчивается ваш код

if accepted: print('Поздравляем, вы приняты!!!')
else: print('Спасибо за ваше время. Мы обязательно вам перезвоним;)')