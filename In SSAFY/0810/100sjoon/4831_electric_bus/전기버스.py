import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split()) # K : 한번충전최대이동칸, N : 종점정류장, M : 충전기설치된 정류장 갯수
    char_num = list(map(int, input().split()))

    for i in range(len(char_num)):
<<<<<<< HEAD
    
=======
>>>>>>> c6b6b91356014bd7b5ce2c3d64ab19c4dfbe8d25
