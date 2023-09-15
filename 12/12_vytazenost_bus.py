fr = open("12/bus_vytazenost.txt", 'r', encoding="UTF-8")

capacity = int(fr.readline())
zoz = fr.readlines()
print("pocet zastavok je", len(zoz))

zoz = [i.split() for i in zoz]
for i in range(len(zoz)):
    zoz[i][0], zoz[i][1] = int(zoz[i][0]), int(zoz[i][1])
    zoz[i][2] = " ".join(zoz[i][2:])
print("nazvy zastavok:", ", ".join([i[2] for i in zoz]))

overcap = {}
for i in zoz:
   capacity -= i[0] - i[1]
   if capacity < 0:
       overcap[i[2]] = capacity

if len(overcap) > 0:
    print("bus bol preplneny na zastavke/zastavkach", ", ".join([i for i in overcap]))
    print("najviac zatazena zastavka je", sorted(overcap, key= lambda x: overcap[x])[0])
else:
    print("ziadna zastavka nebola vytazena")
