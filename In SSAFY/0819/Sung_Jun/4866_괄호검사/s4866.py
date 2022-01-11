import sys
sys.stdin = open('input.txt')


def pra_test(test_str):
    result_list = []
    for test in test_str:
        if test in ['(', ')', '{', '}']:
            if test == '(' or test == '{':
                result_list.append(test)
            else:
                if len(result_list) != 0:
                    check = result_list.pop()
                    if check + test not in ['()', '{}']:
                        return 0
                else:
                    return 0
    if len(result_list) != 0:
        return 0
    else:
        return 1


T = int(input())
for tc in range(T):
    test_str = input()
    print('#{} {}'.format(tc+1, pra_test(test_str)))
