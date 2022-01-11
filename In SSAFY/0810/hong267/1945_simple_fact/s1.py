import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = [0] * 5 # 2 3 5 7 11의 제곱 수를 리스트로 만들기 위한 카운트 리스트

    while True: # N을 2, 3, 5, 7, 11로 나눠 준 후 numbers의 각 인덱스에 카운트
        if N % 2 == 0:
            N = N // 2 # N을 해당 수로 나눈 후에는 몫으로 바꿔줌
            numbers[0] += 1
        elif N % 3 == 0:
            N = N // 3
            numbers[1] += 1
        elif N % 5 == 0:
            N = N // 5
            numbers[2] += 1
        elif N % 7 == 0:
            N = N // 7
            numbers[3] += 1
        elif N % 11 == 0:
            N = N // 11
            numbers[4] += 1
        elif N == 1: # 반복적으로 나누다가 N이 1이 되면 더 이상 나눌 수 없으므로 break
            break

    print('#{0} {1} {2} {3} {4} {5}'.format(tc, numbers[0], numbers[1], numbers[2], numbers[3], numbers[4]))
