import sys
sys.stdin = open('input.txt')

for T in range(10):
    len_testcase = int(input())
    arr = list(map(int, input().split()))
    result = 0
    # 앞의 2번째와 뒤의 2번째 값은 계산할 필요가 없으므로 제외
    for i in range(2, len_testcase-2):
        # 앞에서 2번째, 뒤에서 2번째 값들이 모두 비교하고자 하는 값보다 작으면 조망권 존재
        if arr[i-2] < arr[i] and arr[i-1] < arr[i] and arr[i+1] < arr[i] and arr[i+2] < arr[i]:
            # 비교하고자 하는 값에서 앞에서 2번째, 뒤에서 2번째 값들 중 가장 큰 값을 빼주면 조망권 수가 됨
            result += arr[i] - max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
    # print('#{} {}'.format(T+1, result))
    print('#%d %d'%(T+1, result))