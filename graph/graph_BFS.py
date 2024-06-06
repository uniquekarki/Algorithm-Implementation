def BFS(nodes, start):
    bfs_result = [start]
    queue = [start]
    visited = set([start])
    while queue:
        current = queue.pop(0)
        for i in nodes[current]:
            if i not in visited:
                queue.append(i)
                bfs_result.append(i)
                visited.add(i)
    return bfs_result

nodes = [[3,1], [0,2,4,6,7], [1,3,8,9],[0,2], [1,5,6,7], [4], [1,4,7],[1,4,6], [2], [2]]
start = 0
print("BFS:", BFS(nodes, start))