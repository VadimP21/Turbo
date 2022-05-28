def is_simmetric(numbers_list):
    half_word = len(numbers_list) // 2
    is_palindrome = True
    for i_simm in range(half_word):
        if numbers_list[len(numbers_list) - i_simm - 1] != numbers_list[- len(numbers_list) + i_simm]:
            is_palindrome = False
    return is_palindrome

numbers_list = []

amount_of_numbers = int(input('Кол-во чисел: '))

for i_number in range(amount_of_numbers):
    number = int(input('Число: '))
    numbers_list.append(number)

new_list = []

count = 0

for i in range(amount_of_numbers):
    numbers_list.insert(amount_of_numbers, numbers_list[count])
    new_list.insert(0, numbers_list[count])
    count += 1
    if is_simmetric(numbers_list):
        print('Последовательность:', numbers_list)
        print('Нужно приписать чисел:', count)
        print('Сами числа:', new_list)
        break

