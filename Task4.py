# Написать программу получающую набор 
# произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

def set_of_products_of_numbers(N):
    set = []
    set.append(1)
    for i in range(1, N):
        set.append(set[i-1]*(i+1))
    return(set)

N = int(input(f'Введите число N: '))
print(set_of_products_of_numbers(N))
