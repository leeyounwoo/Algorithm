import sys
sys.stdin = open('1005/woosteelz/4336_은행/sample_input.txt')

b_dict = {
    '0': '1',
    '1': '0'
}

for tc in range(int(input())):
    two = list(input())
    three = list(input())
    ans = ''
    print(two)
    for i in range(len(two)):
        two[i] = b_dict[two[i]]
        print(two)
        for n in range(len(three)):
            temp = three[n]
            for m in range(3):
                if not temp == str(m):
                    three[n] = str(m)
                    if int(''.join(two), 2) == int(''.join(three), 3):
                        ans = int(''.join(two), 2)
                    three[n] = temp
                if ans:
                    break
            if ans:
                break
        if ans:
            break
        two[i] = b_dict[two[i]]
    print(f'#{tc+1} {ans}')
