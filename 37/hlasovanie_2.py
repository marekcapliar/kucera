fr = open("kucera/37/hlasovanie_1.txt", 'r', encoding="UTF-8")
hlasy = fr.readlines()
fr.close()
poradie = {str(i): [] for i in range(5220, 5230)}
for i in range(len(hlasy)):
    poradie[hlasy[i].rstrip('\n')].append(str(i))

for i in poradie:
    meno = "kucera/37/" + i + ".txt"
    fw = open(meno, 'w', encoding="UTF-8")
    fw.write('\n'.join(poradie[i]))
    fw.close()