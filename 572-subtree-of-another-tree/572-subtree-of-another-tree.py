# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = [root]
        while queue:
            node = queue.pop()
            # check if same as subtree
            check_queue = [(node, subRoot)]
            same = []
            while check_queue:
                main_node, compared_node = check_queue.pop(0)
                if main_node and compared_node:
                    if main_node.val == compared_node.val:
                        same.append(True)
                        check_queue.append((main_node.left, compared_node.left))
                        check_queue.append((main_node.right, compared_node.right))
                    else:
                        same = [False]
                        break
                elif main_node or compared_node:
                    same = [False]
                    break
            if all(same):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False