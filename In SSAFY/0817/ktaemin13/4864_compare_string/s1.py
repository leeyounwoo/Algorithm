import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    str1 = list(map(str, (input())))
    str2 = list(map(str, (input())))

    str_list = []
    result = 0
    cnt = 0

    while cnt < (len(str2)-1):
        for chr in str2[cnt: len(str1) + cnt]:
            str_list.append(chr)
            if str_list == str1:
                result = 1
        cnt += 1
        str_list = []

    print('#{0} {1}'.format(tc+1, result))
