import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(TC):
    s1 = set(list(str(input())))
    s2 = list(str(input()))

    results = []

    for i in s1:
        results.append(s2.count(i))

    print(f"#{tc+1} {max(results)}")