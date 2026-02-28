dr = [-1, 1, 0, 0] # 상, 하, 좌, 우
dc = [0, 0, -1, 1]
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 0: 빈칸, 1: 벽, 2: 우주괴물
    area = [list(map(int, input().split())) for _ in range(N)]
 
    # 우주 괴물 찾기
    for r in range(N):
        for c in range(N):
            if area[r][c] == 2:
                # 몬스터를 찾아서 4방향으로 광선 발사
                for dir in range(4):
                    nr = r + dr[dir]
                    nc = c + dc[dir]
 
                    # 벽(1)을 만나거나 맵 밖으로 나갈때까지 직진(인덱스 범위 내)
                    while 0 <= nr < N and 0 <= nc < N and area[nr][nc] != 1:
                        # 0이면 광선 표시 남기기(3)
                        if area[nr][nc] == 0:
                            area[nr][nc] = 3
 
                        # 방향을 유지한 채 다음 칸으로 직진
                        nr += dr[dir]
                        nc += dc[dir]        
 
    # 광선 발사가 끝나고 0 개수 세기
    count_zero = 0  # 0의 개수를 새로운 테스트케이스마다 초기화 해야함
    for row in area:
        for cell in row:
            if cell == 0:
                count_zero += 1
                 
                 
    print(f'#{tc} {count_zero}')``






