# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, num_sum = stack.pop()
            if node.left:
                stack.append((node.left, num_sum + node.left.val))
            if node.right:
                stack.append((node.right, num_sum + node.right.val))
            if not node.left and not node.right:
                if num_sum == targetSum:
                    return True
        return False