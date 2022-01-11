import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    fire, num_pizza = map(int, input().split()) # 3, 5
    alpha = list(map(int, input().split()))
    chz = []
    for i in range(1, len(alpha)+1): # 뒤에 피자 번호를 붙이고싶어서!
        chz.append([alpha[i-1], i])
    # print(chz)  [[7, 1], [2, 2], [6, 3], [5, 4]] #대충 이렇게
    cooking = []
    for i in range(fire): # 화구만큼 뽑아내기!
        cooking.append(chz.pop(0))
    # print(cooking) #[[7, 1], [2, 2], [6, 3]]

    while len(cooking) > 1: # 화구가 3이니까,, 남은게 1되면 멈추자?
        a = cooking.pop(0) # 하나씩 빼내고 # a = [7, 1]
        b = a[0] // 2 # 2로 나눠서
        if b > 0:  # 0 보다 크면
            a[0] = b # 치즈양 b 로 바꿔서
            cooking.append(a)  # 그냥 다시뒤로넣어
        elif b == 0 and len(chz) > 0:  # 첫자리가 0이 되고 남은피자가잇다면
            c = chz.pop(0) # 치즈에서 남은 피자 꺼내서
            cooking.append(c)  # 피자넣어
        elif b == 0 and len(chz) == 0:  # 첫자리가 0이고 대체할 피자없다면( 요부분 생략가능)
            continue

    last = cooking.pop(0)
    fin = last[1]
    print('#{} {}'.format(tc, fin))
