# Написать функцию, 
# находящую числовой палиндром.

def polindrom(a):
    b = str(a)
    c = int(len(b)/2)
    d = [b]
    count = -1
    for i in range(c):
        #print(i, b[i], b[-i-1])
        if b[i] == b[-i-1]:
            count += 1
            #print(count, i)
    if count == i:
        print(f'Polindrom')
    else:
        print(f'Not polindrom')
    
a = input(f'Введите число a: ')
polindrom(a)
    



