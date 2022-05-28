shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail = input('Название детали: ')

count_detail = 0
price_detail = 0

for i_detail in shop:

        if i_detail[0] == detail:
                count_detail += 1
                price_detail += i_detail[1]

print('Кол-во деталей —', count_detail)
print('Общая стоимость —', price_detail)
