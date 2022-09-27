
#  Модули


# import msg #если в папке то прописываем путь

# print(msg.hello)
# msg.print_message('ChakNoris')

# from msg import hello, print_message #глобальный вызов

# from msg import * # все импортировать

# print(hello)
# print_message('ChakNoris')

# import message as msg   # псевдонимы

# print(msg.hello)
# msg.print_message('ChakNoris')


# from msg import hello as welcome  # псевдонимы для отдельных элементов модуля

# print(welcome)


# from random import random, randint, randrange  # встроенный модули

# # num = random() * 100
# # num = randint(1, 100)
# num = randrange(10)

# print(num)

# import math

# n1 = math.pow(2,3)
# print(n1)

# n2 = math.sqrt(36)
# print(n2)

# n3 = math.ceil(4.56)
# print(n3)

# n4 = math.floor(4.59)
# print(n4)


import datetime as dt
date = dt.datetime(2022,9,4)
print(date)


