import sys

sys.stdin = open('input.txt')
n = int(input())
ans = set()
for _ in range(n):
    command = sys.stdin.readline()
    if command[:2] == 'ad':
        ans.add(list(command.split())[1])
    elif command[:2] == 're':
        if list(command.split())[1] in ans:
            ans.remove(list(command.split())[1])
    elif command[:2] == 'ch':
        if list(command.split())[1] in ans:
            print(1)
        else:
            print(0)
    elif command[:2] == 'to':
        if list(command.split())[1] in ans:
            ans.remove(list(command.split())[1])
        else:
            ans.add(list(command.split())[1])
    elif command[:2] == 'al':
        ans = set(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
             '20'])
    elif command[:2] == 'em':
        ans.clear()


