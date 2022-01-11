import sys
# input.txt 파일에서 입력값 불러오는 코드
sys.stdin = open('input.txt')

T = int(input()) # 테케 입력

for tc in range(1, T+1):  # 테케 10개 루프 돕니다~
    N = int(input()) #N개의 입력받을 정수
    NList = list(map(int, input().split())) #공백기준 리스트에 자르는 NList선언

    def max(NList):
        max = NList[0]
        for i in range(1, N): # 0 1 2 3 4 5 6 7 8 9 //N이 10이니깐
            if NList[i] > max:
                max = NList[i]
        return max

    def min(NList):
        min = NList[0]
        for i in range(1, N): # 0 1 2 3 4 5 6 7 8 9 //N이 10이니깐
            if NList[i] < min:
                min = NList[i]
        return min

    result = (max(NList)-min(NList)) # max함수와 min함수 이용해서 최대값 - 최소값 계산
    print('#{} {}'.format(tc, result)) # tc 번호와 결과값 출력합니다~