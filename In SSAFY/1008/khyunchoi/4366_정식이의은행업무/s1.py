import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    binary_num = input()
    ternary_num = input()

    guess_binary_list = []
    for i in range(1, len(binary_num)):
        guess_binary_list.append(binary_num[:i] + str(int(binary_num[i]) ^ 1) + binary_num[i+1:])

    guess_ternary_list = []
    if ternary_num[0] == '1':
        guess_ternary_list.append('2' + ternary_num[1:])
    else:
        guess_ternary_list.append('1' + ternary_num[1:])

    for i in range(1, len(ternary_num)):
        if ternary_num[i] == '0':
            guess_ternary_list.append(ternary_num[:i] + '1' + ternary_num[i+1:])
            guess_ternary_list.append(ternary_num[:i] + '2' + ternary_num[i+1:])
        elif ternary_num[i] == '1':
            guess_ternary_list.append(ternary_num[:i] + '0' + ternary_num[i+1:])
            guess_ternary_list.append(ternary_num[:i] + '2' + ternary_num[i+1:])
        else:
            guess_ternary_list.append(ternary_num[:i] + '0' + ternary_num[i + 1:])
            guess_ternary_list.append(ternary_num[:i] + '1' + ternary_num[i + 1:])

    dec_guess_ternary_list = []
    for num in guess_ternary_list:
        dec_guess_ternary_list.append(int(num, 3))

    for num in guess_binary_list:
        if int(num, 2) in dec_guess_ternary_list:
            result = int(num, 2)

    print('#{} {}'.format(tc, result))