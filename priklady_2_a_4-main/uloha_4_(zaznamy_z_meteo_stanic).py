fr = open('text/meteo_stanice.txt', 'r')

fr_cely = fr.read()
poc = 0
for i in fr_cely:
    if i in '\n':
        poc += 1
print('pocet merani:', poc)

fr.seek(0)
zoz = fr.readlines()
zoz_teploty = []
for i in range(poc):
    teplota = ''
    temperature = ''
    riadok = zoz[i]
    for a in range(5):
        teplota += riadok[21 + a]
    if riadok[21] == '+':
        for e in range(4):
            if riadok[22 + e] == ',':
                temperature += '.'
            else:
                temperature += riadok[22 + e]
    else:
        for f in range(5):
            if riadok[21 + f] == ',':
                temperature += '.'
            else:
                temperature += riadok[21 + f]
    zoz_teploty.append(float(temperature))
    print(teplota)

zoz_teploty.sort()
print('')
print(zoz_teploty[-1])

string_naj_teplota = ''
kod = ''
for i in str(zoz_teploty[-1]):
    if i == '.':
        string_naj_teplota += ','
    else:
        string_naj_teplota += i
for i in zoz:
    if string_naj_teplota in i:
        for a in range(3):
            kod += i[a]
print(kod)

sucet = 0
for i in zoz_teploty:
    sucet += i
priemer = sucet / len(zoz_teploty)
print(priemer)
