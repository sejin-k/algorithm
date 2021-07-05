# input 입력
n, m, v = map(int, input().split())

# 그래프 간선 초기화
graph = []
for i in range(n):
    graph.append([])

# 그래프 간선 입력
for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

def bfs(start):
    from collections import deque
    # 필요 변수 선언
    q = deque([start-1])
    visited = []

    while q:
      current = q.popleft()
      if current not in visited:
        visited.append(current)
      q.extend(sorted(list(set(graph[current]) - set(visited))))

    return " ".join([str(i + 1) for i in visited])
      

def dfs(start):
  # 필요한 변수 선언
  stack = [start-1]
  visited = []

  while stack:
    current = stack.pop()
    if current not in visited:
      visited.append(current)
      stack.extend(sorted(list(set(graph[current]) - set(visited)), reverse=True))
  
  return " ".join([str(i + 1) for i in visited])

print(dfs(v))
print(bfs(v))