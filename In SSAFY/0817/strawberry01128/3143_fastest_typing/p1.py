import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    whole, part = list(map(str, input().split()))
    # whole = banana part = bana
    print('#{} {}'.format(test_case, len(whole.replace(part,''))+whole.count(part)))
    KT -giga