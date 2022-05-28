
fst_list = []
scd_list = []

for i_fst_list in range(3):
    print('Введите ' + str(i_fst_list + 1) + '-е число для первого списка:', end=' ')
    num_frt_list = int(input())
    fst_list.append(num_frt_list)

for i_scd_list in range(7):
    print('Введите ' + str(i_scd_list + 1) + '-е число для второго списка:', end=' ')
    num_scd_list = int(input())
    scd_list.append(num_scd_list)

print('\nПервый список:', fst_list)
print('Второй список:', scd_list)

fst_list.extend(scd_list)

for i in range(1, 10):
    fst_list.count(i)
    for _ in range(fst_list.count(i) - 1):
        fst_list.remove(i)

print('\nНовый первый список с уникальными элементами:', fst_list)