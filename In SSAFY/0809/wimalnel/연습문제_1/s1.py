import sys
# input.txt 파일에서 입력값 불러오는 코드
sys.stdin = open('input.txt')
#위 코드를 통해 자동으로 input() 함수에 값 입력 됨
#즉, 터미널에 직접 input 값을 넣을 필요X

#T = int(input())
#for tc in range(1, 1+T):
#   pass
#1. 두자리 숫자 입력받기 '33'=>33
number = int(input())
#2. 띄어쓰기로 구분된 숫자 시퀀스 받기
#'1 2 3 4 5' => [1, 2, 3, 4, 5]
numbers = list(map(int, input().split()))

#3. N줄에 걸쳐서 숫자 시퀀스가 들어올 때
T = int(input()) # 3

for tc in range(T):
    numbers = list(map(int, input().split()))
