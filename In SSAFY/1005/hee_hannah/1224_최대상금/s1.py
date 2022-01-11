import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    num, change = map(int, input().split())
    num = str(num) # 문자열로 받아서
    li = [] # 넣어주기
    for i in num:
        li.append(i)

    sorted_li = sorted(li, reverse=True) # 내림차순 정렬( 원하는 이상적인 표본 모양 )
    # lis = li[:]
    #print(sorted_li) # ['3', '2', '1'] ['7', '7', '3', '2'] ['8', '8', '8', '3', '2']
    for i in range(len(li)):

        if li[i] != sorted_li[i] and change != 0: # 표본과 같지 않고 바꿀 기회가 남아있다면
            locate = num.rfind(sorted_li[i]) # 32888 4 3 원하는 표본의 수가 num 의 몇번째인지(li의 위치)알아내기
            # 이때 왼쪽부터 찾아야 원하는 위치랑 바꿀 수 잇음(더 크게)
            num1 = num[::-1] # replace 쓰기 위해 순서 뒤집기
            num1 = num1.replace(sorted_li[i], '0', 1) # 바꿀 애 0으로 만들고
            num = num1[::-1] # 다시 원위치
            #print(num)
            li[i], li[locate] = li[locate], li[i] # 자리 바꿔주기
            change -= 1 # 카운트 줄이기
        elif li[i] == sorted_li[i] and change != 0: # 만약 같다면
            if i == len(li): # 끝자리까지 왓는데도 동일하다면
                change = 0 # 체인지 0만들고 끝내기
                break
            else:
                continue
        if change == 0:
            break

    #print(li) # 맥스순서대로 놓고 첫번째 맥스를 맨앞이랑 바꾸고 두번째 자리는 두번째 맥스랑 바꾸고,,
    total = ''
    for i in li:
        total += str(i)
    print(total) # 82883

'''
#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645
'''