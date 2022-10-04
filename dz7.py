#ДЗ 7
'''
1. Написать функцию binary_search, принимающую в качестве входящего параметра
элемент для поиска и список в котором необходимо искать.
2. Алгоритм должен искать с помощью двоичного поиска, изображенного на блок-схеме
презентации.
3. Функция в итоге должна распечатать результат.
4. Написать функцию buble_sort или selection_sort, принимающую в качестве входящего
параметра не отсортированный список.
5. Алгоритм функции должен сортировать список методом пузырьковой сортировки или
методом сортировки выбором.
6. Функция в итоге должна возвращать отсортированный список.
'''
# 1111111


def binary_search(a, list):
    list.sort()
    print(list)
    first = 0  
    length = len(list)
    last = length - 1  
    middle_index = (first + last) // 2  
    middle = list[middle_index] 

    while True:
        if first == last:
            if a != middle:
                print(f'Число {a} не найдено в данном списке')
                break

        elif a == middle:
            print(f"Число {a} найдено в списке под индексом {middle_index}")
            break

        elif a < middle:
            high = middle_index - 1
            last = high
            middle_index = (first + last) // 2
            middle = list[middle_index]
            if a == middle:
                print(f"Число {a} найдено в списке под индексом {middle_index}")
                break

        elif a > middle:
            low = middle_index + 1
            first = low
            last = length - 1
            middle_index = (first + last) // 2
            middle = list[middle_index]
            if a == middle:
                print(f"Число {a} найдено в списке под индексом {middle_index}")
                break


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


binary_search(2, list)



# 2222222222



# def bubble_sort(a):
#     size = len(a)
#     step = 0
#     index = size - 1
#     for i in range(index):
#         for b in range(0, index - i):
#             if a[b] > a[b + 1]:
#                 step = a[b]
#                 a[b] = a[b + 1]
#                 a[b + 1] = step

#     print(a)


# list = [1, 7, 3, 4, 9, 8, 11, 10, 5, 2, 6]
# bubble_sort(list)

