import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    str1 = input()
    str2 = input()

    max_num = 0
    for st1 in str1:
        count = 0
        for st2 in str2:
            if st1 == st2:
                count += 1
        if max_num < count:
            max_num = count
    print('#{0} {1}'.format(tc+1, max_num))

