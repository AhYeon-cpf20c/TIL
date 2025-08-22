# Tree (1/2) : 휘람이의 크리스마스 트리 #

import sys
sys.stdin = open("21911_input.txt")

def dfs(node):
    if node == -1:
        return
    # print(node, end=' ')  # V L R (전위 순회)
    preorder.append(node)
    dfs(graph[node][0]) # 왼쪽 자식으로 이동
    # print(node, end=' ') # L V R (중위 순회)
    inorder.append(node)
    dfs(graph[node][1]) # 오른쪽 자식으로 이동
    postorder.append(node)
    # print(node, end=' ') # L R V (후위 순회)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [[] for _ in range(N+1)]

    for _ in range(N):
        s, e1, e2 = map(int, input().split())
        graph[s].append(e1)
        graph[s].append(e2)

    preorder = []
    inorder = []
    postorder = []
    dfs(1)

    print(f'#{tc}')
    print(*inorder)
    print(*preorder)
    print(*postorder)