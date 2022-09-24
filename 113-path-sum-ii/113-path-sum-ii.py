# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, [root.val], root.val)]
        paths = []
        while stack:
            node, path, sum = stack.pop()
            if node.left:
                stack.append((node.left, path + [node.left.val], sum + node.left.val))
            if node.right:
                stack.append((node.right, path + [node.right.val], sum + node.right.val))
            if not node.left and not node.right:
                if sum == targetSum:
                    paths.append(path)
        return paths