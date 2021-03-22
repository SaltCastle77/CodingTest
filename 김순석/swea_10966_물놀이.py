from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    pool = []
    arr =[[0] * M for _ in range(N)]
    ans = 0
    water = deque()
    for i in range(N):
        pool.append(input())
        for j in range(M):
            if pool[i][j] == 'W':

                water.append((i, j))

    while water:
        x, y = water.popleft()
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if tx < 0 or tx >= N or ty < 0 or ty >= M or pool[tx][ty] == 'W':
                continue

            if arr[tx][ty] == 0 and pool[tx][ty] == 'L':
                arr[tx][ty] = arr[x][y] + 1
                ans += arr[tx][ty]
                water.append((tx, ty))

    print('#{} {}'.format(t, ans))