#히스토그램에서 가장 넓이가 큰 직사각형의 넓이
while True:
    temp = list(map(int, input().split()))
    n = temp[0]
    if n == 0:
        break
    height = temp[1:]

    height.insert(0, 0)
    height.append(0)

    check = [0]
    area = 0

    for i in range(1, n+2):
        while check and height[i] < height[check[-1]]:

            idx = check.pop()

            area = max(area, (i-1-check[-1])*height[idx])

        check.append(i)

    print(area)