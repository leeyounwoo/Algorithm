import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    command = input()
    
    steel = 0      # 겹쳐 놓인 쇠막대기의 개수
    my_steel = 0   # 잘려나간 쇠막대기 조각의 개수

    for i in range(len(command)):
        if command[i] == '(':
            # 바로 뒤에 )가 오면 레이저 -> 겹쳐진 쇠막대기 수만큼 조각이 생김
            if command[i+1] == ')':
                my_steel += steel
                
            # 그게 아니라면 새로운 쇠막대기가 겹쳐진 것
            else:
                steel += 1
                
        elif command[i] == ')':
            # 바로 앞이 (이면 레이저 -> (일때 이미 처리했으므로 pass
            if command[i-1] == '(':
                pass
            
            # 그게 아니라면 쇠막대기의 길이가 끝난 것
            else:
                steel -= 1
                my_steel += 1

    print('#{} {}'.format(t, my_steel))