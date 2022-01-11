import sys
sys.stdin = open('input.txt')

def triplet(lst):
    for i in range(len(lst)):
        if lst[i] >= 3:
            lst[i] -= 3
            return True
    
    return False


def check_run(lst):
    for i in range(len(lst)-2):
        if lst[i]:
            if lst[i+1]:
                if lst[i+2]:
                    return True
    
    return False


T = int(input())

for t in range(1, T+1):
    cards = list(map(int, input().split()))

    player1 = [0] * 10
    player2 = [0] * 10

    result = 0

    for i in range(0, len(cards)-1, 2):
        player1[cards[i]] += 1
        player2[cards[i+1]] += 1

        if triplet(player1) or check_run(player1):
            result = 1
            break
        
        if triplet(player2) or check_run(player2):
            result = 2
            break
    
    print('#{} {}'.format(t, result))