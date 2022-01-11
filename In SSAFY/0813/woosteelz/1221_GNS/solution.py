import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(TC):
    num_dict = {
        "ZRO": 0, "ONE": 0,
        "TWO": 0, "THR": 0,
        "FOR": 0, "FIV": 0,
        "SIX": 0, "SVN": 0,
        "EGT": 0, "NIN": 0
    }
    a, b = map(str, input().split())
    arr = list(map(str, input().split()))
    for num in arr:
        num_dict[num] += 1

    print('#{}'.format(tc+1))
    for key, value in num_dict.items():
        for _ in range(value):
            print(key, end=' ')

