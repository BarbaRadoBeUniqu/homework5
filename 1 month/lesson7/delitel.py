# import statistics

def delitel(x):
    
    y = range(1, x)
    z = list()
    for i in y:
        if x % i == 0:
            z.append(i)
    return z  
    
    

# print(delitel(x = int(input('Введите число для проверки: '))))










# print(newfunction(x = int(input('Введите список чисел, когда закончите оставьте строку пустой и нажмите Enter: '))))