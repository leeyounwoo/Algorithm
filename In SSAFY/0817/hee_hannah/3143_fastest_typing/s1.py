import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    a, b = map(str, input().split()) # 각각 변수에 담아준다 banana, bana
    total = a.count(b) # 바나나에서 바나의 수를 센다 1
    a = a.replace(b, "") # 바나나에서 바나를 공백으로 대체한다
    total += len(a) # 남은 na의 글자수를 총합에 더한다

    print('#{} {}'.format(tc, total))
