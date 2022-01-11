import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    test_str = input()

    result = []
    for test in test_str:
        if result == []:
            result.append(test)
        else:
            if result[-1] == test:
                result.pop()
                continue
            else:
                result.append(test)
    print('#{} {}'.format(tc+1, len(result)))
