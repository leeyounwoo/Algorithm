for T in range(int(input())):
    floor = int(input())
    address = int(input())
    prev_floor = []
    for i in range(1, address+1):
        prev_floor.append(i)
    # print(prev_floor)
    for i in range(floor):
        now = []
        for j in range(address):
            now.append(sum(prev_floor[:j+1]))
        prev_floor = now[:]
    print(now[address-1])
