# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).



length = int(input('ВВедите длину (число долек) шоколадки: '))

width = int(input('ВВедите ширину (число долек) шоколадки: '))

number = int(input('Сколько долек вы хотите отломить?: '))

chocolate = length * width     #Вводим эту переменную для того, чтобы при проверке условия разлома шоколадки
                               # нам обязательно пришлось ее разломить, то есть если человек захочет съесть шоколад целиком, 
                               # не разламывая, это не будет соответствовать проверки условия на разлом шоколадки.

if (number % length == 0   or number % width == 0) and number < chocolate:

    print('Вы можете разломить шоколадку на два прямоугольника :)')

else:
    print('У вас не выйдет разломить шоколадку на два прямоугольника :(')