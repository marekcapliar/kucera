from string import ascii_uppercase

text = input("Napis vety na zasifrovanie (iba velke pismena a medzery): ")
cipher = ['', "ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZ"]
new_text = ""
counter = {}
for i in text:
    if i == ' ':
        new_text += '0 '
        counter[0] = counter.get(0, 0) + 1
    else:
        temp = ord(i) - 65
        new_text += str((temp)//3 + 1)*(temp%3 + 1) + ' '
        counter[(temp)//3 + 1] = counter.get((temp)//3 + 1, 0) + (temp%3 + 1)
print(new_text) 
# print(sorted(counter, key= lambda x: counter[x], reverse= True))
highest = []
temp = 0
for i in counter:
    if temp == counter[i]:
        highest.append(str(i))
    elif counter[i] > temp:
        highest = [str(i)]
        temp = counter[i]
print("Najčastejšie zvolené políčka:", ", ".join(highest))