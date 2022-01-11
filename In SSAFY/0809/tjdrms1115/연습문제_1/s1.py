import sys
sys.stdin = open('input.txt')

# 1. 두자리 숫자 입력받기
a = int(input())

# 2. 띄어쓰기로 구분된 숫자 시퀀스 받기
b = list(map(int, input().split()))

# 3. N줄에 걸쳐 받기
T = int(input())
c = []
for tc in range(T):
    c.append(list(map(int, input().split())))