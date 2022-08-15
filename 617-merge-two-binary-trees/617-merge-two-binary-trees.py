# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        self.root = None
        self.populate_tree(root1)
        self.populate_tree(root2)
        return self.root
    
    def populate_tree(self, orig_root):
        if not orig_root:
            return
        if not self.root:
            self.root = TreeNode()
        stack = [(orig_root, self.root)]
        while stack:
            node, new_node = stack.pop()
            if node.left:
                if not new_node.left:
                    new_node.left = TreeNode()
                stack.append((node.left, new_node.left))
            if node.right:
                if not new_node.right:
                    new_node.right = TreeNode()
                stack.append((node.right, new_node.right))
            if node.val:
                new_node.val += node.val