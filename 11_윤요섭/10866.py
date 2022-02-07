import sys
n = int(input())
for i in range(n):
    deq = []
    c = sys.stdin.readline().split()
    if c == 'push_back':
        deq.append(c[1])
    elif c == 'push_front':
        deq.appendleft(c[1])
    elif c[0] == 'pop_front':
        if len(deq) != 0:
            print(deq[0])
            del deq[0]
        else:
            print(-1)
    elif c[0] == 'pop_back':
        if len(deq) != 0:
            print(deq[0])
            del deq[-1]
        else:
            print(-1)
    elif c[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if len(deq) != 0:
            print(deq[0])
        else:
            print(-1)
    elif c[0] == 'back':
        if len(deq) != 0:
            print(deq[-1])
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(deq))