s = int(input('Введите сумму двух чисел: '))
p = int(input('Введите произведение двух чисел: '))
i = 0
for x in range(s):
    y = s - x 
    if x + y == s and x * y == p:
        i = i + 1
        print (x, y)