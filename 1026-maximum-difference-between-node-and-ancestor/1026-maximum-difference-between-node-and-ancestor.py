# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        queue = [(root, [])]
        max_diff = 0
        while queue:
            node, ancestors = queue.pop()
            ancestors += [node.val]
            if node.left:
                queue.append((node.left, ancestors + [node.left.val]))
                diff = self.calc_max_ancestor_diff(node.left, ancestors)
                max_diff = max(max_diff, diff)
            if node.right:
                queue.append((node.right, ancestors + [node.right.val]))
                diff = self.calc_max_ancestor_diff(node.right, ancestors)
                max_diff = max(max_diff, diff)
        return max_diff
    
    def calc_max_ancestor_diff(self, node: TreeNode, ancestors: List[int]) -> int:
        max_diff = 0
        val = node.val
        for ancestor in ancestors:
            max_diff = max(max_diff, abs(val - ancestor))
        return max_diff