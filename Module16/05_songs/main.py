violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

num_songs = int(input('Сколько песен выбрать? '))
total_duration = 0
count = 1

for i in range(num_songs):
    print('Название', i + 1, 'песни: ', end=' ')
    name_song = input()
    count += 1
    for i_song in violator_songs:

        if name_song == i_song[0]:
            total_duration += i_song[1]

print('\nОбщее время звучания песен: ', round(total_duration, 2), 'минуты')