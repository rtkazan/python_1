from random import randint
coins = int(input('Введите количество монет: '))
orel_1 = 0
reshka_0 = 0
for i in range(coins):
    side = randint(0, 1)
    if side == 0:
        reshka_0 = reshka_0 + 1
        print(side)
    else:
        orel_1 = orel_1 + 1
        print(side)
if reshka_0 < orel_1:
    print(reshka_0)
else:
    print(orel_1)
