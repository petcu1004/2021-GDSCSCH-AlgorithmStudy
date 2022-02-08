import sys
t = int(sys.stdin.readline())
for i in range(t):  #테스트 케이스 개수
    n = int(sys.stdin.readline())  #전화번호 수
    nlist = []
    for j in range(n):
        call_num = (sys.stdin.readline())
        nlist.append(call_num)
        answer = 'YES'
        if j != 0:
            ch_num = nlist[j]
            # print(ch_num)
            for k in range(j):
                if len(ch_num) > len(nlist[k]):
                    # print(nlist[k])
                    # print(ch_num[:len(nlist[k]) - 1])
                    if int(ch_num[:len(nlist[k]) - 1]) == int(nlist[k]):
                        answer = 'NO'
                        break
    print(answer)
