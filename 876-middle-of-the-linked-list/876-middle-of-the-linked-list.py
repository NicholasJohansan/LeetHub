# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        current_node = head
        while current_node.next != None:
            length += 1
            current_node = current_node.next
        mid = (length // 2) + 1
        index = 1
        current_node = head
        while index < mid:
            index += 1
            current_node = current_node.next
        return current_node
            
        