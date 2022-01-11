import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    str1 = input()
    str2 = input()

    i = 0
    result = 0
    while i < len(str2)-len(str1) + 1:
        count = 1
        if str2[i] == str1[0]:
            for check in range(1, len(str1)):
                if str2[i+check] != str1[check]:
                    i += check
                    break
                count += 1
        if count == len(str1):
            result = 1
            break
        i += 1

    print('#{} {}'.format(tc+1, result))
