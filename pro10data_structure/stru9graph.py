# Graph : node와 edge의 집합으로 이루어진 자료구조
# Tree : 계층구조, root(있음), 사이클 없음, 항상 연결

#Graph : 일반 네트워크 구조, root없음, 사이클(순환)있음, 연결/비연결

graph = {
    'A':('B', 'C'),
    'B':('D', 'E'),
    'C':('F', 'G'),
    'D':('H', 'I'),
    'H':(),
    'I':(),
    'E':(),
    'F':(),
    'G':(),
}

# DFS - 깊이 우선 탐색 방식 - 재귀함수 또는 스택으로 구현, 경로추적
def dfsFunc(graph, start, visited):
    visited_dfs.append(start)
    for next_node in graph[start]:
        if next_node not in visited:
            dfsFunc(graph, next_node, visited)

visited_dfs = []    # 방문 순서 저장용
dfsFunc(graph, 'A', visited_dfs)
print('DFS 방문 순서 : ', visited_dfs)
# DFS 방문 순서 :  ['A', 'B', 'D', 'H', 'I', 'E', 'C', 'F', 'G']

# BFS - 너비 우선 탐색 방식 - 큐로 구현
from collections import deque
def bfsFunc(graph, start):
    visited = [start]
    queue = deque([start])  # queue 사용(FIFO)

    while queue:
        node = queue.popleft()  # 가장 먼저 들어온 node 꺼냄
        for next_node in graph[node]:   # 현재 노드와 이웃 노드 확인
            if next_node not in visited:
                visited.append(next_node)   # 방문 처리
                queue.append(next_node) # 다음 탐색 대상으로 queue에 추가
    return visited

visited_bfs = bfsFunc(graph, 'A')    # 방문 순서
print('BFS 방문 순서 : ', visited_bfs)
# BFS 방문 순서 :  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
# 방문 즉시 queue에 쌓고 먼저 들어온 것부터 처리(거리<레벨> 개념이 생김)
