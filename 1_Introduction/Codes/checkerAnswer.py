'''
Вам необходимо написать программу, которая будет исправлять грамматические ошибки
в простых английский приложениях для просто (Present Simple) и просто продолжительного
(Present Continouos) временях. Если приложение не имеет ошибок, то программа должна
отобразить в консоле "Everything is correct!". Если же ошибки есть, то программа
должна вывеси в консоле "You are wrong!!!". Если программа не может проверить предложение,
то она должна отобразить "Can't check:(". В качестве подлежащего программа принимает только местоимения.

Пример:
    Enter sentence:
    I am waiting my friend
    Everything is correct!

    Enter sentence:
    I going to school
    You are wrong!!!

    Enter sentence:
    Tom will play football
    Can't check:(
'''

sen = input('Enter sentence:\n')

sen = sen.split(' ')

if sen[0] == 'I':
    if sen[1] == 'am' and sen[2][-3:] == 'ing': # present continuous
        print('Everything is correct!')
    elif sen[1][-3:] != 'ing': # present simple
        print('Everything is correct!')
    else:
        print('You are wrong!!!')
elif sen[0] == 'You' or sen[0] == 'We':
    if sen[1] == 'are' and sen[2][-3:] == 'ing': # present continuous
        print('Everything is correct!')
    elif sen[1][-3:] != 'ing': # present simple
        print('Everything is correct!')
    else:
        print('You are wrong!!!')
elif sen[0] == 'She' or sen[0] == 'He' or sen[0] == 'It':
    if sen[1] == 'is' and sen[2][-3:] == 'ing': # present continuous
        print('Everything is correct!')
    elif sen[1][-1:] == 's': # present simple
        print('Everything is correct!')
    else:
        print('You are wrong!!!')
else: print('Can\'t check')
