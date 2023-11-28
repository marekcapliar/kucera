import random


def rotate(string):
    return string[::-1]


fr = open("kucera/27/virus.txt", 'r', encoding="UTF-8")
text = fr.readlines()
fw = open("kucera/27/virus_vystup.txt", 'w', encoding="UTF-8")

print(''.join(text))

riadky = random.choice([True, False])
if riadky:
    random.shuffle(text)

for i in range(len(text)):
    riadok = random.choice([True, False])
    if riadok:
        temp = [x for x in text[i][:-1].split(' ')]
        random.shuffle(temp)
        text[i] = ' '.join(temp)
    else:
        text[i] = text[i][:-1]
    
    line_temp = ""
    for j in text[i].split(' '):
        slovo = random.choice([True, False])
        if slovo:
            line_temp += rotate(j)
        else:
            line_temp += j
        line_temp += ' '
    text[i] = line_temp[:-1]
        
fw.write('\n'.join(text))
       