while True:
    lengths = list(map(int, input().split()))
    if not sum(lengths):
        break
    longest = lengths.pop(lengths.index(max(lengths)))
    if longest ** 2 == lengths[0] ** 2 + lengths[1] ** 2:
        print("right")
    else:
        print("wrong")