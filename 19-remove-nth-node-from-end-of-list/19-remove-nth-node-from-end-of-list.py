# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        current_node = head
        while current_node.next != None:
            current_node = current_node.next
            length += 1
        index = 1
        previous_node = None
        current_node = head
        while index < length - (n - 1):
            previous_node = current_node
            current_node = current_node.next
            index += 1
        if previous_node != None:
            if current_node.next != None:
                previous_node.next = current_node.next
            else:
                previous_node.next = None
        if current_node == head:
            if current_node.next != None:
                return current_node.next
            else:
                return None
        return head
            
        