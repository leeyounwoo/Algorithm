n = int(input())
answers = []
for i in range(n):
    numbers = list(map(int, input().split()))
    student_cnt = numbers[0]
    scores = numbers[1:]
    avg_score = sum(scores) / student_cnt
    cnt = 0
    for i in range(len(scores)):
        if scores[i] > avg_score:
            cnt += 1
    answers.append(round(cnt / student_cnt * 100, 3))
for i in range(len(answers)):
    if int(answers[i]) >= 10:
        temp = 6 - len(str(answers[i]))
    else:
        temp = 5 - len(str(answers[i]))
    print(str(answers[i]), end='')
    for _ in range(temp):
        print('0', end='')
    print('%')
