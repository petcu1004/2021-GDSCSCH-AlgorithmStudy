A = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
l = []


def D(s):
    for i in range(len(s)):
        for j in range(len(A)):
            if s[i] in A[j]:
                l.append(j + 3)


D(input())
print(sum(l))