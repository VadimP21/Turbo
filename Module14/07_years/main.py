def check_year(year):
    year_str = str(year)
    count = 0
    for digit in range(0, 10):
        for number in year_str:
            if digit == int(number):
                count += 1
        if count == 3:
            return int(year)
        count = 0


while True:
    first_year = int(input('\nВведите первый год: '))
    second_year = int(input('Введите второй год: '))
    if first_year < 999 or first_year > 10000 or second_year < 999 or second_year > 10000:
        print('Введите четрехзначные числа')
    elif second_year < first_year:
        print('Введите года по возрастанию')
    else:
        print('Годы от', first_year, 'до', second_year, 'с тремя одинаковыми цифрами:')
        for year in range(first_year, second_year + 1):
            year_special = check_year(year)
            if year_special != None:
                print(year_special)
