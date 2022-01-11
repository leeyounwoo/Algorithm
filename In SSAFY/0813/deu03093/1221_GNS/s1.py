import sys

sys.stdin = open('input.txt')
string_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for T in range(1, int(input()) + 1):
    tc, strings_size = map(str, input().split())
    strings = list(input().split())
    # 각 숫자가 몇번 발생하는지
    ans = [0] * 10
    for string in strings:
        ans[string_list.index(string)] += 1
    print('#{}'.format(T))
    # 0부터 9까지 발생한 횟수만큼 문자열 출력
    for i in range(10):
        for j in range(ans[i]):
            print(string_list[i], end=' ')
    print()