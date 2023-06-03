import random


def evenodd(otazken):
    if len(exam) > 0:
        last = list(exam.values())[-1]
        while last % 2 == otazken % 2:
            otazken = random.choice(questions)
    return otazken


number_of_students = 30   # 1-30
no_questions = 50  # 1-50

students = [x for x in range(1, number_of_students+1)]
questions = [x for x in range(1, no_questions + 1)]

exam = {}
if number_of_students < no_questions:
    for i in range(number_of_students):
        obet = random.choice(students)
        otazka = random.choice(questions)

        evenodd(otazka)

        students.remove(obet)
        questions.remove(otazka)
        exam[obet] = exam.get(obet, otazka)
else:
    print('nedostatok otazok')
print(exam)

