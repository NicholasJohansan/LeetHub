# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = set()
        stack = [root]
        while stack:
            node = stack.pop()
            num = node.val
            if k - num in nums:
                return True
            nums.add(num)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False