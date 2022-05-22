# Пользователь задаёт две строки. 
# Определить количество вхождений одной строки в другой.

def the_number_of_occurrences_of_one_string_in_another(text1, text2):
    count = 0
    for i in text2:
        for j in text1:
            if i == j:
                count += 1
    return count

text1 = input('Введите строку 1: ')
text2 = input('Введите строку 2: ')
print(the_number_of_occurrences_of_one_string_in_another(text1, text2))