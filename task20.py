"""
*Задача 20: * В настольной игре Скрабл (Scrabble) 
каждая буква имеет определенную ценность. В случае 
с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
 D, G – 2 очка; B, C, M, P – 3 очка; 
 F, H, V, W, Y – 4 очка; K – 5 очков; 
 J, X – 8 очков; Q, Z – 10 очков. 
 А русские буквы оцениваются так: 
 А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
 Д, К, Л, М, П, У – 2 очка; 
 Б, Г, Ё, Ь, Я – 3 очка; 
 Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; 
 Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
 Напишите программу, которая вычисляет стоимость 
 введенного пользователем слова. Будем считать, 
 что на вход подается только одно слово, которое 
 содержит либо только английские, либо только русские буквы.

*Пример:*
ввод - >  ноутбук
вывод ->    12
"""

english_alphabet = {'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 
                    'N':1, 'S':1, 'T':1, 'R':1,
                    'D':2, 'G':2, 'B':3, 'C':3, 'M':3, 'P':3, 
                    'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 'K':5,
                    'J':8, 'X':8, 'Q':10, 'Z':10}
russian_alphabet = {'А':1, 'В':1, 'Е':1, 'И':1, 'Н':1, 'О':1, 
                    'Р':1, 'С':1, 'Т':1, 'Д':2, 'К':2, 'Л':2, 
                    'М':2, 'П':2, 'У':2, 'Б':3, 'Г':3, 'Ё':3, 
                    'Ь':3, 'Я':3, 'Й':4, 'Ы':4, 'Ж':4, 'З':4, 
                    'Х':4, 'Ц':4, 'Ч':5, 'Ш':8, 'Э':8, 'Ю':8, 
                    'Ф':10, 'Щ':10, 'Ъ':10}
wordFromPlayer = str(input("Введите слово: "))     # введенное слово игрока
wordFromPlayer = wordFromPlayer.upper()            # .upper() - переводит все буквы в верхний регистр
sumOfPoints = 0                                    # переменная для подсчета количества очков
for letter in wordFromPlayer:                      # перебор букв в слове
    if letter in english_alphabet:                 # сравнение буквы с алфавитом
        sumOfPoints += english_alphabet[letter]    # плюсуем значение буквы к сумме
    elif letter in russian_alphabet:               # сравнение буквы с другим алфавитом
        sumOfPoints += russian_alphabet[letter]    # плюсуем значение буквы к сумме
print(f"Сумма очков за слово {wordFromPlayer} равняется {sumOfPoints}")




 
