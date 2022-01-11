import sys
sys.stdin = open('input.txt')

dict_16_to_10 = {
    '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
    '6': '0110', '7': '0111', '8': '1000', '9': '1001', '0': '0000',
    'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}
for T in range(1, 1+int(input())):
    N, num_16 = map(str, input().split())
    N = int(N)
    ans = ''
    for num in num_16:
        ans += dict_16_to_10[num]
    print('#{} {}'.format(T, ans))
