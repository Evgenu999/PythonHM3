# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным  и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
print(list)

fractional_part =[]
for i in range(len(list)):
        if (list[i] % 1) != 0:
            fractional_part.append(round((list[i] % 1), 3))

print(fractional_part)
print(round(( max(fractional_part) - min(fractional_part) ), 3))