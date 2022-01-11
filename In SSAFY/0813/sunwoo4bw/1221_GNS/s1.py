import sys
sys.stdin = open('input.txt')

T = int(input())
extrasolar_str = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# 문자열을 받아 작은 수부터 차례로 정렬
# 문자별로 숫자를 지정해줘야겠네..?
for _ in range(1, T + 1):
    tc, num = map(str, input().split())
    num_list = list(map(str, input().split()))
    # ['SVN', 'FOR', 'ZRO', 'NIN', ...]

    extrasolar_num = []
    for n in num_list :
        tmp = extrasolar_str.index(n)
        extrasolar_num.append(tmp)

    # 문자로 재변환
    result = []
    for tn in sorted(extrasolar_num):
        result.append(extrasolar_str[tn])
    print(tc)
    print(' '.join(result))
