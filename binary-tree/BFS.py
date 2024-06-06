# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bfs(self,root):
        if not root:
            return []
        
        queue = [root]

        traverse = []

        while queue:
            node = queue.pop(0)
            traverse.append(node.val)

            if node.right:
                queue.append(node.right)

            if node.left:
                queue.append(node.left)
                
        return traverse


# Test cases
if __name__ == "__main__":
    # Example 1
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)


    solution = Solution()
    print('BFS:', solution.bfs(root))