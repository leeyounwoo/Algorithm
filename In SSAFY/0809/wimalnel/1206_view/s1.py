import sys
# input.txt 파일에서 입력값 불러오는 코드
sys.stdin = open('input.txt')

Tc = 10 # 테케는 10개입력
for tc in range(1, Tc+1):  # 테케 10개 루프 돕니다~
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0  # 결과값 저장변수

#접근 아이디어 : 하나의 빌딩이 조망권이 확보되는 조건을 확인하고 모던 빌딩에 적용
#처음 2개와 마지막 2개 할 필요X
#왼쪽 i-2, i-1,  오른쪽 i+1, i+2  //가장 큰 값이 필요하다. 조망권 검사
#조망권 검사 후 값을 누적한다.
    # 2 ~ N-2 각각 검사해서
    for i in range(2, N-2):
        high = max(arr[i-2],arr[i-1],arr[i+1],arr[i+2]) # 왼쪽과 오른쪽 비교할 제일 큰 빌딩 high
        # 최소값이 양수이면 조망권이 확보
        if arr[i] - high > 0 :
            result += arr[i] - high  # 조망권이 확보된 빌딩 높이의 누적합
    print("#{} {}".format(tc, result)) # 테케와 결과값 출력
