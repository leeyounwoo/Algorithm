import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    s = int(input())
    num_list = list(map(int, input()))
    count = [0 for _ in range(10)]

    for i in num_list:
        count[i] += 1

    max_card = max(count)
    max_idx = 0
    for i in range(len(count)):
        if max_card == count[i]:
            max_idx = i

    print("#{} {} {}".format(test_case, max_card, max_idx))
