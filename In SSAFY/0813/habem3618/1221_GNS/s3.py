import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1+T):
    _ = input()
    number_map = {
        "ZRO": 0,
        "ONE": 1,
        "TWO": 2,
        "THR": 3,
        "FOR": 4,
        "FIV": 5,
        "SIX": 6,
        "SVN": 7,
        "EGT": 8,
        "NIN": 9,
    }
    string = input().split()
    string.sort(key=lambda num: number_map[num])
    print('#{} {}'.format(tc, ' '.join(string)))
