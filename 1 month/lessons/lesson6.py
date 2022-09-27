# lamda function анонимные функции


# def sum(a, b):
#     return a + b

# a = sum(10, 2)
# print(a)

# msg = lambda: print('hello')
# msg()


# sum = lambda a, b: a + b
# a = sum(10, 2)
# print(a)
# print(sum(13, 6))

# square = lambda n: n * n
# print(square(5))
# print(square(2))
# print(square(23))

# def square2(n): return n * n
# print(square2(2))
# print(square(2))


# def do_operation(a, b, oper):
#     res = oper(a, b)
#     print(f'result = {res}')

# do_operation(2, 3, lambda a, b: a + b)
# do_operation(6, 3, lambda a, b: a / b)
# do_operation(2, 3, lambda a, b: a * b)




# def select_operations(choice):
#     if choice == 1:
#         return lambda a, b: a + b
#     elif choice == 2:
#         return lambda a, b: a - b
#     elif choice == 3:
#         return lambda a, b: a * b
#     else:
#         return lambda a, b: a // b

# oper = select_operations(1) # первый вариант 
# print(oper(12,3))

# oper = select_operations(2) # второй вариант
# res = oper(5, 3)
# print(res)



# oper2 = select_operations(3)(2,3)   #третий вариант
# print(oper2)

#  работа с ошибками

# try:
#     string = input('Enter num: ')
#     num = int(string)
#     print(num)
# except:
#     print('Преобразование прошло неудачно')
# finally:
#     print('End of block try ... except ...')

# print('End')


# try:
#     num1 = int(input('Enter first num: '))
#     num2 = int(input('Enter second num: '))
#     print('Res of division: ', num1/num2)
# except ValueError:
#     print('Value error')
# except ZeroDivisionError:
#     print("На ноль делить нельзя")
# except BaseException:
#     print('Error your division')