import sys
# input 파일을 불러오기 위한 코드
sys.stdin = open('input.txt')

N1 = int(input())

arr1 = list(map(int, input().split()))

N2 = int(input())

arr2 = []
for _ in range(N2):
    temp = list(map(int, input().split()))
    arr2.append(temp)

