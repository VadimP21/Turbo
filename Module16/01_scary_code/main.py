a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
number_5 = a.count(5)
print('Кол-во цифр 5 при первом объединении: ', number_5)

for _ in range(a.count(5)):
    a.remove(5)

a.extend(c)
number_3 = a.count(3)
print('Кол-во цифр 3 при втором объединении: ', number_3)

print('Итоговый список: ', a)


# for i in b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)

# TODO переписать программу
