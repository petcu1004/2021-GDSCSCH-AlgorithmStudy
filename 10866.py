import sys

def push_front(x) :
    deque.insert(0, x)

def push_back(x) :
    deque.append(x)

def pop_front() :
    if deque :
        return deque.pop(0)
    else :
        return -1

def pop_back() :
    if deque :
        return deque.pop()
    else :
        return -1

def size() :
    return len(deque)

def empty() :
    if deque :
        return 0
    else :
        return 1

def front() :
    if deque :
        return deque[0]
    else :
        return -1

def back() :
    if deque :
        return deque[-1]
    else :
        return -1

N = int(sys.stdin.readline())
deque = []

for _ in range(N) :
    order = sys.stdin.readline().rstrip().split()
    if order[0] == 'push_front' :
        push_front(order[1])
    elif order[0] == 'push_back' :
        push_back(order[1])
    elif order[0] == 'pop_front' :
        print(pop_front())
    elif order[0] ==  'pop_back' :
        print(pop_back())
    elif order[0] == 'size' :
        print(size())
    elif order[0] == 'empty' :
        print(empty())
    elif order[0] == 'front' :
        print(front())
    elif order[0] == 'back' :
        print(back())