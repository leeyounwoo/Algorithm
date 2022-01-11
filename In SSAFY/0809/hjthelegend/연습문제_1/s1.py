import sys
sys.stdin = open('input.txt')

# 1. 두자리 숫자 입력받기 ('33' => 33)
number = int(input())

# 2. 띄어쓰기로 구분된 숫자 시퀀스 받기
# '1 2 3 4 5' => [1, 2, 3, 4, 5]
numbers = list(map(int, input().split()))

# 3. N줄에 걸쳐서 숫자 시퀀스가 들어올 때
T = int(input()) #3

for tc in range(T):
    numbers = list(map(int, input().split()))