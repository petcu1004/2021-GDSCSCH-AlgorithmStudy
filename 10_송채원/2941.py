n = list(map(str, input()))

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

i, cnt = 0, 0
while True:
    if ''.join(n[i:i+2]) in croatia:
        i += 2
    elif ''.join(n[i:i+3]) in croatia:
        i += 3
    else:
        i += 1
    cnt+=1
    if i >= len(n):
        break

print(cnt)