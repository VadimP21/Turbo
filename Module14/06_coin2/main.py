import math


def check_monet(x, y, r_check):
    r = math.sqrt(x ** 2 + y ** 2)

    if r <= r_check:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


while True:
    print('\nВведите координаты монетки:')
    x = float(input('X: '))
    y = float(input('Y: '))
    r_check = float(input('Введите радиус: '))

    check_monet(x, y, r_check)

