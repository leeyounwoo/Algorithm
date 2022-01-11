import sys
sys.stdin = open('input.txt')

def  pay(cost, mon):
    global min_cost

    if mon > 12:
        min_cost = min(cost, min_cost)
        return
    
    # 1일 이용권과 1달 이용권 비교
    pay(cost + min(swim[mon] * day, month1), mon+1)

    # 3달 이용권
    pay(cost + month3, mon+3)


T = int(input())

for t in range(1, T+1):
    day, month1, month3, year = map(int, input().split())
    swim = [0] + list(map(int, input().split()))

    min_cost = year
    pay(0, 1)

    print('#{} {}'.format(t, min_cost))