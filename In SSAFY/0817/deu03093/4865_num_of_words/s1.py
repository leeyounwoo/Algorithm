import sys

sys.stdin = open('input.txt')
for T in range(1, 1 + int(input())):
    str1 = input()
    str2 = input()

    dict_1 = {}
    for i in range(len(str1)):
        dict_1[str1[i]] = 0

    for i in range(len(str2)):
        if str2[i] in str1:
            dict_1[str2[i]] += 1

    # ans = 0
    # for value in dict_1.values():
    #     if value > ans:
    #         ans = value
    ans = max(dict_1.items(), key=lambda pair: pair[1])[1]
    print('#{} {}'.format(T, ans))