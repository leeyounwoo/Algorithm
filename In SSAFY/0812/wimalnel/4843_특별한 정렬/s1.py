import sys
# input.txt 파일에서 입력값 불러오는 코드
sys.stdin = open('input.txt')

T = int(input())
for Tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))  # 정수 ai가 주어진다. 10<=N <= 100, 1<= ai <=100
    max_sorting = sorted(ai, reverse=True) # 역순정렬
    min_sorting = sorted(ai) #오름차순 정렬
    result = list()
    i = 0
    while i != len(ai):
        result.append(max_sorting[i])  # 큰 수 넣은 후 작은 수 넣기
        result.append(min_sorting[i])
        i += 1
    print('#%d' % Tc, end=' ')

    for i in result[:10]:  # 최대 10개만 출력
        print(i, end=' ')
    print()

