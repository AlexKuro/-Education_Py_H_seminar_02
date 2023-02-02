
""" 
Задача 1. Напишите программу, которая принимает на вход вещественное число 
и показывает сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11 
"""

print("\nЯ подсчитаю сумму всех введеных цифр.")

numbStr = input("Введите любое число, тип int или float: ")
resultSum = 0
numList = []

for i in range(0, len(numbStr)):
    numList.append(numbStr[i])

for i in numList:
    if i == '-':
        numList.remove('-')
    elif i == '.':
        numList.remove('.')

for i in numList:
    resultSum += int(i)

print("\tСумма цифр", end=' ')
print(f"{numbStr} --> {resultSum}\n")
