# 같은 행열이 아닐 것
# 대각선이 아닐 것
# 델타 -> 우주괴물

# 변수
# N = int(input())
# visited > visited = [[0]*N for _ in range(N)]

dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

N = int(input())
visited = [[0]*N for _ in range(N)]
count = 0

def dfs(r, c):
    global count
    visited[r][c] = 1
    count += 1 # 문제?
    # 리턴어디서?

    for dir in range(8):
        nr = r + dr[dir]
        nc = c + dc[dir]

        while 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            nr =+ dr[dir]
            nc =+ dc[dir]

            dfs(nr, nc) #문제?
            # visited[r][c] = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j) 

print(count)
