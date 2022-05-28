
amount_of_people = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый ' + str(amount_of_people) + '-й человек')

# amount_of_people = 5
# number = 7
print('Значит, выбывает каждый ' + str(number) + '-й человек')

list_of_people = list(range(1, amount_of_people + 1))
print(list_of_people)
start_number = 0

for i_round in range(1, amount_of_people):
    print('\nТекущий круг людей: ', list_of_people)
    print('Начало счёта с номера ', list_of_people[start_number])
    i_out = number % amount_of_people - 1 + start_number
    print('Выбывает человек под номером ', list_of_people[i_out])
    start_number = list_of_people.index(list_of_people[i_out % (amount_of_people - 1)])
    list_of_people.remove(list_of_people[i_out])
    amount_of_people -= 1

print('\nОстался человек под номером', list_of_people[0])

