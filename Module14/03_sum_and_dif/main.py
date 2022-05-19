def summ_of_numbers(number):
    summ_of_numbers = 0

    while number != 0:
        number_temp = number // 10
        number = number_temp
        summ_of_numbers += 1

    return summ_of_numbers

def summ_all_numbers(number):

    summ_all_numbers = 0
    while number != 0:
        number_temp = number // 10
        number_temp_1 = number - number_temp * 10
        number = number_temp
        summ_all_numbers += number_temp_1
    return summ_all_numbers


number = int(input('Введите число: '))
while number <= 0:
    print('Введите целое положительное число')
    number = int(input('Введите число: '))

summ_of_numbers = summ_of_numbers(number)
summ_all_numbers = summ_all_numbers(number)

print('\nСумма чисел: ', summ_all_numbers)
print('Количество цифр в числе: ', summ_of_numbers)
print('Разность суммы и количества цифр: ', summ_all_numbers - summ_of_numbers)