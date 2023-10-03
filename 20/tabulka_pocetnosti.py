from string import ascii_uppercase

fr = open("kucera/20/tabulka_pocetnosti.txt", 'r', encoding="UTF-8")
text = fr.read()
print(text)
text = text.upper()

znaky = dict([str(i) + str(0) for i in ascii_uppercase])    # treba zlepsit
for i in znaky:                                             # nech tam nie je tento for loop
    znaky[i] = int(znaky[i])

for i in text:
    if i in ascii_uppercase:
        znaky[i] = znaky.get(i) + 1

nula_znakov = []
for i in znaky:
    if znaky[i] > 0:
        print(i, '-', znaky[i])
    else:
        nula_znakov.append(i)
print("Znaky ktore sa nevyskytli:", ", ".join(nula_znakov))