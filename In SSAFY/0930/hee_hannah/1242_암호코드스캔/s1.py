import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    n, m = map(int, input().split())
    codes = [list(map(str, input())) for _ in range(n)]
    total_key = []
    for i in codes:
        for j in i:
            if j != '0':
                ans = i
    #print(ans)
    #['0', '0', '0', '0', '0', '0', '0', '0', '6', '8', 'B', '4', '6', 'D', 'D', 'B', '9', '3', '4', '6', 'F', '4', '0'
                key_word = []
                for k in range(len(ans)):
                    if ans[k] != '0':
                        last_w = k
                        for a in range(last_w, len(ans)):
                            if a+3 <= len(ans)-1 and ans[a:a+3] == ['0', '0', '0']:
                                break
                            else:
                                key_word.append(ans[a])

                        break
                total_key.append(key_word)
    #print(total_key)
    fin_key = []
    for i in total_key:
        if i not in fin_key:
            fin_key.append(i)
        else:
            continue
    #print(fin_key) #[['1', 'D', 'B', '1', '7', '6', 'C', '5', '8', '8', 'D', '2', '6', 'E', 'C', '0', '0', '0']]
    last_key = []
    for i in range(len(fin_key)):
        a = ''.join(fin_key[i])
        b = a.rstrip('0')
        last_key.append(b)
    #print(last_key) #['1DB176C588D26EC'], ['196EBC5A316C578', '328D1AF6E4C9BB']
    new_word = []
    for i in last_key:
        ten = 0
        for j in range(len(i), 0, -1): # 길이가 8이고 자리가 5라면 16^3
            if i[j-1] == 'A':
                ten += 10*(16**(len(i)-j))
            elif i[j-1] == 'B':
                ten += 11*(16**(len(i)-j))
            elif i[j-1] == 'C':
                ten += 12*(16**(len(i)-j))
            elif i[j-1] == 'D':
                ten += 13*(16**(len(i)-j))
            elif i[j-1] == 'E':
                ten += 14*(16**(len(i)-j))
            elif i[j-1] == 'F':
                ten += 15*(16**(len(i)-j))
            else:
                ten += int(i[j-1])*(16**(len(i)-j))
        new_word.append(ten)
    #print(new_word)  # [133726368047113964] , [114538074621789560, 14228895786387899]
    li = []
    for i in new_word:
        lis = []
        if i < 2:
            lis.append(i)
        while i >= 2:
            i, leftover = divmod(i, 2)
            lis.append(leftover)
            if i < 2:
                lis.append(i)
                break

        new_lis = lis[::-1]
        #print(new_lis)
        li.append(new_lis)
    print(li)
    fin_fin = ''
    for i in li:
        for j in range(len(i)):
            fin_fin+=str(i[j])
    print(fin_fin)

# 내꺼 111011011000101110110110001011000100011010010011011101100
# 답 01110110110001011101101100010110001000110100100110111011