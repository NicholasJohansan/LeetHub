# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        bst_sum = 0
        val_range = range(low, high+1)
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val in val_range:
                bst_sum += node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return bst_sum