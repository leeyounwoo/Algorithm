import sys
# input.txt 파일에서 입력값 불러오는 코드
sys.stdin = open('input.txt')

def binary_search(start, end, target, count):  #이진탐색 함수정의
    mid = int(start+end)//2  # 중간페이지
    if mid == target:
        return count  #누가 이겼는지 알아내기 위해 카운트
    if target > mid:   #오른쪽 검색
        return binary_search(mid, end, target, count+1)
    else:           #왼쪽검색
        return binary_search(start, mid, target, count+1)

T=int(input())

for t in range(1, T+1):
    P, A, B = map(int, input().split())
    count_A = binary_search(1, P, A, 0)
    count_B = binary_search(1, P, B, 0)
    if count_A > count_B:  # B가 이김
        print("#{} B".format(t))
    elif count_A == count_B:  # 무승부
        print("#{} 0".format(t))
    else:            # A가 이김
        print("#{} A".format(t))