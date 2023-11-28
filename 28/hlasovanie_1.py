def uprav(text):
    new = [int(i[:-1]) for i in text]
    new[-1] = int(text[-1])
    return new


fr = open("kucera/28/hlasovanie_1.txt", 'r', encoding="UTF-8")
hlasovanie = fr.readlines()
fr2 = open("kucera/28/hlasovanie_vypadnuti.txt", 'r', encoding="UTF-8")
vypadnuti = fr2.readlines()

print("Celkovy pocet sms je", len(hlasovanie))

sutaziaci = {i:0 for i in range(5220, 5230)}
hlasovanie = uprav(hlasovanie)
vypadnuti = uprav(vypadnuti)
for i in sutaziaci:
    sutaziaci[i] = hlasovanie.count(i)
    print("Sutaziaci cislo", i, "dostal", sutaziaci[i], "hlasov")

temp = sutaziaci
zoradenie = sorted(sutaziaci.items(), key= lambda x: x[1])
posledny_bez_vypadnutia = zoradenie[0][0]
for i in vypadnuti:
    temp.pop(i)
zoradenie = sorted(temp.items(), key= lambda x: x[1])
posledny = zoradenie[0][0]
print("Posledny bol", posledny)
print("Posledny s vypadnutymi bol", posledny_bez_vypadnutia)
