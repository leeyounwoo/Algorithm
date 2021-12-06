x = int(input())
y = int(input())

flag_x = False
flag_y = False
if x > 0:
    flag_x = True
if y > 0:
    flag_y = True

if flag_x and flag_y:
    print(1)
elif flag_x and not flag_y:
    print(4)
elif not flag_x and flag_y:
    print(2)
else:
    print(3)