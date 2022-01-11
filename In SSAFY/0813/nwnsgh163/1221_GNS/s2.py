import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    _ = input()
    string = input().split()

    number_map = {
        "ZRO" : 0,
        "ONE" : 0,
        "TWO" : 0,
        "THR" : 0,
        "FOR" : 0,
        "FIV" : 0,
        "SIX" : 0,
        "SVN" : 0,
        "EGT" : 0,
        "NIN" : 0,
    }


    for word in string:
        number_map[word] += 1

    result = ''
    for key, value in number_map.items():
        # ZRO ZRO ZRO...
        result += (key + ' ') * value


    print('#{} {}'.format(tc, result))