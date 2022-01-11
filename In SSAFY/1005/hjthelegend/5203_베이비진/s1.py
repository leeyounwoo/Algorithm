import sys
sys.stdin = open('input.txt')

t = int(input())
# 연속된 숫자 3개 이상 : run
# 같은 숫자가 3개 이상 : triplet

# 12개의 숫자 카드 : 교대로 1장씩 가져감.
# run or triplet -> 하나라도 충족하면 승리
# 무승부 : 0, or 승자
def triplet(player):
    for i in range(len(player)):
        if player[i] == 3:
            return True
    return False

def runner(player):
    for i in range(8):
        if player[i] != 0:
            if player[i] and player[i+1] and player[i+2]:
                return True
    return False

for tc in range(1, t+1):
    cards = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10

    answer = 0
    for i in range(len(cards)):
        if i % 2 == 0:
            player1[cards[i]] += 1
            if triplet(player1) or runner(player1):
                answer = 1
                break

        else:
            player2[cards[i]] += 1
            if triplet(player2) or runner(player2):
                answer = 2
                break

    print('#{} {}'.format(tc, answer))