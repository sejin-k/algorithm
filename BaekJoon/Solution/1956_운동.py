# 플로이드 와샬 알고리즘 (pypy3 : 통과, python3 : timeout)
INF = 10001
v, e = map(int, input().split())
map_ = [[INF] * v for i in range(v)]
min_ = INF

for i in range(e):
    s, e, d = map(int, input().split())
    map_[s-1][e-1] = d
    
for i in range(v):
    for j in range(v):
        for k in range(v):
            map_[i-1][j-1] = min(map_[i-1][j-1], map_[i-1][k] + map_[k][j-1])

for i in range(v):
    if min_ > map_[i][i]: min_ = map_[i][i]

if min_ == INF: print(-1)
else: print(min_)
    
    
# # dfs -> timeout
# graph = []
# distance = {}
# v, e = map(int, input().split())

# for i in range(v+1):
#     graph.append([])
    
# # 그래프 간선 입력
# for _ in range(e):
#     s, e, d = map(int, input().split())
#     graph[s].append(e)
#     distance[(s, e)] = d
    
# ## dfs(재귀함수) timeout
# INF = 10001
# min_ = INF
                
# def dfs(start, current, visited):
#     global min_
    
#     if current not in visited:
#         visited_t = visited.copy()
#         visited_t.append(current)
        
#         for i in graph[current]:
#             dfs(start, i, visited_t)
    
#     else:
#         if current == start:
#             visited_t = visited.copy()
#             visited_t.append(current)
#             circle = min_distance(visited_t)
#             if min_ > circle: min_ = circle 
            
# def min_distance(visited):
#     dis = 0
#     for i in range(len(visited)-1):
#         dis += distance[(visited[i], visited[i+1])]
        
#     return dis


# visited = []
# for i in range(1, v+1):
#     dfs(i, i, visited)

# if min_ == INF: print(-1)
# else: print(min_)