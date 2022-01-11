import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    # if str1 in str2:
    #     print('#{} 1'.format(tc))
    # else:
    #     print('#{} 0'.format(tc))

    flag = 1
    for i in range(len(str2)-len(str1)+1):
        flag = 1
        for j in range(len(str1)):
            if str1[j] != str2[i+j]:
                flag = 0
                break

        if flag:
            break

    if flag:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))