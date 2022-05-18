def smallest_divisor(number):
    for divider in range(2,number + 1):
        if number % divider == 0:
            smallest_divisor = divider
            return smallest_divisor

number = int(input('Введите число: '))

smallest_divisor = smallest_divisor(number)
print('Наименьший делитель, отличный от единицы: ', smallest_divisor)

