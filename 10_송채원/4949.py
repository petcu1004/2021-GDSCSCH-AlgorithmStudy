while 1:
    s = input()
    if s == '.':
        break
    stack = []
    ok = 1
    for c in s:
        if c in '([':
            stack.append(c)
        elif c in ')':
            if stack == [] or stack[-1] != '(':
                ok = 0
                break
            else:
                stack.pop()
        elif c in ']':
            if stack == [] or stack[-1] != '[':
                ok = 0
                break
            else:
                stack.pop()
    print("yes" if ok and stack == [] else "no")