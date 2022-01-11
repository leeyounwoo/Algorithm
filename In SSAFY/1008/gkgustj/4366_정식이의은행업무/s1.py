import sys
sys.stdin = open('input.txt')

def bin_to_3(bin_list):
    # 10진수 변환
    dec_num = 0
    for i in range(len(bin_list)):
        dec_num += int(bin_list[i]) * 2**(len(bin_list)-1-i)
    
    answer = dec_num

    # 3진수 변환
    num3 = []
    while dec_num:
        num3.append(dec_num%3)
        dec_num //= 3

    num3 = num3[::-1]
    
    # 3진수와 비교
    if len(num3) != len(cash_3):
        return 0

    cnt = 0
    for j in range(len(num3)):
        if num3[j] != int(cash_3[j]):
            cnt += 1
        
        if cnt > 1:
            return 0
    
    if cnt == 1:
        return answer
    
    return 0


T = int(input())

for t in range(1, T+1):
    cash_2 = list(input())
    cash_3 = list(input())

    for i in range(1, len(cash_2)):
        if cash_2[i] == '0':
            cash_2[i] = 1
            temp = bin_to_3(cash_2)
            cash_2[i] = 0
        else:
            cash_2[i] = 0
            temp = bin_to_3(cash_2)
            cash_2[i] = 1
        
        if temp:
            break
    
    print('#{} {}'.format(t, temp))        