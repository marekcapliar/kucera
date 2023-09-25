fr = open('kucera/14/skok_do_dialky.txt', 'r', encoding="UTF-8")
zoz = fr.readlines()
zoz = list(map(lambda x: x.split(), zoz))

print("Zucastnene krajiny: " + ', '.join([i[1] for i in zoz]))

contestants = {}
for i in zoz:
    contestants[i[1]] = contestants.get(i[1], 0) + 1
print("Pocty sutaziacich z jednotlivych krajin: " + ", ".join([i + ": " + str(contestants[i]) for i in contestants]))

vysledky = {}
for i in zoz:
    vysledky[i[0]] = sorted([int(j) for j in i[2::]], reverse=True)

temp = 0
vyherci = []
for i in vysledky:
    if vysledky[i][0] > temp:
        temp = vysledky[i][0]
        vyherci = [i]
    elif vysledky[i][0] == temp:
        vyherci.append(i)
print(vyherci)