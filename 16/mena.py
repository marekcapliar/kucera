fr = open("kucera/16/mena_zamestnancov.txt", 'r', encoding="UTF-8")
zoz = fr.readlines()
print("Pocet mien v subore je: " + str(len(zoz)//2))
longest_first_name = sorted(zoz[:len(zoz)//2 - 1:], reverse=True)[0]
longest_last_name = sorted(zoz[len(zoz)//2::], reverse=True)[0]
print("Dlzka najdlhsieho krstneho mena:", len(longest_first_name))
print("Dlzka najdlhsieho priezviska je", len(longest_last_name))
print(zoz)
fw = open("kucera/16/vystup.txt", 'w', encoding="UTF-8")
spaces = len(longest_first_name)
for i in range(len(zoz)//2):
    temp = zoz[i][:-1] + ((spaces-len(zoz[i])+1)*' ') + zoz[i + len(zoz)//2]
    fw.write(temp)