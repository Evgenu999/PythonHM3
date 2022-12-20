# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input('Введите число:\n'))

def GetFibonacci(number):

    if number < 0:
        print('Ошибка, введите число больше или равно 0')
    elif number == 0:
        print('Список чисел Фибоначчи => 0')
    elif number == 1:
        print('Список чисел Фибоначчи => [1, 0, 1]')
    else:
        fib_list_positive = [0, 1]
        for i in range(2, number + 1):
            fib_list_positive.append(fib_list_positive[i - 2] + fib_list_positive[i - 1])

    fib_list_negative = []
    for i in range(1, len(fib_list_positive)):
        if i % 2 == 0:
            fib_list_negative.append(-fib_list_positive[i])
        else:
            fib_list_negative.append(fib_list_positive[i])

    fib_list_negative.reverse()

    return(fib_list_negative + fib_list_positive) 

print(f'Список чисел Фибоначчи {number} => {GetFibonacci(number)}')
