# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = True
        prev = None
        node = head
        while node:
            next_node = node.next
            if not next_node:
                break
            node.next, next_node.next = next_node.next, node
            if not prev:
                head = next_node
            if prev:
                prev.next = next_node
            prev = node
            node = node.next
        return head