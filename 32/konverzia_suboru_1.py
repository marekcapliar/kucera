def spracuj_riadok(riadok: str):
    polka = 16 * 16 / 2
    riadok = riadok.rstrip('\n')
    new_riadok = ""
    for i in range(0, len(riadok), 2):
        temp = int(riadok[i:i+2], 16)
        if temp < polka:
            new_riadok += '0 '
        else:
            new_riadok += '1 '
    return new_riadok.rstrip(' ')


fr = open("kucera/32/skuska.txt", 'r', encoding="UTF-8")
dimensions = fr.readline()
picture = fr.readlines()

print("Sirka:", dimensions.split(' ')[0], '\nvyska:', dimensions.split(' ')[1], 'pocet znakov:', int(dimensions.split(' ')[0]) * int(dimensions.split(' ')[1].rstrip()))

fw = open("kucera/32/ciernobiely_obrazok_1_vystup.txt", 'w', encoding="UTF-8")

fw.write(dimensions)
for i in picture:
    fw.write(spracuj_riadok(i) + '\n')
