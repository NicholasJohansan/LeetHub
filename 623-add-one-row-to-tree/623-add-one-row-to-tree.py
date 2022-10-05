# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val=val, left=root)
            return new_root
        stack = [root]
        iteration = 0
        while stack:
            iteration += 1
            nodes = stack
            stack = []
            if not iteration == depth - 1:
                for node in nodes:
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
            else:
                for node in nodes:
                    new_left_node = TreeNode(val=val, left=node.left)
                    new_right_node = TreeNode(val=val, right=node.right)
                    node.left = new_left_node
                    node.right = new_right_node
                return root
        return root