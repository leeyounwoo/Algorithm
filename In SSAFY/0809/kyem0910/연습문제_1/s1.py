import sys
sys.stdin = open('input.txt')

# 33 입력 받기
number = int(input())

# 1 2 3 4 5 => [1,2,3,4,5]
number = list(map((input.split())))

# N줄에 걸쳐서 숫자 시퀀스
T = int(input())

for tc in range(T):
    numbers = list(map(int,input().split()))
