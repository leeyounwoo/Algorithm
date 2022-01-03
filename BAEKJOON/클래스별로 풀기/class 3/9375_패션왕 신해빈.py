import sys

sys.stdin = open('input.txt')
for T in range(int(input())):
    n = int(input())
    clothes = {}
    for _ in range(n):
        name, key = map(str, sys.stdin.readline().rstrip().split())
        if key not in clothes:
            clothes[key] = 1
        else:
            clothes[key] += 1
    ans = 1
    # 해당 카테고리의 옷의 수 + 1 (해당 카테고리의 옷을 입지 않는 경우)
    for key in clothes.keys():
        ans *= clothes[key] + 1
    # -1 (알몸인 경우 제외)
    print(ans-1)