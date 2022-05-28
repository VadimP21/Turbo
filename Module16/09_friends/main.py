def total_list_form(amount_of_friends):
    total_list = []
    personal_list = [0, 0]

    for i_friend in range(1, amount_of_friends + 1):
        personal_list.insert(0, i_friend)
        total_list.append(personal_list)
        personal_list = [0, 0]
    return total_list

amount_of_friends = int(input('Кол-во друзей: '))
amount_of_debt_lists = int(input('Долговых расписок: '))

total_list = total_list_form(amount_of_friends)

for i_debt_list in range(amount_of_debt_lists):
    print('\n' + str(i_debt_list + 1) + '-я расписка')
    debtor = int(input('Кому: '))
    borrower = int(input('От кого: '))
    debt = int(input('Сколько: '))

    total_list[borrower - 1][1] += debt
    total_list[debtor - 1][2] -= debt

print('\nБаланс друзей:')

for i in range(amount_of_friends):
    print(str(total_list[i][0]) + ': ' + str(total_list[i][1] + total_list[i][2]))

