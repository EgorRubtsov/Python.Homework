


# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
#  D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; 
#  J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
#   Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; 
#   Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
#   Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
#   Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.



dict_british = {1: 'A, E, I, O, U, L, N, S, T, R', 2: 'D, G', 3: 'B, C, M, P', 4: 'F, H, V, W, Y', 5: 'K', 8: 'J, X', 10: 'Q, Z'}

dict_russian = {1: 'А, В, Е, И, Н, О, Р, С, Т', 2: 'Д, К, Л, М, П, У', 3: 'Б, Г, Ё, Ь, Я', 4: 'Й, Ы', 5: 'З, Х, Ц, Ч', 8: 'Ш, Э, Ю', 10: 'Ф, Щ, Ъ'}







word = input('Напишите слово, стоимость которого хотите узнать: ')



result = 0

if word[0] in 'abcdefghijklmnopqrstuvwxyz':
    for i in word:
        for k, v in dict_british.items():
            if i.upper() in v:
                result += k
    print(f'Стоимость вашего слова: {result}')

if word[0] in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
    for i in word:
        for k, v in dict_russian.items():
            if i.upper() in v:
                result += k
    print(f'Стоимость вашего слова: {result}')
    
  

    







# result = sum([k for i in word for k, v in dict_british.items() if i in v])

# print(result)

# print(sum([k for i in word for k, v in dict_russian.items() if i in v]))



# print(word)
# result = 0
# for i in word:
#     result += word[i]
# print(result)