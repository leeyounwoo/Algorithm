import sys
sys.stdin = open('input.txt')

def m_code():
    while arr[-1] > 0:  # arr의 맨 마지막 값이 0이면 암호 완성이므로 종료
        for i in range(1, 6):  # 5번 돌릴 범위 설정
            if arr[0] - i <= 0:  # arr[0] 값에서 i를 뺀 값이 0보다 작거나 같으면
                arr.pop(0)  # arr[0] 값을 지우고, 
                arr.append(0)  # 0 값을 append 해준다.
                break
            else:
                arr.append(arr.pop(0) - i)  # 이외에 조건에는 arr[0]을 pop 해서 i만큼 빼준다.
    return print('#{}'.format(tc+1), *arr)  # 결과 출력


for tc in range(10):
    N = input()
    arr = list(map(int, input().split()))
    m_code()
