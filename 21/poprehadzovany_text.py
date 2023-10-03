import random

fr = open("kucera/21/poprehadzovany_text1_vstup.txt", 'r', encoding="UTF-8")
text = fr.readlines()
print(''.join(text), '\n')
fr.close()

text = [i.split() for i in text]
new_text = ""
for j in text:
    for i in j:
        word = [l for l in i[1:-1]]
        new_text += i[0]
        for j in range(len(i)-2):
            temp = random.choice(word)
            new_text += temp
            word.pop(word.index(temp))
        new_text += i[-1] + ' '
    new_text += '\n'
fw = open("kucera/21/poprehadzovany_text1.txt", 'w', encoding="UTF-8")
fw.write(new_text[:-1])
fw.close()
