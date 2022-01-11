import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):

    fire_duck, pizza = map(int,input().split())
    pizza_hut = list(map(int, input().split()))
    print(pizza_hut)
    pizza_hut_shadow = []
    for i in range(pizza):
        pizza_hut_shadow.append(i)
    print(pizza_hut_shadow)

    rail = []
    dict = {}
    for i in range(pizza):
        dict[i] = pizza_hut[i]
    print(dict)
    # 숫자마다 딕셔너리로 만들어서 벨류를 빼버려야될거같은데

    # 일단 화덕의 크기만큼 숫자를 넣을거야
    # 그다음에 만약 0 있으면 빼고 그다음숫자넣어
    # 만약 화덕에 1개 남으면 그게 정답

    #레일에 처음 시작하는만큼 넣었어
    for _ in range(fire_duck):
        rail.append(pizza_hut.pop(0))
    # 반복문을 돌릴거야 피자헛에 피자가 다떨어지고
    # 레일에 마지막 피자 1개남을때까지
    # 레일에서 한개빼고 반나누고 넣을건데
    # 만약 반나눳을때 0이면? 그거 버리고 피자헛에서
    # 선입선출로 피자 한게 더가져와
    while True:
        if len(pizza_hut) == 0 and len(rail) == 1:
            pass
            break
        a = rail.pop(0)

        a = a // 2
        if a == 0 :
            if len(pizza_hut) != 0:
                rail.append(pizza_hut.pop(0))
            else:
                pass
        else:
            rail.append(a)

