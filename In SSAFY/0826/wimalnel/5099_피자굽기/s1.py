import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split()) # N개 피자를 동시에 굽는 화덕, M개의 피자 굽기
    cheese = list(map(int, input().split())) # 치즈량(C//2)

      # ex) 3, 5 3개를 동시에굽는 화덕에 5개의 피자를 구워보기
    pizza = [i for i in range(M)] # 피자 배열 생성

    Q = pizza[:N]       # 피자넣는 화덕 큐 생성 (삭제,삽입)

    while len(Q) != 1: # 큐에 남는것이 한개가 될때까지 반복쓰
        if cheese[Q[0]] != 1:
            cheese[Q[0]] = cheese[Q[0]] // 2  # 한바꾸 돌면 치즈량 반으로 줄어든다!
            Q.append(Q.pop(0)) # 맨 앞의 화덕피자를 꺼내 맨뒤로 보내는 작업

        else: # 치즈량이 1일때는 //2하면 0.5라서 0임 -> 바로 교체
            Q.pop(0)  # 첫번째 화덕 꺼내서
            if N != M: # M개를 구워야하니깐!
                Q.append(pizza[N]) # 첫번째 화덕에서 꺼낸걸 뒤로 넣어주는 작업
                N += 1 # 다음순서 진행

    pizza_num = Q[0] + 1             # 0번지 시작이라 피자번호 +1번
    print('#{} {}'.format(tc, pizza_num))