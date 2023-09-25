fr = open('kucera/2/hada.txt', 'r')

zoz = fr.readlines()
num_of_games = len(zoz)
print('pocet hier je', num_of_games)

len_zoz = [len(i) for i in zoz]
print('najdlhsia hra je', sorted(len_zoz)[-1] - 1, 'krokov dlha')

fw = open('kucera/2/hada_write.txt', 'w')

counter = 0
for i in zoz:
    temp = i[0]
    for j in i:
        if j == temp:
            counter += 1
        else:
            fw.write(temp + ' ' + str(counter) + ' ')
            temp = j
            counter = 1
    fw.write('\n')
