N, M, R = map(int, input().split())
# N개 만큼 배열을 만들어야 한다.
arr = [list(map(int, input().split())) for _ in range(N)]
# 처음 값만 temp에 넣어주고 비어있는 곳헤 하나하나 돌리면 된다
# 제한 부분을 보면 min(N, M) mod 2 = 0이 있는데 만약 3X4 형태일 때 중간 부분을 해결하기 위함이다.