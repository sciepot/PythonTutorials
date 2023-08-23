'''
Вам необходимо создать программу которая будет брать email адрес
и возвращать его написанным с заглавными буквами и без домена.

Подсказки:
    Используйте slicing (вырезание подстроки) для удаление домена

Пример:
    Введите email адресс:
    fake.address@gmail.com
    FAKE.ADDRESS

    Введите email адресс:
    my_address123@mail.ru
    MY_ADDRESS123
'''

address = input('Введите email адресс:') # строка, пример 'fake.address@gmail.com'
# address = fake.address@gmail.com

# Здесь начинается ваш код
indexDog = address.find('@')
address = address[:indexDog]
address = address.upper()
# Здесь заканчивается ваш код

print(address) # строка, пример 'FAKE.ADDRESS'