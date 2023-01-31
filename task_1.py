
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
if float(numbStr) < 1:
    for i in range(2, len(numbStr)):
        resultSum += int(numbStr[i])
elif float(numbStr) > 0:
    for i in range(0, len(numbStr)):
        resultSum += int(numbStr[i])

print("Сумма цифр", end=' ')
print(f"{numbStr} --> {resultSum}")
