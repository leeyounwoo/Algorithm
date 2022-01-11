import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    book = list(map(int, input().split()))
    # book = [400, 300, 350] [1000, 299, 578] [1000, 222, 888] 로나옴
    #         전체  A찾  B찾
    A = 0
    B = 0
    center = int((1 + book[0]) / 2)
    left = 1
    right = book[0]

    # 자 이제 내 말 들을때 까지 무한대로 괴롭힐거야.
    while True:
        # 만약 A가 찾는게 센터보다 크면? 센터값을 오른쪽으로 조정하고
        # A는 1번시도했다! 체크해주는거 잊지마시고
        if book[1] > center:
            left = center
            center = int((center+right) / 2)
            A = A + 1
        # 만약 A 가 찾는게 지금 센터랑 같다? 멈춰!
        elif book[1] == center:
            break
        # 만약 A 가 찾는게 센터보다 작아? 그럼 센터값을 왼쪽으로조정
        elif book[1] < center:
            right = center
            center = int((left+center) / 2)
            A = A + 1


    center = int((1 + book[0]) / 2)
    left = 1
    right = book[0]

    while True:
        # 만약 B가 찾는게 센터보다 크면? 센터값을 오른쪽으로 조정하고
        # B는 1번시도했다! 체크해주는거 잊지마시고
        if book[2] > center:
            left = center
            center = int((center + right) / 2)
            B = B + 1
        # 만약 B 가 찾는게 지금 센터랑 같다? 멈춰!
        elif book[2] == center:
            break
        # 만약 B 가 찾는게 센터보다 작아? 그럼 센터값을 왼쪽으로조정
        elif book[2] < center:
            right = center
            center = int((left + center) / 2)
            B = B + 1


    if A > B:
        print('#{} B'.format(test_case))
    elif A < B:
        print('#{} A'.format(test_case))
    else:
        print('#{} 0'.format(test_case))