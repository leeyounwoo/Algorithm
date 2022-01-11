'''
입력)
0000000111100000011000000111100110000110000111100111100111111001100111

출력)
0,120,12,7,76,24,60,121,124,103
'''

'''
K = list(input())
for i in range(10):
    result = 0
    for j in range(1, 8):
        result += (1 << (7 - j)) * int(K.pop(0))
    N = len(K)
    if N:
        print(result, end=",")
    else:
        print(result)
'''

num = '0000000111100000011000000111100110000110000111100111100111111001100111'

for i in range(0, len(num) - 7 + 1, 7):
    bin = num[i:i+7]

    total = 0
    for j in range(len(bin)-1, -1, -1):
        if bin[j] == '1':
            total += 2 ** (len(bin) - 1 -j)
    print(total, end=" ")
