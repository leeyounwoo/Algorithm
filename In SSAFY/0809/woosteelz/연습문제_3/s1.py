import sys
# input 파일을 불러오기 위한 코드
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(TC):
    area = int(input())
    arr = list(map(int, input().split()))
    max_temp = max(arr)
    for i in arr:
        if i == max_temp:
            area -= 1
    print(tc, area)