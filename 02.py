
# 2.	Напишите функцию, которая проверяет: является ли слово палиндромом
def polindrom(s):
    s=s.split()
    s=''.join(s)

    if s==s[::-1]:
        print('это слово полиндром')
    else:
        print(('это слово не полиндром'))

polindrom('jgkglgl')


