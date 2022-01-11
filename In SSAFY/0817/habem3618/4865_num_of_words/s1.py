import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    str1 = str(set(str1))

    count = 0
    result = dict()

    for i in str1:
        for j in str2:
            if i == j:
                count += 1
                result[i] = count
        count = 0

    print("#{} {}".format(tc, max(result.values())))
