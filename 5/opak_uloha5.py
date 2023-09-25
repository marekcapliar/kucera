fr = open('priklady_5_7-main/text/objednane_jedla.txt')

zoz = fr.readlines()
print('pocet jedal je', len(zoz))

zoz_jedal = {}
for i in zoz:
    zoz_jedal[i[-2]] = zoz_jedal.get(i[-2], 0) + 1

malo_jedal = []
print('pocet objednanych jedal:')
for i in zoz_jedal:
    print(i, ':', zoz_jedal[i])
    if zoz_jedal[i] < 20:
        malo_jedal.append(i)

if len(malo_jedal) == 0:
    print('z kazdeho jedla sa objednalo dost')
else:
    print('nedostatok si objednali ' + str(malo_jedal)[1:-1])
