import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    buildings = list(map(int, input().split()))

    result = 0
    for i in range(2, T-2): # bulidings 안의 요소 중 맨 앞 2개와 맨 뒤 2개가 0,0 이므로 2부터 T-2까지 범위 설정
        tmp = buildings[i-2:i] + buildings[i+1:i+3] # i를 중심으로 앞뒤 2개의 요소를 합한 임시 리스트
        for j in range(len(tmp)-1): # 임시 리스트를 버블정렬
            if tmp[j] > tmp[j+1]:
                tmp[j], tmp[j+1] = tmp[j+1], tmp[j]
        if buildings[i] > tmp[-1]: # i의 값이 임시 리스트의 가장 큰 값보다 크다면
            difference = (buildings[i] - tmp[-1]) # 그 차이를 구함
            result += difference # result에 더해줌

    print('#{0} {1}'.format(tc, result))




