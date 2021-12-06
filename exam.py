#2 Написати програму на мові Python, яка обчислює значення функції y = 4x3-2x2 + 5 для значень x, що змінюються від -3 до 1, з кроком 0.1.
def range1(start, stop, step):
    while start < stop:
        yield start
        start = start + step

seq = range1(-3, 1, 0.1)

for x in seq:
    y = (4 * x**3) - (2 * x**2) + 5
    print(y)

print('-----------------')

#3 Написати програму на мові Python, яка виводить в стандартний потік виведення кількість парних чисел в заданому списку.
list = [5, 21, 6, 41, 88, 18]
for num in list:
    if num % 2 == 0:
     print(num, end=' ')
print()
print('-----------------')
#4 Написати програму на мові Python, яка видаляє в заданому непорожньому тексті всі пари букв виду abab. Результуючий текст вивести на екран монітора.

string = 'abab helloabab world!ab'
string = string.replace('ab','')
print(string)

print('-----------------')

#5Написати програму на мові Python, яка виводить 10 рядків із значенням числа Pi. У першому рядку повинно бути 2 знака після коми, у другій 3 і так далі.
from math import pi
for i in range(2,12):
    long = 'pi = {:.' + str(i) + 'f}'
    print(long.format(pi))

print('end')