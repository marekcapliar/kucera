import random


def my_checker(guess, win):
    guess = guess.split()
    win_num = []
    win_count = 0
    for i in guess:
        if int(i) in win:
            win_num.append(i)
            win_count += 1
    return win_num, win_count


def checker(guess, win):
    global correct_guesses
    win_count = 0
    for i in guess:
        if int(i) in win:
            win_count += 1
    correct_guesses[win_count] += 1
    return 0


fr = open("kucera/25/loteria_2.txt", 'r', encoding="UTF-8")
tickets = fr.readlines()
tickets = [i.split() for i in tickets]

numbers = [i for i in range(1, 50)]
winning_numbers = []
for i in range(6):
    winning_numbers.append(random.choice(numbers))
    numbers.remove(winning_numbers[-1])

correct_guesses = {i: 0 for i in range(7)}

tipy = input("Daj svoj tip (1-49): ")
moj_tip = my_checker(tipy, winning_numbers)
print("moje vyherne cisla: " + ' '.join([str(i) for i in moj_tip[0]]) + "\nuhadol si " + str(moj_tip[1]) + " cisel")
print("Vyherne cisla su " + ' '.join([str(i) for i in winning_numbers]))

for i in tickets:
    checker(i, winning_numbers)
correct_guesses.pop(0)
correct_guesses.pop(4)
print(correct_guesses)
