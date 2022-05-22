# Подсчитать сумму цифр в вещественном числе.

def sum_of_digits_in_float(a):
    sum = 0
    b = list(a)
    for i in b:
        if i != '.':
            sum += int(i)
    return sum

a = input(f'Введите вещественное число: ')
print(f'Сумма цифр числа: {sum_of_digits_in_float(a)}')
