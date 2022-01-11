import sys

sys.stdin = open('input.txt')
for T in range(1, int(input()) + 1):
    # () ((( () () ) ( () ) () ))( ())
    pipe = input()
    ans = 0
    pipe_count = 0
    razer_flag = False

    for i in range(len(pipe)):
        if pipe[i] == '(':
            if pipe[i + 1] == ')':
                razer_flag = True
            else:
                pipe_count += 1

        else:
            if razer_flag:
                ans += pipe_count
                razer_flag = False
            else:
                pipe_count -= 1
                ans += 1
    print('#{} {}'.format(T, ans))