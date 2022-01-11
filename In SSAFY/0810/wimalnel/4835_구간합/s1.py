import sys
# input.txt 파일에서 입력값 불러오는 코드
sys.stdin = open('input.txt')

T = int(input()) # 테케 입력

## N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.

##M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
for tc in range(1, T+1):  # 테케 루프 돕니다~
    N, M = list(map(int, input().split())) #N개의 입력받을 정수 , M개의 합인지
    Num = list(map(int, input().split())) #공백기준 리스트에 자르는 Num배열
    result = [0] * (N + 1) # 누적합 구하기위해 배열만들기  계산을 쉽게하려고 0번에 0을넣음
    # 만약 5번째 자리 누적합은 누적합[5] - 누적합[5-3]을 계산하면됨  2차원배열 N^2의 시간복잡도나오는걸
    # 배열N 누적합N 원하는값 계산 N 해서 3N으로 O(N) 시간복잡도

## M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오
    for i in range(1, N + 1):
        result[i] = Num[i - 1] + result[i - 1]
    # M번째를 최대값과 최소값으로 설정
    minnum = maxnum = result[M]
    # 반복을 돌면서 최소값과 최대값 찾기
    for i in range(M, N + 1):
        minnum = min(minnum, result[i] - result[i - M])
        maxnum = max(maxnum, result[i] - result[i - M])
    # 결과출력
     print("#{} {}".format(tc, maxnum - minnum) #최대값에서 최소값 뺀 결과 출력