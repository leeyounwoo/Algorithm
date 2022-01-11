import sys
sys.stdin = open('input.txt')

for test_case in range(1,11):
    Test_number = int(input())
    result = []
    for bet in range(100):
        Test_box = list(map(int, input().split()))
        result.append(Test_box)
    max_total = 0
    for i in range(100):
        total = 0
        for j in range(100):
            total += result[i][j]
            if total > max_total:
                max_total = total
    for i in range(100):
        total = 0
        for j in range(100):
            total += result[j][i]
            if total > max_total:
                max_total = total
    for i in range(100):
        total = 0
        total += result[i][i]
        if total > max_total:
            max_total = total
    print('#{} {}'.format(test_case,max_total))





