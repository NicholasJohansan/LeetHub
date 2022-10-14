# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        mid = head
        end = head.next.next
        while end and end.next:
            mid = mid.next
            end = end.next.next
        mid.next = mid.next.next
        return head