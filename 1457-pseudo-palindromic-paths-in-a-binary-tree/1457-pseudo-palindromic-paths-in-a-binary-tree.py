# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_palindrome(self, frequency):
        odds = 0
        evens = 0
        for value in frequency.values():
            if value % 2 == 0:
                evens += 1
            else:
                odds += 1
        return odds <= 1
    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        palindromic_paths = 0
        stack = [(root, { root.val: 1 })]
        while stack:
            node, frequency = stack.pop()
            
            # end of path
            if node.left == None and node.right == None:
                if self.is_palindrome(frequency):
                    palindromic_paths += 1
                    
            if node.left:
                new_frequency = frequency.copy()
                new_frequency[node.left.val] = new_frequency.get(node.left.val, 0) + 1
                stack.append((node.left, new_frequency))
                
            if node.right:
                new_frequency = frequency.copy()
                new_frequency[node.right.val] = new_frequency.get(node.right.val, 0) + 1
                stack.append((node.right, new_frequency))
            
        return palindromic_paths