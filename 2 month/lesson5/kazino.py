import random

from decouple import config


def kazino():

    money = config('MONEY', cast = int)
    balance = money


    while True:

        

        
        b = int(input('Выберите число: '))

    
        c = int(input('Сделайте ставку: '))

        a = random.randint(1,31)

        if a == b:
            balance += (c*2)
            
            print (f'You won {c*2}')
        else:
            balance -= c
            print(f'Вы проиграли {c} денег')

        answer = input('Хотите продолжить? y/n   ')
        
        if answer == 'y':
            
            continue
        else:
            print('Ваш баланс', balance )
            break



