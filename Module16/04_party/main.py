guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

come_or_gone = 'Party'

while come_or_gone != 'Пора спать':
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    come_or_gone = input('Гость пришёл или ушёл? ')
    if come_or_gone == 'пришёл':
        name = input('Имя гостя: ')
        if len(guests) < 6:
            print('Привет, ' + name + '!')
            guests.append(name)
        else:
            print('Прости, ' + name + ', но мест нет.')
    elif come_or_gone == 'ушёл':
        name = input('Имя гостя: ')
        print('Пока,', name, '!')
        guests.remove(name)
    elif come_or_gone == 'Пора спать':
        print('\nВечеринка закончилась, все легли спать.')
        break