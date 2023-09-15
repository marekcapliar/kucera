fr = open("11/sutaz_vbehu.txt", 'r', encoding="UTF-8")

zoz = fr.readlines()
print("Počet zúčastnených športovcov:", len(zoz))

for i in range(len(zoz)):
    zoz[i] = zoz[i].split()
    zoz[i][1] = int(zoz[i][1])
    print("Súťažiaci", zoz[i][0], "dobehol do cieľa za", zoz[i][1], "sekúnd")

zoz = sorted(zoz, key= lambda x: x[1])
print("Najlepsi sutaziaci je", zoz[0][0], "s casom", zoz[0][1], "sekund")
