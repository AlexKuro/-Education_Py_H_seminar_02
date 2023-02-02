import random

""" 
Задача 3. Задайте список из n чисел последовательности
(1 + 1/n)^n и выведите на экран их сумму. 
"""

print("\nПрограмма, выводит сумму последовательности (1 + 1/n)^n")
# number = int(input("Введите число, для набора произведений чисел: "))
number = random.randint(3, 10)
result = 0
summa = 0

print(f"Последовательность (1 + 1/n)^n из {number} чисел--> ", end='[ ')

for i in range(1, number + 1):
    result = round(((1 + 1/i)**i), 2)
    summa += result
    print(result, end=' ')

print(end=']')
print(f"\nСумма последовательности (1 + 1/n)^n из {number} чисел --> {summa}")

print(end='\n\n')
