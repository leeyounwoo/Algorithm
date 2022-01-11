import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    temp, cnt = map(int, input().split())

    numbers = []
    flag = False
    for num in str(temp):
        tmp = int(num)

        if not flag:
            if tmp in numbers:
                flag = True

        numbers.append(tmp)

    n = len(numbers)

    # 내림차순 정렬
    i = 0
    while cnt and i < n:
        after_max = 0
        for j in range(i+1, n):
            # 뒤 쪽에 있는 큰 값을 가져와야하므로 등호포함
            if numbers[j] >= after_max:
                after_max = numbers[j]
                max_idx = j

        if numbers[i] < after_max:
            numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]
            cnt -= 1

        i += 1

    # 카운트가 아직 남아있는 경우
    # 1. 중복된 숫자가 존재한다면 그것만 계속 바꿔주면 됨 (777770)
    if flag:
        pass
    # 2. 중복된 숫자가 없으면 짝수횟수는 그냥 아무 쌍이나 반복해서 바꾸기
    #                         홀수횟수는 맨 마지막 두 개만 바꾸기
    elif cnt%2:
        numbers[n-1], numbers[n-2] = numbers[n-2], numbers[n-1]
    
    answer = ''
    for number in numbers:
        answer += str(number)
    
    print('#{} {}'.format(t, answer))

# 88823에서 실패