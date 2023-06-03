import string

fr = open('text/objednane_jedla.txt')
order = fr.read()

lunch = {}
numlun = 0
not_enough = []

for i in order:
    if i in string.ascii_lowercase:
        lunch[i] = lunch.get(i, 0) + 1
for i in lunch:
    numlun += lunch[i]
    if lunch[i] < 20:
        not_enough.append(i)
    else:
        print('obedov', i, 'je dost')
print('pocet objednanych jedal:', numlun)
print(lunch)
print('objednalo si menej ako 20 ludi', not_enough)
