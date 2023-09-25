fr = open('priklady_2_a_4-main/text/meteo_stanice.txt', 'r')

merania = fr.readlines()
pocet_merani = len(merania)
print('pocet merani je', pocet_merani, '\n')

merania = [i.split(' ') for i in merania]
teploty = [i[3] for i in merania]
print('namerane teploty:')
for i in teploty:
    print(i)

for i in range(len(teploty)):
    teploty[i] = teploty[i].replace(',', '.')
    match teploty[i][0]:
        case '+':
            teploty[i] = float(teploty[i][1:])
        case '-':
            teploty[i] = float(teploty[i])

top_teplota = sorted(teploty)[-1]
print('najvyssia teplota je', top_teplota)

print('najvyssia teplota je na stanici', merania[teploty.index(top_teplota)][0])

priemer = sum(teploty)/len(teploty)
print('priemer teplot je', priemer)
