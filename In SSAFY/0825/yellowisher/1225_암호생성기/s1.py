import sys
from collections import deque
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    pwd = list(map(int, input().split()))
    queue = deque(pwd) # 입력된 list를 queue 자료구조로 변환

    i = 0 # 1~5까지 순회하면서 빼주기 위한 변수
    while True:
        i += 1
        num = queue.popleft() # 맨 왼쪽 값을 뺀다.
        if (num - i) <=0: # 맨 왼쪽 값에서 i를 뺀 값이 0보다 작거나 같으면 0을 끝에다 더해줌
            queue.append(0)
            break
        else:
            queue.append(num - i) # 0 이상이라면 num - i를 끝에다 더해줌
        if i == 5: # 1~5 반복
            i = i % 5

    print("#{}".format(tc), end = " ")
    for i in queue:
        print(i, end = " ")
    print()
