from string import ascii_lowercase
import random


def encrypting(text_input, cipher):
    new_text = ""
    for j in text_input:
        new_text += chr(cipher + 96)
        for letter in j:
            if letter in ascii_lowercase:
                letter_new = chr((ord(letter) - 97 + cipher) % 26 + 97)
                new_text += letter_new
            else:
                new_text += letter
        cipher = random.randint(1, 25)
    return new_text


def decrypting(text_input):
    new_text = ""
    for i in text_input:
        key = ord(i[0]) - 96
        for letter in i[1:]:
            if letter in ascii_lowercase:
                letter_new = chr((ord(letter) - 97 - key + 26) % 26 + 97)
                new_text += letter_new
            else:
                new_text += letter
    return new_text


clean_text = open("kucera/24/vstupny_text.txt", 'r', encoding="UTF-8")
text = clean_text.readlines()

encrypt_text = open("kucera/24/zasifrovany_text_2.txt", 'r', encoding="UTF-8")
text_encrypted = encrypt_text.readlines()

new_encrypted_text = open("kucera/24/new_encryption.txt", 'w' , encoding="UTF-8")
new_encrypted_text.write(encrypting(text, 2))

new_derypted_text = open("kucera/24/new_decryption.txt", 'w' , encoding="UTF-8")
new_derypted_text.write(decrypting(text_encrypted))