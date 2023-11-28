def spracuj_riadok(riadok):
    riadok = riadok[:-1]
    i = 0
    counter = 0
    new_riadok = ""
    char = ['0', '1']
    # if riadok[0] == '0':
    #     while i < len(riadok) and riadok[i] == 0:
    #         counter += 1
    #         i += 1
    #     new_riadok += str(counter) + ' '
    #     counter = 0
    while i < len(riadok):
        while i < len(riadok) and riadok[i] == char[0]:
            counter += 1
            i += 1
        new_riadok += str(counter) + ' '
        char = char[::-1]
        counter = 0
    return new_riadok


fr = open("kucera/29/kompresia_obrazka_1.txt", 'r', encoding="UTF-8")
fw = open("kucera/29/kompresia_obrazka_vystup.txt", 'w', encoding="UTF-8")
tester = open("kucera/29/test.txt", 'r', encoding="UTF-8")


dimensions = fr.readline()
picture = fr.readlines()

# s, v = tester.readline().split(' ')
# s, v = int(s), int(v)
# picture = tester.readlines()
# for i in picture:
#     print(spracuj_riadok(i))

fw.write(dimensions)
for i in picture:
    fw.write(spracuj_riadok(i) + '\n')