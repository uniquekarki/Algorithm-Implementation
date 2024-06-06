class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class DFS:
    def dfs(self, root):
        def helper(node, path, count):
            new_path = path + [node.value]
            if not node:
                return None    
            elif not node.left and not node.right:
                if max(new_path) == node.value:
                    count += 1
                # print(f'{new_path} ==> {node.value}')
            else:
                if max(new_path) == node.value:
                    count += 1
                # print(f'{new_path} ==> {node.value}')
                if node.left:
                    helper(node.left,new_path, count)
                if node.right:
                    helper(node.right,new_path, count)
        count = 0
        helper(root, [], count)
        return count

root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(9)
root.right.right = Node(8)
root.left.right.left = Node(7)
root.left.right.right = Node(4)

dfs = DFS()
print(dfs.dfs(root))