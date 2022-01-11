import sys
sys.stdin = open('input.txt')


def run_flag(now, player):
    if now == 0:
        if now+1 in player and now+2 in player:
            return True
        else:
            return False
    elif now == 1:
        if now-1 in player and now+1 in player:
            return True
        elif now+1 in player and now+2 in player:
            return True
        else:
            return False
    elif now == 8:
        if now-1 in player and now+1 in player:
            return True
        elif now-2 in player and now-1 in player:
            return True
        else:
            return False
    elif now == 9:
        if now-2 in player and now-1 in player:
            return True
        else:
            return False
    else:
        if now-1 in player and now+1 in player:
            return True
        elif now-2 in player and now-1 in player:
            return True
        elif now+1 in player and now+2 in player:
            return True
        else:
            return False

for T in range(1, 1+int(input())):
    ans = 0
    cards = list(map(int, input().split()))
    player1 = {}
    player2 = {}
    for i in range(len(cards)):
        if i % 2:
            if cards[i] in player2:
                player2[cards[i]] += 1
            else:
                player2[cards[i]] = 1

            # triplet
            if player2[cards[i]] == 3:
                ans = 2
                break
            # run
            flag = run_flag(cards[i], player2)
            if flag:
                ans = 2
                break
        else:
            if cards[i] in player1:
                player1[cards[i]] += 1
            else:
                player1[cards[i]] = 1
            # triplet
            if player1[cards[i]] == 3:
                ans = 1
                break
            # run
            # print(T, i, cards[i])
            flag = run_flag(cards[i], player1)
            if flag:
                ans = 1
                break
    print('#{} {}'.format(T, ans))