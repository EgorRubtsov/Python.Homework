#  Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#  Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 списка. 1 строка - первый список через пробел. 2 строка - второй список через пробел.



string_1 = set(map(int, input('Введите ряд чисел через пробел: ').split()))
string_2 = set(map(int, input('Введите еще один ряд чисел через пробел: ').split()))


multiplication = list(string_1.intersection(string_2))
print(*multiplication)
