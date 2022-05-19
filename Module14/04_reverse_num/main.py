def reverse_number_int(number):
    result = 0
    n_temp = number
    amount_of_numbers = 0
    while n_temp != 0:
        division_n = n_temp // 10
        amount_of_numbers += 1
        n_temp = division_n

    for count in range(amount_of_numbers - 1, -1, -1):
        digit = 10 ** count
        division_n = number // 10
        number_n = number - 10 * division_n
        number = division_n
        result += number_n * digit
    return result


def revers_number_of_fraction(number):
    number_str = str(number)
    amount_of_digits = -2
    for count in number_str:
        amount_of_digits += 1
    number *= 10 ** amount_of_digits

    result = 0
    n_temp = number
    amount_of_numbers = 0
    while n_temp != 0:
        division_n = n_temp // 10
        amount_of_numbers += 1
        n_temp = division_n

    for count in range(amount_of_numbers - 1, -1, -1):
        digit = 10 ** count
        division_n = number // 10
        number_n = number - 10 * division_n
        number = division_n
        result += number_n * digit

    revers_number_of_fraction = result / 10**amount_of_numbers
    return revers_number_of_fraction



number_first = float(input('Введите первое число: '))
number_second = float(input('Введите второе число: '))


number_int = int(number_first)
number_fraction = round(number_first - number_int, 14)

resoult_int = reverse_number_int(number_int)
resoult_fraction = revers_number_of_fraction(number_fraction)

reverse_number_first = resoult_int + resoult_fraction

number_int = int(number_second)
number_fraction = round(number_second - number_int, 14)

resoult_int = reverse_number_int(number_int)
resoult_fraction = revers_number_of_fraction(number_fraction)

reverse_number_second = resoult_int + resoult_fraction

print(reverse_number_first)
print(reverse_number_second)
print(reverse_number_first + reverse_number_second)