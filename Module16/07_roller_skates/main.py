list_of_skates = []
list_of_people = []
go_ride = 0

amount_of_skates = int(input('Кол-во коньков: '))
for i_skates in range(amount_of_skates):
    print('Размер ' + str(i_skates + 1) + '-й пары: ', end= '')
    size = int(input())
    list_of_skates.append(size)

amount_of_people = int(input('\nКол-во людей: '))
for i_people in range(amount_of_people):
    print('Размер ноги ' + str(i_people + 1) + '-го человека: ', end= '')
    size = int(input())
    list_of_people.append(size)

for count_s in range(4):
    for count_p in range(3):
        if list_of_people[count_p] <= list_of_skates[count_s]:
            go_ride += 1
            list_of_skates[count_s] -= 100
            break

print('\nНаибольшее кол-во людей, которые могут взять ролики: ', go_ride)
