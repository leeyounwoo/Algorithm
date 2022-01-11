import sys
sys.stdin = open('0930/woosteelz/1242_암호코드스캔/sample_input.txt')

# hex_str = '0328D1AF6E4C9BB'
# print((bin(int(hex_str, 16))[2:]))

for tc in range(int(input())):
    n, m = map(int, input().split())
    codes = []
    for _ in range(n):
        string = input()
        string = bin(int(string, 2))[2:]
        if '1' in string:
            temp = ''
            idx = 0
            string = string[::-1]
            while idx < m:
                if string[idx] == 1:
                    pass
