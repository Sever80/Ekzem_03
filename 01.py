# 1.	Напишите функцию, которая будет принимать номер кредитной карты
# и показывать только последние 4 цифры.
# Остальные цифры должны заменяться звездочками

def my_card(x):
    print( '*' * len(x[:-4]) + x[-4:])

my_card(input('Введите номер карты:'))