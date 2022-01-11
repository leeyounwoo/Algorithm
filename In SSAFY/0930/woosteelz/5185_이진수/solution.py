import sys
sys.stdin = open('0930/woosteelz/5185_이진수/input.txt')

TC = int(input())
for tc in range(1, TC + 1):
    N, hex_string = map(str, input().split())
    ans = bin(int(hex_string, 16))[2:]
    ans = '0' * (4 * len(hex_string) - len(ans)) + ans
    print(f"#{tc} {ans}")
