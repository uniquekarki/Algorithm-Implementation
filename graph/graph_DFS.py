def DFS(nodes, start):
    dfs_result = [start]
    stack = [start]
    visited = set([start])
    while stack:
        current = stack[-1]
        flag = 0
        for i in nodes[current]:
            if i not in visited:
                dfs_result.append(i)
                stack.append(i)
                visited.add(i)
                flag += 1
                break
        if not flag:
            stack.pop()

    
    return dfs_result

nodes = [[3,1], [0,2,4,6,7], [1,3,8,9],[0,2], [1,5,6,7], [4], [1,4,7],[1,4,6], [2], [2]]
start = 0
print("DFS:", DFS(nodes, start))