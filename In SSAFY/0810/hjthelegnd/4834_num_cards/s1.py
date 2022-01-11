import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    cards = list(input()) # 리스트로 입력, 인트로 받을 필요 없음
    result = {}
    count = 0

    for _ in range(n):
        popped = cards[-1+count] # pop()함수를 구현하기 위해 위에 count 변수 선언

        if popped in result: # 만약 없다면 1로 생성하고 있다면 += 1
            result[popped] += 1
        else:
            result[popped] = 1
        count -= 1 # pop함수 구현, 마지막 리스트 원소는 사라졌다고 가정
        tmp = 0 # idx 초기숫자(카드 숫자는 음수로 들어오지 않는다)
        answer = 0 # value 초기숫자

    for idx, values in result.items():
        if tmp < values: # 만약 value가 더 크다면 (갯수가 더 크다면)
            tmp = values
            answer = idx
        elif tmp == values: # 만약 value가 같다면(갯수가 같다면) idx를 더 큰걸로!
            tmp = values
            if idx > answer:
                answer = idx

    print('#{0} {1} {2}'.format(tc, answer, tmp))