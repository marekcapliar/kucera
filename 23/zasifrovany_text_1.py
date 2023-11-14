from string import ascii_lowercase


def sifruj(vstup, sifra):
    new_text = ""
    for j in range(len(vstup)):
        if vstup[j] in ascii_lowercase:
            cipher_letter = ord(sifra[j%len(sifra)]) - 96
            letter_new = chr((ord(vstup[j]) - 97 + cipher_letter) % 26 + 97)
            new_text += letter_new
        else:
            new_text += vstup[j]
    return new_text



def desifruj(vstup, sifra):
    new_text = ""
    for j in range(len(vstup)):
        if vstup[j] in ascii_lowercase:
            cipher_letter = ord(sifra[j%len(sifra)]) - 96
            letter_new = chr((ord(vstup[j]) - 97 - cipher_letter + 26) % 26 + 97)
            new_text += letter_new
        else:
            new_text += vstup[j]
    return new_text


fr = open("kucera/23/vstupny_text.txt", 'r', encoding="UTF-8")
normal_text = fr.read()

fr2 = open("kucera/23/zasifrovany_text_1.txt", 'r', encoding="UTF-8")
cipher_text = fr2.read()

cipher = "abc"

print(True if desifruj(sifruj(normal_text, cipher), cipher) == normal_text else False)

print(sifruj("maturujeme v pythone", cipher))
print(desifruj("ncwvtxkgpf y rbujrog", cipher))