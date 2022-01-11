import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):

    fire_duck, pizza = map(int,input().split()) # 화_덕의 크기와 과 피자의 갯수
    pizza_hut = list(map(int, input().split())) # 이건 피자들!
    pizza_hut_shadow = [] # 이건 피자의 인덱스
    for i in range(pizza):
        pizza_hut_shadow.append(i)
    rail = [] # 피자를 구울 레일
    dict = {}
    for i in range(pizza):
        dict[i] = pizza_hut[i]
    print(dict)
    # 숫자마다 딕셔너리로 만들어서 벨류를 빼버려야될거같은데

    # 일단 화덕의 크기만큼 숫자를 넣을거야
    # 그다음에 만약 0 있으면 인덱스값을 빼고  그다음숫자넣어
    # 만약 화덕에 1개 남으면 그게 정답!

    #레일에 처음 시작하는만큼 넣었어 (피자헛쉐도우(피자헛의인덱스값) 0 ,1 ,2 들어감)
    for _ in range(fire_duck):
        rail.append(pizza_hut_shadow.pop(0))
    # 반복문을 돌릴거야 피자헛에 피자가 다떨어지고
    # 레일에 마지막 피자 1개남을때까지
    # 레일에서 한개빼고 반나누고 넣을건데
    # 만약 반나눳을때 0이면? 그거 버리고 피자헛에서
    # 선입선출로 피자 한게 더가져와

    # 무한대로 돌릴거야
    while True:
        # 1번피자 를 a에넣어
        a = rail.pop(0)
        # a 치즈양 반으로 녹인다!
        dict[a] = dict[a] // 2
        # 혹시 레일에 남은 피자가 없니?
        if len(rail) == 0:
            # 장사 망함 ㅈㅈ 마지막남은 피자발표
            print('#{} {}'.format(tc,a+1))
            break
        # 혹시 a번 피자 치즈가 없어졌니?
        if dict[a] == 0:
            # 치즈도 없는데 더넣을 피자가있어?!
            if len(pizza_hut_shadow) != 0:
                #   그럼 레일에 (피자헛 인덱스값의)피자 이렇게 넣어!
                rail.append(pizza_hut_shadow.pop(0))
            else:
                pass
            # 치즈 다안녹았으면 다시 a번피자 레일에넣어~
        else:
            rail.append(a)


