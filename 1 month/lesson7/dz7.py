'''
ДЗ:
Собственным делителем числа называется всякий его делитель, отличный от самого числа. 
Напишите функцию, которая будет возвращать список всех собственных делителей заданного числа. 
Само это число должно передаваться в функцию в виде единственного аргумента. 
Результатом функции будет перечень собственных делителей числа, собранных в список. 
Основная программа должна демонстрировать работу функции, запрашивая у пользователя число 
и выводя на экран список его собственных делителей. Программа должна запускаться только в том случае, 
если она импортирована в виде модуля в другой файл.


Доп:
Напишите программу, которая будет запрашивать у пользователя чис- ла, пока он не пропустит ввод. 
Сначала на экран должно быть выведено среднее значение введенного ряда чисел, после этого друг за другом 
неoбходимо вывести список чисел ниже среднего, равных ему (если такие найдутся) и выше среднего. 
Каждый список должен предваряться соответствующим заголовком.

'''
# dz

import statistics
import delitel

print(delitel.delitel(x = int(input('Введите число для проверки собственного делителя: '))))



# dopzadanie

'''

b=list()
while True:
        a = input("Введите целые числа, когда закончите, оставьте строку пустой: ")
        if a != "":
            b.append(int(a))
            continue
        else:
            print("Вы закончили ввод")
            break
b.sort()
i = statistics.mean(b)
n = list()
r = list()
v = list()
for y in b:
        if y < i:
                n.append(y)
        elif y == i:
                r.append(y)
        else:
                v.append(y)


print('Ваш список чисел: ',b)
print("Среднее значение Ваших чисел: ", i)
print("Числа ниже среднего: ", n)
print('Числа равны среднему: ', r)
print('Числа выше среднего: ', v)

'''

