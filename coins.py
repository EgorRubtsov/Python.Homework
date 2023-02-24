# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# ыведите минимальное количество монет, которые нужно перевернуть

from random import randint

n = int(input('Сколько у вас монеток?: '))

countEagles = 0     #количество монет с "орлом"

countTails = 0      #количество монет с "решкой"

minCoins = 0        # монет к перевороту

for i in range(n):
    
    sideOfCoin = randint (0, 1)

    print(sideOfCoin)

    if sideOfCoin == 0:
        countEagles += 1

    if sideOfCoin == 1:
        countTails += 1


if countEagles > countTails:
    minCoins = n - countEagles
    if minCoins == 0: print('Ничего не нужно переворачивать, у вас одна монета')
    else: print(f'Необходимо перевернуть {minCoins} решек')

    

if countTails > countEagles:
    minCoins = n - countTails
    if minCoins == 0: print('Ничего не нужно переворачивать, у вас одна монета')
    else: print(f'Необходимо перевернуть {minCoins} орлов') 

    

if countTails == countEagles:

    minCoins = n - countTails or countEagles

    print(f'Необходимо перевернуть {minCoins} орлов или решек')

        
