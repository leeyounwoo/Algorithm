import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    n, word = map(str, input().split()) # 일단 문자열로 받기
    n = int(n)
    new_word = []

    for i in range(n): #a b c d e f
        if word[i] == 'A': # 각 자리의 수가 문자라면
            new_word.append(10) #숫자로 바꾸고
        elif word[i] == 'B':
            new_word.append(11)
        elif word[i] == 'C':
            new_word.append(12)
        elif word[i] == 'D':
            new_word.append(13)
        elif word[i] == 'E':
            new_word.append(14)
        elif word[i] == 'F':
            new_word.append(15)
        else: # 숫자라면
            new_word.append(int(word[i])) # 숫자로 변환하여 넣어줍니다
    #print(new_word) #[4, 7, 15, 14] = 1 0 0  1 1 1
    li = []
    for j in new_word: #새로 바꾼 숫자리스트에서 하나씩 빼서
        lis = []
        if j < 2: # 만약 0, 1이라면 그대로 새 리스트에 넣고
            lis.append(j)
        while j >= 2: #아니라면 나눠줍니다
            j, leftover = divmod(j, 2)
            lis.append(leftover) #나머지를 넣고
            if j < 2: # 2 미만이 된 몫도 넣어주기
                lis.append(j)
                break
        #print(lis) #[0, 0, 1] 이걸 [0,1,0,0,]으로!
        if len(lis) != 4: # 리스트의 길이가 4가 안된다면 4자리를 만들기 위해
            for k in range(4-len(lis)):
                li.append(0) # 앞에 0을 넣어줌
            for f in range(len(lis)-1, -1, -1):
                li.append(lis[f]) # 역순을 제대로 바꿔주기
        else: #4자리가 맞다면
            for f in range(len(lis)-1, -1, -1): # 순서만 바꿔주기
                li.append(lis[f])
    fin = ''
    for a in li: # 최종적으로 한 덩어리로 만들어주기
        fin += str(a)
    print(fin)

