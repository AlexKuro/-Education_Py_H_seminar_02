""" 
Задача 5. Реализуйте алгоритм перемешивания списка.
"""
print("\n\tАлгоритм перемешивания списка.")
print("Cписок до: ")

array = []
n = 20

for i in range(0, n):
    array.append(i)

print(array)
print()
for i in range(0, len(array)):
    temp = array[i]
    array[i] = array[2+i//2]
    array[2+i//2] = temp
    for i in range(0, len(array)):
        temp = array[i]
        array[i] = array[2+i//2]
        array[2+i//2] = temp
print("Cписок после: ")
print(array)
print()
print("Cписок отсортированный: ")
print(sorted(array))
print()
