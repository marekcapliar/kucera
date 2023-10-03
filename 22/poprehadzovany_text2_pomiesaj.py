import random
from string import ascii_letters


def pomiesaj(retazec):
    pismenka = list(retazec)
    random.shuffle(pismenka)
    return ''.join(pismenka)


fr = open("kucera/22/poprehadzovany_text_vstup2.txt", 'r', encoding="UTF-8")
fw = open("kucera/22/poprehadzovany_text.txt", 'w', encoding="UTF-8")
text = fr.readlines()
print("".join(text), '\n')
fr.close()
new_text = ""
for j in text:
    for i in j.split():
        if i[0] in ascii_letters and i[-1] in ascii_letters:
            new_text += i[0] + pomiesaj(i[1:-1]) + i[-1] + ' '
        elif i[0] not in ascii_letters:
            new_text += i[0:2] + pomiesaj(i[2:-1]) + i[-1] + ' '
        elif i[-1] not in ascii_letters:
            new_text += i[0] + pomiesaj(i[1:-2]) + i[-2:] + ' '
    new_text += '\n'
fw.write(new_text)
fw.close()