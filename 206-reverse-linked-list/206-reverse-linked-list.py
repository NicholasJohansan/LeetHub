# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        pointer = head
        while pointer:
            vals.append(pointer.val)
            pointer = pointer.next
            
        head = None
        tail_pointer = None
        
        while vals:
            val = vals.pop()
            if head == None:
                head = ListNode(val=val)
                tail_pointer = head
            else:
                tail_pointer.next = ListNode(val=val)
                tail_pointer = tail_pointer.next
                
        return head