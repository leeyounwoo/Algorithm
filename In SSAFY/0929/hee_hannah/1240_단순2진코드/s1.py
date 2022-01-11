import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    n, m = map(int, input().split())
    li = [list(map(str, input())) for _ in range(n)]
    # 인풋값들을 받아 줍니다
    for i in range(len(li)): # 줄마다
        if '1' in li[i]: # 만약 0으로만 이루어져있지 않다면
            num = li[i] # 원하는 줄을 찾앗으니 브레이크를 건다.
            break
    # 0000011101101100010111011011000101100010001101001001101110110000000000
    for j in range(len(num)-1, -1, -1): #10 -> 0~9 -> 9~-1
        if num[j] == '1': # 5  # 순서를 뒤집어서 만약 끝자리가 1이라면
            a = j # 끝자리의 자리수를 알아냅니다
            break
    # print(a) # 59 니까 56
    fin = [] #
    for k in range(a-55, a+1, 7): # 56개의 자리수로 이루어져있기 떄문에 이렇게 범위를 잡고
        # 53~59 -> 53~60 -> 53 46 39 32 25 18 11 4
        fin.append(num[k:k+7]) # 3~9 #각 7개씩 슬라이스 해서 넣어줍니다
    #print(fin)
    last = []
    for c in range(len(fin)):
        last.append(''.join(map(str, fin[c]))) #한덩어리로 만들어줍니다
    # print(last)
    # ['0011101', '1011000', '1011101', '1011000', '1011000', '1000110', '1001001', '1011101', '1000000']
    #print(len(last))
    number = []
    for z in range(len(last)): # 만약 덩어리들이 아래 조건과 매칭된다면 숫자로 바꿔줍니다
        if last[z] == '0001101':
            number.append('0')
        elif last[z] == '0011001':
            number.append('1')
        elif last[z] == '0010011':
            number.append('2')
        elif last[z] == '0111101':
            number.append('3')
        elif last[z] == '0100011':
            number.append('4')
        elif last[z] == '0110001':
            number.append('5')
        elif last[z] == '0101111':
            number.append('6')
        elif last[z] == '0111011':
            number.append('7')
        elif last[z] == '0110111':
            number.append('8')
        elif last[z] == '0001011':
            number.append('9')
    # print(number) #['7', '5', '7', '5', '5', '0', '2', '7']
    total = 0
    for i in range(1, 9): # 0~7 1~8
        if i % 2: # 홀수라면 number
            total += int(number[i-1])*3
        else: # 짝수라면
            total += int(number[i-1])
    fin_fin = 0
    if total % 10 == 0: # 10의 배수라면 올바른 키 이기 때문에
        for v in number:
            fin_fin += int(v)
        print(fin_fin) # 각 자리수의 합을 구해줍니다
    else:
        print('0') # 잘못된 키
