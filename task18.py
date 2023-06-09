"""
Задача 18: Требуется найти в массиве A[1..N] 
самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число 
N – количество элементов в массиве. В последующих  
строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
ввод 5
вывод массива -> 1 2 3 4 5
ввод 6
вывод  -> 5
"""

from random import randint
n = int (input("Введите количество элементов "))
list_1 = [randint(1, 100) for _ in range(n)]
x = (int(input("Введите X ")))
print(list_1)
number = list_1[0]
for i in range(n):
    if abs(list_1[i] - x) < abs(number - x):   
        number = list_1[i]                    
print(f"Самым близким элементом к числу Х({x}) является ",number)

# abs возвращает абсолютное значение числа
# то-есть результат его всегда положительный
# х = -5, print(abs(x))     -> 5