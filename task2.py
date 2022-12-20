# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]

def GetWorkPairsOfNumbers(list):
    new_list = []
    
    for i in range(round((len(list) + 1) / 2)):
        new_list.append(list[i] * list[-i - 1])

    return new_list


print(f'{list1} =>', end =" ")
print(GetWorkPairsOfNumbers(list1))

print(f'{list2} =>', end =" ")
print(GetWorkPairsOfNumbers(list2))