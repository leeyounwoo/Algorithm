while True:
    word = input()
    if word == '0':
        break
    length = len(word)
    for i in range(length//2):
        if word[i] != word[length-1-i]:
            print("no")
            break
    else:
        print("yes")