# 미로의 거리 #
import sys; sys.stdin = open("5105_input.txt")
'''
visited 생성
큐생성, 시작점 인큐
인큐 표시
반복
    디큐
    방문해서 할일
    방문정점에 인접하고 미방문이면
        인큐
        인큐표시
'''
def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] = 2:
                return i, j
def bfs(i, j ,N):
    visited = [[0] * N for _ in range(N)]
    q = [[i, j]]
    visited[i][j] = 1
    while q:
        ti, tj = q.pop(0)
        if maze[ti][tj] == 3:
            return visited[ti][tj] - 2
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi, wj = ti,+ di, tj + dj
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj]:
                q.append([wi,wj])
                visited[wi][wj] = visited[ti][tj] + 1
    # 도착하지 못하는경우 추가하기




for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)
    print(ans)


