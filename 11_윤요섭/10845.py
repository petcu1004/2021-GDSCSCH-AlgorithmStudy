n = int(input())
nlist = []
for i in range(n):
    c = input()
    if c[:4] == 'push':
        num = int(c[-1])
        nlist.append(num)
    elif c == 'pop':
        if len(nlist) != 0:
            print(nlist[0])
            del nlist[0]
        else:
            print(-1)
    elif c == 'empty':
        if len(nlist) != 0:
            print(0)
        else:
            print(1)
    elif c == 'front':
        if len(nlist) != 0:
            print(nlist[0])
        else:
            print(-1)
    elif c == 'back':
        if len(nlist) != 0:
            print(nlist[-1])
        else:
            print(-1)
    elif c == 'size':
        print(len(nlist))