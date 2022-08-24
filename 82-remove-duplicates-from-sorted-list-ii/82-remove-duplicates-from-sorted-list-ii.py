# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-101, head)
        prev_pointer = dummy_head
        start_pointer = dummy_head
        node_pointer = head
        iteration = 0
        while node_pointer:
            if prev_pointer.val != node_pointer.val:
                if iteration != 0:
                    start_pointer.next = node_pointer if node_pointer else None
                    prev_pointer = start_pointer
                    iteration = 0
                    if node_pointer.next:
                        prev_pointer = node_pointer
                        node_pointer = node_pointer.next
                    continue
                start_pointer = prev_pointer
                iteration = 0
            else:
                iteration += 1
            prev_pointer = node_pointer
            node_pointer = node_pointer.next
        if iteration != 0:
            start_pointer.next = node_pointer if node_pointer else None
        return dummy_head.next
        