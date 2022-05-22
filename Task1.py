# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

def list_of_numbers(N):
    list = []
    for i in range(N):
        list.append((-3)**i)
    print(list)

N = int(input(f'Введите количество членов последователности N: '))
list_of_numbers(N)