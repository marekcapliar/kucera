def spracuj_riadok(riadok):
    znaky = ['0', '1']
    new_riadok = ""
    for i in riadok.split(' '):
        new_riadok += int(i)*znaky[0]
        znaky = znaky[::-1]
    return new_riadok


fr = open("kucera/34/skuska.txt", 'r', encoding="UTF-8")
dimensions = fr.readline()
picture = fr.readlines()

print("Sirka:", dimensions.split(' ')[0], '\nvyska:', dimensions.split(' ')[1], 'pocet znakov:', int(dimensions.split(' ')[0]) * int(dimensions.split(' ')[1].rstrip()))

fw = open("kucera/34/dekompresia_obrazka_vystup.txt", 'w', encoding="UTF-8")
fw.write(dimensions)
for i in picture:
    fw.write(spracuj_riadok(i) + '\n')