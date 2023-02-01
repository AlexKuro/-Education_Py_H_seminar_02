import random

"""
Задача 4. Задайте список из N элементов,
заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.
"""
number = 12
listNum = []
list_is_File = []
for i in range(0, number):
    listNum.append(random.randint(number * -1, number))
print(f"\n\tCписок из {number} элементов: ")
print(listNum)

filename = 'file.txt'
with open(filename) as f_obj:
    lines = f_obj.readlines()

for line in lines:
    list_is_File.append(line.rstrip())
    
#print(list_is_File)

num_list = []

for i in range(0, len(list_is_File)):
    num_list.append(int(list_is_File[i]))

print("\tСписок элементов из file.txt:")
print(num_list)


print("Умножение произведение элементов на указанных позициях:")
count = 0
n = 1
for i in range(1, number, 2):
    print(f"{n}. Позиция(индексы) из file.txt {num_list[count]}", end=" ")
    print(f"{num_list[count + 1]} --> ", end=' ')
    print(f"{listNum[num_list[count]]} * {listNum[num_list[count+1]]} = ", end='')
    print(f"{listNum[num_list[count]] * listNum[num_list[count+1]]}")
    count += 1
    n += 1
print()
#print(" ", listNum[num_list[0]])
#print(" ", lines)
