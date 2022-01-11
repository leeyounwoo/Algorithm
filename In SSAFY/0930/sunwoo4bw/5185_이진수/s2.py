import sys
sys.stdin = open("input.txt")

# hex -> dec -> bi
T = int(input())
for tc in range(1, T+1):
    N, hexadec = input().split()

    nums = []
    for i in hexadec: # 47FE
        if i == 'A':
            nums.append(10)
        elif i == 'B':
            nums.append(11)
        elif i == 'C':
            nums.append(12)
        elif i == 'D':
            nums.append(13)
        elif i == 'E':
            nums.append(14)
        elif i == 'F':
            nums.append(15)
        else:
            nums.append(int(i))
    #print(nums) # [4, 7, 15, 14]

    binary = []
    for n in nums:
        tmp = []
        if n < 2:
            tmp.append(n)
        while n >= 2:
            #r = n%2
            n, r = divmod(n, 2)
            tmp.append(r)
            if n < 2:
                tmp.append(n)
                break
        #tmp = [0, 0, 1]
        if not len(tmp) == 4:
            for _ in range(4-len(tmp)):
                binary.append(0)

            for i in range(len(tmp)-1, -1, -1): # 최종binary에 tmp 넣는 과정
                binary.append(tmp[i])
        else:
            for i in range(len(tmp)-1, -1, -1):
                binary.append(tmp[i])
    # print(binary) # [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    final = ''
    for n in binary:
        final += str(n)

    print('#{} {}'.format(tc, final))
