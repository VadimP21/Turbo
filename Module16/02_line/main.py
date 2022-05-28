# TODO здесь писать код
def selection_sort(my_list):
    for i_mn in range(len(my_list)):
        for curr in range(i_mn, len(my_list)):
            if my_list[curr] < my_list[i_mn]:
                my_list[curr], my_list[i_mn] = my_list[i_mn], my_list[curr]




first_list = []
second_list = []

for i_fst_list in range(160, 177, 2):
    first_list.append(i_fst_list)

for i_scd_list in range(162, 181, 3):
    second_list.append(i_scd_list)

first_list.extend(second_list)

selection_sort(first_list)

print('Отсортированный список учеников:', first_list)