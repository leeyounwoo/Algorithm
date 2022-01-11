import sys
sys.stdin = open('1005/woosteelz/5203_베이비진/sample_input.txt')


def check_run(arr):
    for i in range(8):
        if arr[i]:
            if arr[i+1] and arr[i+2]:
                return True
    return False


def check_triplet(arr):
    for a in arr:
        if a >= 3:
            return True
    return False


TC = int(input())
for tc in range(1, TC + 1):
    card = list(map(int, input().split()))

    player1 = [0] * 10
    player2 = [0] * 10
    winner = 0
    for i in range(len(card)):
        # 홀수일 경우
        if i & 1:
            player2[card[i]] += 1
            if check_run(player2) or check_triplet(player2):
                winner = 2
                break
        else:
            player1[card[i]] += 1
            if check_run(player1) or check_triplet(player1):
                winner = 1
                break

    print(f"#{tc} {winner}")
