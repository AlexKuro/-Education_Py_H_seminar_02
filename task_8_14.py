import random

""" 
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
не превосходящие числа N.
Пример: 10 -> 1 2 4 8 
"""

numN = random.randint(1, 11)
result = 0
print(f"\nВыводим все целые числа степени двойки не превосходящие числа {numN} -->", end=' ')
for i in range(0, numN):
    if 2**i < numN:
        result = 2**i
        print(result, end=' ')
print("\n ")