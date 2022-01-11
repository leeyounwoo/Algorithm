import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(TC):
    string = list(str(input()))
    temp = []
    result = False

    for s in string:
        if s == "{" or s == "(":
            temp.append(s)

        elif s == "}" or s == ")":
            if temp:
                if s == "}" and temp[-1] == "{":
                    temp.pop(-1)
                elif s == ")" and temp[-1] == "(":
                    temp.pop(-1)
                else:
                    result = True
                    break
            else:
                result = True
                break

    if result:
        print(f"#{tc+1} 0")
    else:
        if temp:
            print(f"#{tc+1} 0")
        else:
            print(f"#{tc+1} 1")