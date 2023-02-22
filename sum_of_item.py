
# Найдите сумму цифр трехзначного числа.



number = int(input('ВВедите трехзначное число: '))

# sum = int (number % 10 + number / 10 % 10 + number / 100 % 10)

sum = int(number % 10 + ((number - number % 10) / 10 % 10) + ((number - number % 100) / 100 % 10))

print(sum)



# sum = int(number % 10 + ((number - number % 10) / 10 % 10) + ((number - number % 100) / 100 % 10))